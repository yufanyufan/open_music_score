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
            Millimeters(5.6)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2120.9)
            PageWidth(1500.41)
            with PageMargins(type='even'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
            with PageMargins(type='odd'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Laudate Dominum', default_x=750.207, default_y=2049.47, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('From "Vesperae solennes de confessore" K. 339', default_x=750.207, default_y=1978.04, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('W. A. Mozart (1756-1791)', default_x=1428.99, default_y=1894.67, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Psalm 117', default_x=71.4286, default_y=1894.67, justify='left', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Soprano Solo')
            PartAbbreviation('Solo')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(59.8425)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P2'):
            PartName('Soprano')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(48.0315)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(49.6063)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(49.6063)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(53)
                Volume(50.3937)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P6'):
            PartName('Violins 1')
            PartAbbreviation('Vlns. 1')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Violins 1')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(6)
                MidiProgram(49)
                Volume(24.4094)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Violins 2')
            PartAbbreviation('Vlns. 2')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Violins 2')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(9)
                MidiProgram(49)
                Volume(28.3465)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Violoncellos')
            PartAbbreviation('Vlcs.')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Violoncellos')
            MidiDevice(None, id='P8-I1', port=1)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(13)
                MidiProgram(49)
                Volume(25.1969)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Contrabasses')
            PartAbbreviation('Cbs.')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('Contrabasses')
            MidiDevice(None, id='P9-I1', port=1)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(16)
                MidiProgram(49)
                Volume(25.9843)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=453.1):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(152.1)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Andante ma un poco sostenuto', default_x=-36.0, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12.5992')
                Sound(tempo=54.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=384.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=367.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=293.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=302.08):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=313.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=373.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=382.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-111.95, relative_x=15.09, relative_y=59.78):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-30.06)
            with Note(default_x=78.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-60.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('O', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=672.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=870.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=1068.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-99.15, relative_x=66.36, relative_y=53.75):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=78.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('sing', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=214.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=305.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=303.96):
            with Note(default_x=13.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('praise', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=157.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-112.4, relative_x=201.22, relative_y=51.75):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=206.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=253.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=304.89):
            with Note(default_x=13.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=84.86, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=96.87, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=110.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
                with Lyric(number='1', default_x=6.58, default_y=-51.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=124.73)
            with Note(default_x=158.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.24, default_y=-51.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lord,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='15', width=307.06):
            with Note(default_x=16.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('all', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=160.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=256.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('ye', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=81.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-54.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('na', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=140.27, default_y=-10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=152.29, default_y=-5.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=165.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=207.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-54.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('tions.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='17', width=306.18):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-95.07, relative_x=33.57, relative_y=49.67):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=23.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-54.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Praise', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='18', width=321.34):
            with Note(default_x=14.8, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=34.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-54.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('Him', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=177.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=273.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-54.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('ye', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=296.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=303.1):
            with Note(default_x=13.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-54.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('peo', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=109.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=156.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.11, default_y=-54.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('ple.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=78.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Praise', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='21', width=307.05):
            with Note(default_x=25.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.36, default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Him,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-106.21, relative_x=167.77, relative_y=51.31):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=164.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('all', font_family='Times New Roman', font_size='11.3393')
                    Extend()
        with Measure(number='22', width=295.04):
            with Note(default_x=13.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=152.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=198.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=247.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('ye', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='23', width=305.94):
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('souls', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=157.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=233.34, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=253.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('on', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=77.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.37, default_y=-52.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('earth.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=322.74):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-112.45, relative_x=22.36, relative_y=67.05):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('For', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=92.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-52.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('He', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=128.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('hath', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=180.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('shown', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=274.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('His', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='26', width=277.79):
            with Note(default_x=13.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-52.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=66.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=147.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='27', width=308.04):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-99.1, relative_x=0.72, relative_y=53.45):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-52.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=153.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.2, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=244.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=266.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=283.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-20.34)
            with Note(default_x=80.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-54.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('us,', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.79)
        with Measure(number='29', width=292.29):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-99.7, relative_x=4.01, relative_y=54.3):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-26.01)
            with Note(default_x=58.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_y=-54.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('His', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=100.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-111.38, relative_x=153.96, relative_y=54.48):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=143.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-54.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('love', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=185.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=228.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-35.91)
        with Measure(number='30', width=329.43):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-106.32, relative_x=2.81, relative_y=60.92):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-54.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mer', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=112.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=154.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Lyric(number='1', default_x=6.58, default_y=-54.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=178.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=2.58, default_y=-54.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ful', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='31', width=297.05):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-100.47, relative_x=24.17, relative_y=55.07):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=13.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-54.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=154.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=199.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=78.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.49, default_y=-64.31, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=393.74):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-110.63, relative_x=15.85, relative_y=56.55):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=16.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=204.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=266.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=329.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='34', width=431.4):
            with Note(default_x=14.8, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=34.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('truth', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=166.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=199.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('of', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=232.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('God', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-103.11, relative_x=71.81, relative_y=57.71):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=81.54, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-55.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=258.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=346.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=375.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-55.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('eth', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=406.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-55.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('for', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='36', width=403.6):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-55.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=141.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=172.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.11, default_y=-55.13, relative_y=-30.0):
                    Syllabic('end')
                    Text('er,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='37', width=426.87):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-102.93, relative_x=21.18, relative_y=57.53):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-55.13, relative_y=-30.0):
                    Syllabic('begin')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=78.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.36, default_y=-46.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('eth,', font_family='Times New Roman', font_size='11.3393')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-109.99, relative_x=233.85, relative_y=55.09):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=226.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='39', width=294.39):
            with Note(default_x=14.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=58.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=108.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=153.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=197.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('eth', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=247.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('for', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='40', width=294.39):
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('all', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=153.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=247.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='41', width=304.04):
            with Note(default_x=13.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.22, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=156.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=233.73, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=253.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=277.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ni', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-96.17, relative_x=90.24, relative_y=50.77):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ty.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='43', width=396.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='44', width=403.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='46', width=404.98):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='47', width=398.85):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='49', width=445.72):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='50', width=377.9):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='52', width=380.48):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='53', width=340.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='55', width=409.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='56', width=398.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='58', width=388.71):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='59', width=389.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='61', width=407.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='62', width=403.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-108.6, relative_x=89.72, relative_y=63.2):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-20.68)
            with Note(default_x=80.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.94, default_y=-40.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('A', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='64', width=405.25):
            with Direction(placement='above'):
                with DirectionType():
                    Words('-', default_y=19.4, font_family='Times New Roman')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-109.83, relative_x=6.5, relative_y=64.43):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=15.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-39.69)
        with Measure(number='65', width=411.62):
            with Direction(placement='above'):
                with DirectionType():
                    Words('-', default_y=19.47, font_family='Times New Roman')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-121.22, relative_x=7.14, relative_y=66.32):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=16.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=81.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=147.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=213.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=278.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=344.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.98, default_y=-40.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-110.1, relative_x=86.52, relative_y=49.79):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-38.85)
            with Note(default_x=86.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-52.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=116.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-95.24, relative_x=147.87, relative_y=46.56):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=146.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.7, default_y=-15.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-101.36, relative_x=205.44, relative_y=46.37):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=206.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('-', default_y=10.42, font_family='Times New Roman')
            with Note(default_x=266.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-52.92)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-95.26, relative_x=325.27, relative_y=49.86):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=296.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-35.79)
            with Note(default_x=357.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-94.89, relative_x=404.65, relative_y=49.49):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=387.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=417.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='67', width=425.57):
            with Direction(placement='above'):
                with DirectionType():
                    Words('-', default_y=5.4, font_family='Times New Roman')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-94.71, relative_x=9.83, relative_y=49.31):
                        Mp()
                Sound(dynamics=71.11)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-35.98)
            with Note(default_x=16.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-96.91, relative_x=205.93, relative_y=51.31):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=201.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-34.02)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-93.3, relative_x=304.51, relative_y=47.9):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=293.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=312.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-37.32)
            with Note(default_x=343.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=362.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=381.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=400.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.79)
        with Measure(number='68', width=394.11):
            with Direction(placement='above'):
                with DirectionType():
                    Words('-', default_y=50.42, font_family='Times New Roman')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-98.75, relative_x=5.72, relative_y=49.67):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    with Ornaments():
                        TrillMark()
            with Direction(placement='above'):
                with DirectionType():
                    Words('-', default_y=5.4, font_family='Times New Roman')
            with Note(default_x=259.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=352.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd', size='cue')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=371.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd', size='cue')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.11)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-92.82, relative_x=92.82, relative_y=47.42):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='70', width=334.6):
            with Direction(placement='above'):
                with DirectionType():
                    Words('ritard', default_y=5.9, font_weight='bold', font_style='italic', font_family='Times New Roman', font_size='12.5992')
                Sound(tempo=48.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='71', width=372.71):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='72', width=150.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=384.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=367.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=293.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=302.08):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=313.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=373.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=382.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.29)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.34)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=303.96):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=304.89):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=307.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.06)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=306.18):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=321.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=303.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.15)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=307.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=295.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=305.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.26)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=322.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=277.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=308.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.44)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=292.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=329.43):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=297.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.24)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=393.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=431.4):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.06)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=403.6):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=426.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.15)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='39', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=304.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=85.26, relative_y=-95.05):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.54, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-48.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glo', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=274.25, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=338.48, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=402.72, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='43', width=396.37):
            with Note(default_x=19.28, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('be', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=207.02, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=269.61, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=332.19, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='44', width=403.52):
            with Note(default_x=16.5, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fa', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=209.21, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-48.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('ther', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=273.45, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=337.69, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-104.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=208.46, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-104.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=272.1, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.85, default_y=-104.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=404.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=20.47, relative_y=-54.45):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=21.54, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-104.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=148.82, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-104.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.46, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-104.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ho', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=339.74, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-104.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=371.56, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=398.85):
            with Note(default_x=23.81, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-104.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Spir', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=148.29, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=210.53, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.1, default_y=-104.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('it,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=75.81, relative_y=-59.28):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('as', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='49', width=445.72):
            with Note(default_x=16.56, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('it', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='50', width=377.9):
            with Note(default_x=22.44, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('was', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.58, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('then', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=348.24, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=479.91, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('will', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='52', width=380.48):
            with Note(default_x=16.2, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=197.46, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=257.89, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.25, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.46, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=348.67, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='53', width=340.62):
            with Note(default_x=16.12, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('be,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=89.04, relative_y=-52.56):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=78.43, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-103.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('both', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=268.37, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-103.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('now', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=331.68, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=394.99, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-103.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='55', width=409.79):
            with Note(default_x=16.2, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-103.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-103.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('ways', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='56', width=398.76):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=14.81, relative_y=-54.16):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=13.06, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-103.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=205.11, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=301.13, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=333.14, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-103.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=365.15, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('with', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=216.7, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=250.58, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-47.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('out', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=285.06, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.36, default_y=-47.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('end,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='58', width=388.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=19.0, relative_y=-46.41):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.56, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='59', width=389.8):
            with Note(default_x=15.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-88.72, relative_x=85.26, relative_y=-51.04):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-134.76)
            with Note(default_x=86.54, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-142.07, relative_y=-30.0):
                    Syllabic('middle')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=271.11, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=337.33, relative_y=-52.16):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=332.64, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=394.16, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='61', width=407.82):
            with Note(default_x=19.91, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=226.76, relative_y=-49.18):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=213.06, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=277.45, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=309.64, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=341.84, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-142.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing,', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=374.03, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=403.34):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-90.22, relative_x=17.57, relative_y=-55.39):
                        Ff()
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-140.61)
            with Note(default_x=15.8, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-142.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman', font_size='11.3393')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=203.53, relative_y=-51.8):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=208.77, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-24.57)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-92.11, relative_x=330.66, relative_y=-53.5):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=337.42, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=87.83, relative_y=-103.36):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-136.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='64', width=405.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=6.5, relative_y=-92.07):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.84, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_y=-136.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='65', width=411.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=14.7, relative_y=-100.17):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.39)
            with Note(default_x=86.18, default_y=-143.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.62, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='67', width=425.57):
            with Note(default_x=15.8, default_y=-143.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='68', width=394.11):
            with Note(default_x=16.16, default_y=-143.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=76.92, default_y=-148.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=137.69, default_y=-153.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=198.45, default_y=-148.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    with Ornaments():
                        TrillMark()
            with Note(default_x=319.97, default_y=-148.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=352.33, default_y=-153.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd', size='cue')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=371.32, default_y=-148.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd', size='cue')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=85.26, relative_y=-103.41):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=81.18, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='70', width=334.6):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=173.03, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='71', width=372.71):
            with Note(default_x=24.94, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='72', width=150.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=384.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=367.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=293.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=302.08):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=313.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=373.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=382.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=303.96):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=304.89):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=307.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=306.18):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=321.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=303.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=307.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=295.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=305.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=322.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=277.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=308.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=292.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=329.43):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=297.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=393.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=431.4):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=403.6):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=426.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='39', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=304.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(114.56)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=81.48, relative_y=-243.62):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.54, default_y=-309.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glo', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=274.25, default_y=-309.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=338.48, default_y=-314.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('be', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=402.72, default_y=-319.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='43', width=396.37):
            with Note(default_x=19.28, default_y=-294.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=207.02, default_y=-294.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-58.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fa', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='44', width=403.52):
            with Note(default_x=16.5, default_y=-294.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=80.74, default_y=-299.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=144.98, default_y=-304.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=209.21, default_y=-299.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('ther', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=337.69, default_y=-299.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(134.13)
            with Note(default_x=81.18, default_y=-319.13):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-252.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=208.46, default_y=-319.13):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-252.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=272.1, default_y=-314.13):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.85, default_y=-252.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=404.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=18.58, relative_y=-202.04):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=21.54, default_y=-304.13):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-252.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=148.82, default_y=-304.13):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-252.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.46, default_y=-304.13):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-252.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ho', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=339.74, default_y=-304.13):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-252.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=371.56, default_y=-304.13):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=398.85):
            with Note(default_x=23.81, default_y=-299.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-252.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Spir', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=210.53, default_y=-304.13):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.1, default_y=-252.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('it,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.79)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=74.08, relative_y=-199.38):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-248.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('as', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='49', width=445.72):
            with Note(default_x=16.56, default_y=-253.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('it', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='50', width=377.9):
            with Note(default_x=22.44, default_y=-258.79):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('was', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.58, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('then', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=348.24, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=479.91, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('will', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='52', width=380.48):
            with Note(default_x=16.2, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=197.46, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=257.89, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.25, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.46, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-41.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=348.67, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='53', width=340.62):
            with Note(default_x=16.12, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-41.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('be,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(124.08)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=85.26, relative_y=-199.06):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=78.43, default_y=-304.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-250.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('both', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=268.37, default_y=-304.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-250.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('now', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=394.99, default_y=-304.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-250.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='55', width=409.79):
            with Note(default_x=16.2, default_y=-309.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-250.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.19, default_y=-304.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-250.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('ways', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='56', width=398.76):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=24.26, relative_y=-201.08):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.06, default_y=-304.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-250.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=205.11, default_y=-304.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=333.14, default_y=-304.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-250.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.92)
            with Note(default_x=81.18, default_y=-241.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-248.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('with', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=216.7, default_y=-241.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=250.58, default_y=-241.92):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-248.63, relative_y=-30.0):
                    Syllabic('end')
                    Text('out', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=285.06, default_y=-246.92):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.36, default_y=-248.63, relative_y=-30.0):
                    Syllabic('single')
                    Text('end,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='58', width=388.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=15.22, relative_y=-203.93):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.56, default_y=-246.92):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-248.63, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='59', width=389.8):
            with Note(default_x=15.44, default_y=-246.92):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-248.63, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(162.01)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=79.95, relative_y=-205.84):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=86.18, default_y=-337.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-255.56, relative_y=-30.0):
                    Syllabic('middle')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='61', width=407.82):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=22.52, relative_y=-206.83):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=19.91, default_y=-332.01):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.23, default_y=-255.56, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing,', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=213.06, default_y=-357.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-255.56, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='62', width=403.34):
            with Note(default_x=15.8, default_y=-357.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=208.77, default_y=-357.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=337.42, default_y=-347.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(155.94)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=90.93, relative_y=-242.78):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-335.94):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-56.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='64', width=405.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=10.28, relative_y=-250.82):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.84, default_y=-360.94):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-56.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='65', width=411.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=14.7, relative_y=-239.66):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-355.94):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=86.18, default_y=-258.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.62, default_y=-46.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='67', width=425.57):
            with Note(default_x=15.8, default_y=-263.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-46.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='68', width=394.11):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=11.39, relative_y=-250.27):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.8, default_y=-263.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(122.92)
            with Note(default_x=81.18, default_y=-317.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='70', width=334.6):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=173.03, default_y=-317.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='71', width=372.71):
            with Note(default_x=24.94, default_y=-317.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='72', width=150.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=384.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=367.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=293.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=302.08):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=313.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=373.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=382.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=303.96):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=304.89):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=307.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=306.18):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=321.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=303.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=307.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=295.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=305.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=322.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=277.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=308.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=292.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=329.43):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=297.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=393.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=431.4):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=403.6):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=426.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='39', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=304.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(263.13)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=77.7, relative_y=-387.98):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.54, default_y=-587.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glo', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=274.25, default_y=-587.7):
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
            with Note(default_x=338.48, default_y=-592.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=402.72, default_y=-597.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('be', font_family='Times New Roman', font_size='11.3393')
                    Extend()
        with Measure(number='43', width=396.37):
            with Note(default_x=19.28, default_y=-597.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.86, default_y=-592.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=144.44, default_y=-587.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=207.02, default_y=-582.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-46.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fa', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='44', width=403.52):
            with Note(default_x=16.5, default_y=-592.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=209.21, default_y=-592.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ther', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=337.69, default_y=-592.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(276.23)
            with Note(default_x=81.18, default_y=-625.36):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-405.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=208.46, default_y=-625.36):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-405.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=270.47, relative_y=-354.65):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=272.1, default_y=-630.36):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.85, default_y=-405.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=404.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=14.8, relative_y=-355.13):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=21.54, default_y=-610.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-405.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=148.82, default_y=-610.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-405.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.46, default_y=-610.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-405.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ho', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=339.74, default_y=-610.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-405.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=371.56, default_y=-610.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=398.85):
            with Note(default_x=23.81, default_y=-605.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-405.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Spir', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=148.29, default_y=-600.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=210.53, default_y=-595.36):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.1, default_y=-405.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('it,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(218.89)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=72.03, relative_y=-352.21):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-517.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-42.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('as', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='49', width=445.72):
            with Note(default_x=16.56, default_y=-497.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('it', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='50', width=377.9):
            with Note(default_x=22.44, default_y=-497.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('was', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.58, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('then', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=348.24, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=479.91, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('will', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='52', width=380.48):
            with Note(default_x=16.2, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-44.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=197.46, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=318.46, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='53', width=340.62):
            with Note(default_x=16.12, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-44.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('be,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(270.75)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=73.92, relative_y=-343.79):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=78.43, default_y=-594.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-401.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('both', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=268.37, default_y=-594.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-401.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('now', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=394.99, default_y=-594.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-401.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='55', width=409.79):
            with Note(default_x=16.2, default_y=-589.83):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-401.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.19, default_y=-594.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-401.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('ways', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='56', width=398.76):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=22.37, relative_y=-351.97):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.06, default_y=-594.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-401.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=205.11, default_y=-594.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=333.14, default_y=-594.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-401.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(267.56)
            with Note(default_x=81.18, default_y=-534.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-396.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('with', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=216.7, default_y=-534.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=250.58, default_y=-534.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-396.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('out', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=285.06, default_y=-534.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.36, default_y=-396.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('end,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='58', width=388.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=15.22, relative_y=-351.35):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.56, default_y=-534.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-396.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='59', width=389.8):
            with Note(default_x=15.44, default_y=-539.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-396.04, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(282.42)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=83.73, relative_y=-354.41):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=86.54, default_y=-639.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=271.11, default_y=-639.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=337.33, relative_y=-351.87):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=332.64, default_y=-634.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=394.16, default_y=-629.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.23, default_y=-40.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing,', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='61', width=407.82):
            with Note(default_x=19.91, default_y=-629.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-40.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=213.06, default_y=-654.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='62', width=403.34):
            with Note(default_x=15.8, default_y=-659.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=208.77, default_y=-649.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(270.58)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=92.82, relative_y=-386.59):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-636.52):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='64', width=405.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=12.17, relative_y=-390.3):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.84, default_y=-646.52):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='65', width=411.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=18.48, relative_y=-393.65):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-646.52):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(269.78)
            with Note(default_x=86.18, default_y=-553.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.62, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='67', width=425.57):
            with Note(default_x=15.8, default_y=-548.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='68', width=394.11):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=5.72, relative_y=-395.61):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.8, default_y=-543.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.86)
            with Note(default_x=81.18, default_y=-405.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='70', width=334.6):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=173.03, default_y=-400.78):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='71', width=372.71):
            with Note(default_x=24.94, default_y=-405.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='72', width=150.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=384.58):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=367.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=293.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=302.08):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=313.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='9', width=373.66):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=382.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=303.96):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=304.89):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=307.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=306.18):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=321.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=303.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=307.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=295.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=305.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='25', width=322.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=277.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=308.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=292.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=329.43):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=297.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=393.74):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=431.4):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=403.6):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=426.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='39', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=304.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(407.49)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=79.59, relative_y=-544.3):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.54, default_y=-1020.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glo', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=274.25, default_y=-1025.19):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='43', width=396.37):
            with Note(default_x=19.28, default_y=-1030.19):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('be', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=144.44, default_y=-1030.19):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-48.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=175.73, default_y=-1030.19):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.02, default_y=-1050.19):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='44', width=403.52):
            with Note(default_x=16.5, default_y=-1035.19):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fa', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=209.21, default_y=-1035.19):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('ther', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=337.69, default_y=-1035.19):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(425.3)
            with Note(default_x=81.18, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='11.3393')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=198.65, relative_y=-507.36):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=208.46, default_y=-1105.66):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=272.1, default_y=-1105.66):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.85, default_y=-46.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=404.98):
            with Note(default_x=21.54, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=148.82, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('the', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.46, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ho', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=339.74, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-46.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly', font_family='Times New Roman', font_size='11.3393')
                    Extend()
            with Note(default_x=371.56, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=398.85):
            with Note(default_x=23.81, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Spir', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=210.53, default_y=-1070.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.1, default_y=-46.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('it,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(371.72)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=72.19, relative_y=-496.64):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-914.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('as', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='49', width=445.72):
            with Note(default_x=16.56, default_y=-909.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('it', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='50', width=377.9):
            with Note(default_x=22.44, default_y=-904.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.77, relative_y=-30.0):
                    Syllabic('single')
                    Text('was', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.95)
            with Note(default_x=88.58, default_y=-455.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('then', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=348.24, default_y=-455.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=479.91, default_y=-455.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('will', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='52', width=380.48):
            with Note(default_x=16.2, default_y=-450.95):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=197.46, default_y=-450.95):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=318.46, default_y=-450.95):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='53', width=340.62):
            with Note(default_x=16.12, default_y=-450.95):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-40.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('be,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(430.78)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=79.59, relative_y=-496.02):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=78.43, default_y=-1085.61):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-543.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('both', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=268.37, default_y=-1085.61):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-543.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('now', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=394.99, default_y=-1085.61):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-543.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('and', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='55', width=409.79):
            with Note(default_x=16.2, default_y=-1080.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-543.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=212.19, default_y=-1085.61):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-543.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ways', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='56', width=398.76):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=24.26, relative_y=-493.77):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.06, default_y=-1050.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-543.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=205.11, default_y=-1050.61):
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
            with Note(default_x=333.14, default_y=-1050.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-543.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(421.49)
            with Note(default_x=81.18, default_y=-995.97):
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
                with Lyric(number='1', default_y=-539.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('with', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=216.7, default_y=-995.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=250.58, default_y=-995.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-539.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('out', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=285.06, default_y=-990.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.36, default_y=-539.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('end,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='58', width=388.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=13.33, relative_y=-494.43):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.56, default_y=-980.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-539.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ev', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='59', width=389.8):
            with Note(default_x=15.44, default_y=-975.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-539.12, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(373.92)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=79.95, relative_y=-490.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=86.18, default_y=-1038.35):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-538.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('last', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='61', width=407.82):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=16.85, relative_y=-489.89):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=19.55, default_y=-1033.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.59, default_y=-538.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing,', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='62', width=403.34):
            with Note(default_x=15.8, default_y=-1068.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-538.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman', font_size='11.3393')
            with Note(default_x=208.77, default_y=-1068.35):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=337.42, default_y=-1068.35):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(417.56)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=90.93, relative_y=-530.41):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-1089.08):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-46.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='64', width=405.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=19.73, relative_y=-535.03):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.84, default_y=-1094.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-46.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='65', width=411.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=12.81, relative_y=-532.78):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-1099.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(422.87)
            with Note(default_x=86.18, default_y=-1016.04):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=8.62, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='67', width=425.57):
            with Note(default_x=15.8, default_y=-1011.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='68', width=394.11):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=11.39, relative_y=-529.24):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.8, default_y=-1011.04):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-495.78):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-41.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='70', width=334.6):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=173.03, default_y=-510.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.3393')
        with Measure(number='71', width=372.71):
            with Note(default_x=24.94, default_y=-530.78):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-41.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman', font_size='11.3393')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='72', width=150.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-259.35, relative_x=86.65, relative_y=-470.89):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-725.24)
            with Note(default_x=98.37, default_y=-560.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=274.94, default_y=-560.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=333.79, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=392.64, default_y=-550.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=384.58):
            with Note(default_x=13.06, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=198.02, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.67, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=321.32, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=367.78):
            with Note(default_x=13.06, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=189.62, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=248.47, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=307.33, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.53, default_y=-545.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=159.55, default_y=-540.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=172.77, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=217.57, default_y=-550.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-35.91)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=293.68):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=8.63, relative_y=-472.98):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.06, default_y=-525.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=152.19, default_y=-525.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=246.52, default_y=-530.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='6', width=302.08):
            with Note(default_x=13.06, default_y=-530.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.45, default_y=-535.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=96.46, default_y=-530.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=109.68, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=156.77, default_y=-540.0):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=313.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=7.58, relative_y=-480.9):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=16.2, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=164.11, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=262.83, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=287.43, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=210.81, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=243.91, default_y=-525.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=261.07, default_y=-530.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=278.24, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=295.4, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=312.57, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=373.66):
            with Note(default_x=13.06, default_y=-550.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=192.56, default_y=-550.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=252.39, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=282.31, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.22, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=342.14, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=382.06):
            with Note(default_x=13.06, default_y=-550.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=196.76, default_y=-550.0):
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
            with Note(default_x=257.99, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.61, default_y=-550.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.22, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.84, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-571.29):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=771.68, default_y=-596.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=870.71, default_y=-586.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=969.75, default_y=-571.29):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=1068.78, default_y=-586.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=1167.82, default_y=-596.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=101.1, default_y=-610.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.77, default_y=-600.34):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.44, default_y=-590.34):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.1, default_y=-600.34):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.77, default_y=-610.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=237.11, default_y=-610.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.77, default_y=-600.34):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.44, default_y=-590.34):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.11, default_y=-600.34):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.78, default_y=-610.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=303.96):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=36.84, default_y=-620.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=61.6, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.38, default_y=-590.34):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.16, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.93, default_y=-620.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=181.49, default_y=-620.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.25, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.03, default_y=-595.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.81, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.58, default_y=-620.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=304.89):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=37.76, default_y=-620.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.53, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.31, default_y=-595.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.09, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.86, default_y=-620.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=182.42, default_y=-615.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.18, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.96, default_y=-590.34):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.74, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=279.51, default_y=-615.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=307.06):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=39.94, default_y=-615.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=64.71, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.49, default_y=-590.34):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.27, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.03, default_y=-615.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=184.59, default_y=-615.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.36, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.14, default_y=-590.34):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.92, default_y=-605.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.68, default_y=-615.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=102.26, default_y=-579.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.34, default_y=-569.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.42, default_y=-554.06):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.5, default_y=-579.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=228.75, default_y=-584.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.83, default_y=-569.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.91, default_y=-559.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.99, default_y=-569.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.07, default_y=-584.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=306.18):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=74.99, default_y=-554.06):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.86, default_y=-544.06):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=212.6, default_y=-529.06):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=258.48, default_y=-554.06):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=321.34):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=81.24, default_y=-549.06):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.77, default_y=-539.06):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=223.73, default_y=-574.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=273.26, default_y=-559.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=303.1):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=59.89, default_y=-594.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=109.42, default_y=-569.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=207.83, default_y=-579.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=254.67, default_y=-569.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.62, default_y=-565.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=173.15, default_y=-540.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=263.53, default_y=-540.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=313.06, default_y=-530.15):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=307.05):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=70.26, default_y=-550.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.79, default_y=-535.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=210.16, default_y=-535.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=259.69, default_y=-525.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=295.04):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.24, default_y=-525.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.77, default_y=-515.15):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=198.15, default_y=-515.15):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=247.68, default_y=-505.15):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=305.94):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=60.74, default_y=-520.15):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.28, default_y=-530.15):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=203.77, default_y=-525.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=253.3, default_y=-545.15):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-593.27)
            with Note(default_x=77.74, default_y=-543.26):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.6, default_y=-568.26):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=22.68)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-88.91, relative_x=179.75, relative_y=-509.37):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=173.46, default_y=-563.26):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-593.46)
            with Note(default_x=219.64, default_y=-558.26):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=276.14, relative_y=-511.62):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=265.83, default_y=-553.26):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=312.01, default_y=-548.26):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-37.8)
        with Measure(number='25', width=322.74):
            with Note(default_x=21.04, default_y=-543.26):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=128.84, default_y=-558.26):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=180.07, default_y=-558.26):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=274.62, default_y=-553.26):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='26', width=277.79):
            with Note(default_x=13.06, default_y=-553.26):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.41, default_y=-543.26):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=107.1, default_y=-548.26):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=188.48, default_y=-548.26):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=229.17, default_y=-558.26):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='27', width=308.04):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=62.88, default_y=-558.26):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.8, default_y=-533.26):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=200.24, default_y=-533.26):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=244.16, default_y=-508.26):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.52, default_y=-558.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=170.68, default_y=-533.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=260.18, default_y=-513.44):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=303.33, default_y=-538.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=292.29):
            with Note(default_x=15.8, default_y=-543.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.26, default_y=-533.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.71, default_y=-538.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=185.62, default_y=-543.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=228.08, default_y=-548.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=329.43):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=62.77, default_y=-528.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.49, default_y=-553.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=228.39, default_y=-533.44):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=278.11, default_y=-558.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=297.05):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.82, default_y=-548.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=108.35, default_y=-548.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=199.87, default_y=-548.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=249.41, default_y=-548.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-701.54)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-597.42)
            with Note(default_x=138.21, default_y=-573.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-203.39, relative_x=209.99, relative_y=-503.15):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=197.98, default_y=-568.24):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-597.42)
            with Note(default_x=257.75, default_y=-563.24):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=347.95, relative_y=-508.52):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=317.52, default_y=-568.24):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=43.47)
            with Note(default_x=377.3, default_y=-573.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='33', width=393.74):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=78.82, default_y=-578.24):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=141.49, default_y=-568.24):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=266.82, default_y=-558.24):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=329.48, default_y=-568.24):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='34', width=431.4):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=100.6, default_y=-573.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=166.44, default_y=-583.24):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=298.12, default_y=-578.24):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=363.96, default_y=-593.24):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=140.43, default_y=-559.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=199.32, default_y=-549.06):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=317.09, default_y=-534.06):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=375.98, default_y=-549.06):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='36', width=403.6):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=78.49, default_y=-529.06):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=141.19, default_y=-554.06):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=266.58, default_y=-559.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=329.27, default_y=-534.06):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='37', width=426.87):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=84.45, default_y=-539.06):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.61, default_y=-549.06):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=288.94, default_y=-559.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=357.11, default_y=-574.06):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.57, default_y=-570.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.1, default_y=-560.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=275.36, default_y=-545.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=324.89, default_y=-535.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='39', width=294.39):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.73, default_y=-525.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=108.26, default_y=-500.15):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=197.73, default_y=-555.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=247.26, default_y=-525.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=294.39):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.73, default_y=-550.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=108.26, default_y=-525.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=197.73, default_y=-560.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=247.26, default_y=-550.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='41', width=304.04):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=60.25, default_y=-545.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.78, default_y=-520.15):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=204.16, default_y=-590.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=253.69, default_y=-565.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(563.81)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=113.66, default_y=-1674.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.78, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.89, default_y=-1649.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.01, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.13, default_y=-1674.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=306.37, default_y=-1674.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=338.48, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.6, default_y=-1649.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=402.72, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=434.84, default_y=-1674.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=396.37):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=50.57, default_y=-1669.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.86, default_y=-1659.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.15, default_y=-1649.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.44, default_y=-1659.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.73, default_y=-1669.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=238.32, default_y=-1669.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=269.61, default_y=-1659.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.9, default_y=-1649.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.19, default_y=-1659.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.48, default_y=-1669.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='44', width=403.52):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=48.62, default_y=-1679.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.74, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.86, default_y=-1649.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.98, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.1, default_y=-1679.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=241.33, default_y=-1679.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.45, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.57, default_y=-1654.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.69, default_y=-1664.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.8, default_y=-1679.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(526.87)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=113.0, default_y=-1692.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=144.82, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.64, default_y=-1667.53):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.46, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.28, default_y=-1692.53):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=321.49, relative_y=-644.96):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=303.92, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=335.74, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=367.56, default_y=-1662.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.38, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=431.2, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='46', width=404.98):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=53.36, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.18, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.0, default_y=-1662.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.82, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.64, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=244.28, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.1, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.92, default_y=-1662.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.74, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.56, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=398.85):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=54.93, default_y=-1682.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=86.05, default_y=-1672.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.17, default_y=-1662.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.29, default_y=-1672.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.41, default_y=-1682.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=241.65, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=272.77, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.89, default_y=-1662.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.01, default_y=-1677.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.13, default_y=-1687.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(516.15)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=109.83, relative_y=-657.14):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=121.95, default_y=-1505.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.16, default_y=-1495.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.37, default_y=-1485.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.58, default_y=-1495.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.78, default_y=-1505.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=297.2, default_y=-1505.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=326.41, default_y=-1495.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.61, default_y=-1485.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=384.82, default_y=-1495.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=414.03, default_y=-1505.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='49', width=445.72):
            with Note(default_x=16.92, default_y=-1445.55):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.3, default_y=-1445.55):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.89, default_y=-1450.55):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=197.06, default_y=-1455.55):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=214.22, default_y=-1460.55):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=231.39, default_y=-1465.55):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=248.55, default_y=-1470.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='50', width=377.9):
            with Note(default_x=22.8, default_y=-1475.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=140.64, default_y=-1475.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=317.38, default_y=-1475.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=346.84, default_y=-1450.55):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.19)
            with Note(default_x=88.58, default_y=-532.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=220.26, default_y=-532.15):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=253.17, default_y=-537.15):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=270.34, default_y=-542.15):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=287.5, default_y=-547.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=317.87, default_y=-552.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('64th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=348.24, default_y=-557.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=414.07, default_y=-557.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=479.91, default_y=-557.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='52', width=380.48):
            with Note(default_x=16.2, default_y=-547.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=197.46, default_y=-547.15):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=257.89, default_y=-552.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.25, default_y=-557.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=318.46, default_y=-562.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=348.67, default_y=-557.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='53', width=340.62):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-725.64)
            with Note(default_x=16.12, default_y=-562.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=69.94, default_y=-562.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=28.35)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-96.65, relative_x=135.66, relative_y=-633.98):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=123.75, default_y=-557.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-725.45)
            with Note(default_x=177.57, default_y=-552.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=260.4, relative_y=-637.4):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=231.39, default_y=-557.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=285.21, default_y=-562.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-26.46)
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(572.94)
            with Note(default_x=78.43, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=300.02, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=331.68, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.33, default_y=-1688.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.99, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=426.64, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='55', width=409.79):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=48.87, default_y=-1708.55):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.53, default_y=-1703.55):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.2, default_y=-1693.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.86, default_y=-1703.55):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.53, default_y=-1708.55):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=244.86, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=277.53, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.19, default_y=-1688.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=342.86, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.52, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='56', width=398.76):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=45.06, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=77.07, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.08, default_y=-1688.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.09, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.1, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=237.12, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=269.13, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.13, default_y=-1688.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.14, default_y=-1698.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.15, default_y=-1713.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(558.05)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=115.06, default_y=-1644.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.94, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.82, default_y=-1609.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.7, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.58, default_y=-1644.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=355.51, relative_y=-645.32):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=318.94, default_y=-1639.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.82, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.7, default_y=-1614.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=420.58, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=454.46, default_y=-1639.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='58', width=388.71):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=47.77, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.62, default_y=-1619.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.47, default_y=-1614.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.32, default_y=-1619.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.17, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=232.87, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.71, default_y=-1619.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.56, default_y=-1614.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.41, default_y=-1619.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=356.26, default_y=-1629.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='59', width=389.8):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=46.83, default_y=-1634.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=77.87, default_y=-1624.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.9, default_y=-1614.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.93, default_y=-1624.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.97, default_y=-1634.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=233.03, default_y=-1634.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=264.07, default_y=-1624.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.1, default_y=-1614.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.13, default_y=-1624.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.17, default_y=-1634.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(558.55)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=117.3, default_y=-1706.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.06, default_y=-1686.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.83, default_y=-1676.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.59, default_y=-1686.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.35, default_y=-1706.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=301.87, default_y=-1706.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=332.64, default_y=-1686.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.4, default_y=-1676.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.16, default_y=-1686.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.92, default_y=-1706.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='61', width=407.82):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=52.1, default_y=-1701.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.29, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.49, default_y=-1676.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.68, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.87, default_y=-1701.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=245.26, default_y=-1701.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=277.45, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.64, default_y=-1676.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.84, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=374.03, default_y=-1701.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=403.34):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=47.96, default_y=-1706.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.12, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.29, default_y=-1676.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.45, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.61, default_y=-1706.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=247.12, relative_y=-654.96):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=240.93, default_y=-1706.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.09, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.26, default_y=-1676.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.42, default_y=-1691.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.58, default_y=-1696.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(554.54)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=124.95, relative_y=-696.9):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=111.91, default_y=-1723.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.64, default_y=-1708.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.38, default_y=-1698.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.11, default_y=-1708.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.84, default_y=-1723.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=327.04, default_y=-1673.62):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=388.51, default_y=-1663.62):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='64', width=405.25):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=80.43, default_y=-1698.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.72, default_y=-1688.62):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=275.18, default_y=-1678.62):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=339.42, default_y=-1663.62):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='65', width=411.62):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=81.8, default_y=-1663.62):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.45, default_y=-1638.62):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=278.73, default_y=-1663.62):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=344.38, default_y=-1638.62):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(548.76)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=146.64, default_y=-1549.8):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=206.75, default_y=-1574.8):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=326.96, default_y=-1549.8):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=387.06, default_y=-1574.8):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='67', width=425.57):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.77, default_y=-1599.8):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=139.39, default_y=-1554.8):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=262.62, default_y=-1554.8):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=343.04, default_y=-1574.8):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='68', width=394.11):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=76.92, default_y=-1589.8):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.69, default_y=-1559.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=259.21, default_y=-1559.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=319.97, default_y=-1579.8):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.13)
            with Note(default_x=81.18, default_y=-590.91):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=245.28, default_y=-575.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=354.68, default_y=-595.91):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='70', width=334.6):
            with Note(default_x=13.06, default_y=-590.91):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.03, default_y=-610.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=279.67, default_y=-630.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='71', width=372.71):
            with Note(default_x=24.94, default_y=-625.91):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=198.02, default_y=-640.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=198.02, default_y=-615.91):
                Chord()
                with Pitch():
                    Step('A')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='72', width=150.16):
            with Note(default_x=15.8, default_y=-650.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-625.91):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(709.75)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=80.98, relative_y=-584.3):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=98.01, default_y=-1309.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=384.58):
            with Note(default_x=12.7, default_y=-1309.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='3', width=367.78):
            with Note(default_x=13.06, default_y=-1309.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=189.62, default_y=-1314.75):
                with Pitch():
                    Step('E')
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
            with Note(default_x=307.33, default_y=-1304.75):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(536.67)
            with Note(default_x=78.43, default_y=-1131.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=217.57, default_y=-1136.67):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=293.68):
            with Note(default_x=12.7, default_y=-1126.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='6', width=302.08):
            with Note(default_x=13.06, default_y=-1121.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=156.77, default_y=-1126.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='7', width=313.62):
            with Note(default_x=15.84, default_y=-1126.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.07, default_y=-660.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='9', width=373.66):
            with Note(default_x=13.06, default_y=-665.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=192.56, default_y=-660.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='10', width=382.06):
            with Note(default_x=13.06, default_y=-655.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=196.76, default_y=-650.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=319.22, default_y=-670.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-676.29):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=303.96):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=304.89):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=307.06):
            with Note(default_x=15.8, default_y=-720.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-694.06):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=207.67, default_y=-699.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='17', width=306.18):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=321.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=303.1):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='21', width=307.05):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=295.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=305.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(567.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-704.78)
            with Note(default_x=77.74, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.83, default_y=-1200.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.6, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.36, default_y=-1200.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=179.75, relative_y=-618.98):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=173.46, default_y=-1180.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.55, default_y=-1200.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-32.13)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-704.78)
            with Note(default_x=219.64, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.73, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.83, default_y=-1170.93):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=287.48, relative_y=-621.23):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=288.92, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.01, default_y=-1180.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=335.1, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=322.74):
            with Note(default_x=21.04, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.3, default_y=-1200.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.07, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.33, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.84, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.8, default_y=-1200.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=203.33, default_y=-1200.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.09, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.36, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.62, default_y=-1170.93):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.88, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=277.79):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=33.4, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.41, default_y=-1170.93):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.75, default_y=-1160.93):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.1, default_y=-1165.93):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.44, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=168.13, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=188.48, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.82, default_y=-1165.93):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.17, default_y=-1175.93):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.83, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=308.04):
            with Note(default_x=15.8, default_y=-1185.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-688.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=217.02, default_y=-678.44):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
        with Measure(number='29', width=292.29):
            with Note(default_x=15.8, default_y=-683.44):
                with Pitch():
                    Step('D')
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
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='30', width=329.43):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=297.05):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.82, default_y=-673.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=108.35, default_y=-673.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=199.87, default_y=-673.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=249.41, default_y=-673.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(673.79)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=108.32, default_y=-1307.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.21, default_y=-1297.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.09, default_y=-1307.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=219.44, relative_y=-617.82):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=197.98, default_y=-1292.03):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.87, default_y=-1307.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-702.16)
            with Note(default_x=257.75, default_y=-1287.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=287.64, default_y=-1307.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.52, default_y=-1292.03):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=349.84, relative_y=-615.27):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=347.41, default_y=-1307.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=377.3, default_y=-1297.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=15.12)
            with Note(default_x=407.18, default_y=-1307.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=393.74):
            with Note(default_x=15.8, default_y=-1327.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='34', width=431.4):
            with Note(default_x=34.76, default_y=-1322.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=232.28, default_y=-1327.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-709.06):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='36', width=403.6):
            with Note(default_x=15.8, default_y=-694.06):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=203.88, default_y=-699.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='37', width=426.87):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='39', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=294.39):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='41', width=304.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-1789.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='43', width=396.37):
            with Note(default_x=18.92, default_y=-1789.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='44', width=403.52):
            with Note(default_x=16.5, default_y=-1789.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(664.47)
            with Note(default_x=81.18, default_y=-2397.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=272.1, default_y=-2402.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=404.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=24.25, relative_y=-753.71):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.18, default_y=-2392.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='47', width=398.85):
            with Note(default_x=23.81, default_y=-2387.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=210.53, default_y=-2392.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(676.65)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=68.25, relative_y=-761.7):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=92.38, default_y=-2227.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
        with Measure(number='49', width=445.72):
            with Note(default_x=16.56, default_y=-2232.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='50', width=377.9):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(699.83)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='52', width=380.48):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='53', width=340.62):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-832.63)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=43.03, default_y=-1321.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=69.94, default_y=-1311.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.84, default_y=-1321.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=135.66, relative_y=-743.96):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=123.75, default_y=-1306.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=150.66, default_y=-1321.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-832.02)
            with Note(default_x=177.57, default_y=-1301.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.48, default_y=-1321.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=256.62, relative_y=-741.53):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=231.39, default_y=-1306.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.3, default_y=-1321.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.21, default_y=-1311.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.11, default_y=-1321.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-18.9)
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=110.09, default_y=-1818.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.75, default_y=-1803.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.4, default_y=-1793.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.06, default_y=-1803.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.71, default_y=-1818.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='55', width=409.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='56', width=398.76):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(664.84)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='58', width=388.71):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='59', width=389.8):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='61', width=407.82):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='62', width=403.34):
            with Note(default_x=15.8, default_y=-1816.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=208.77, default_y=-1816.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=337.42, default_y=-1801.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(716.41)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=77.7, relative_y=-804.07):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=81.18, default_y=-2490.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='64', width=405.25):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='65', width=411.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='67', width=425.57):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='68', width=394.11):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=272.63, default_y=-725.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=299.98, default_y=-715.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.33, default_y=-710.91):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=354.68, default_y=-715.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=382.04, default_y=-725.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='70', width=334.6):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=39.72, default_y=-730.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.38, default_y=-720.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.04, default_y=-710.91):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.7, default_y=-720.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.36, default_y=-730.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='71', width=372.71):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=53.79, default_y=-755.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.63, default_y=-745.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.48, default_y=-730.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.33, default_y=-745.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.18, default_y=-755.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=226.87, default_y=-755.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=255.72, default_y=-745.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.57, default_y=-730.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.41, default_y=-745.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=342.26, default_y=-755.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='72', width=150.16):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(633.83)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=137.67, relative_y=-678.77):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=157.23, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.66, default_y=-1923.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.08, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.51, default_y=-1948.58):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=304.36, default_y=-1948.58):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=333.79, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.22, default_y=-1923.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=392.64, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=422.07, default_y=-1948.58):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=384.58):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=43.88, default_y=-1943.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.71, default_y=-1933.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.54, default_y=-1923.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.36, default_y=-1933.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.19, default_y=-1943.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=228.84, default_y=-1943.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.67, default_y=-1933.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.5, default_y=-1923.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.32, default_y=-1933.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.15, default_y=-1943.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=367.78):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=42.48, default_y=-1953.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.91, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.34, default_y=-1923.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.76, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.19, default_y=-1953.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=219.05, default_y=-1953.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=248.47, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.9, default_y=-1928.58):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.33, default_y=-1938.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.75, default_y=-1953.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=100.83, default_y=-1221.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.23, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.0, default_y=-1186.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.77, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.17, default_y=-1211.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=239.97, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=262.36, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.13, default_y=-1181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.9, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.3, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=293.68):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=35.46, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=57.86, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.62, default_y=-1181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.39, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.79, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=174.59, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=196.99, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.75, default_y=-1181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.52, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.92, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=302.08):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=36.6, default_y=-1201.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=60.15, default_y=-1191.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.91, default_y=-1181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.68, default_y=-1191.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.22, default_y=-1201.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=180.31, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=203.86, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.63, default_y=-1181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.39, default_y=-1196.67):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.94, default_y=-1206.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=313.62):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=40.8, default_y=-1201.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.39, default_y=-1191.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.16, default_y=-1181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.92, default_y=-1191.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.52, default_y=-1201.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=188.71, default_y=-1201.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=213.3, default_y=-1191.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.07, default_y=-1181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.83, default_y=-1191.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.43, default_y=-1201.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=111.53, default_y=-730.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=144.62, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.72, default_y=-705.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.81, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.91, default_y=-730.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=345.66, default_y=-730.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=378.76, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.85, default_y=-705.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=444.95, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=478.04, default_y=-730.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=373.66):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=42.97, default_y=-735.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=72.89, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.81, default_y=-710.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.72, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.64, default_y=-735.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=222.47, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=252.39, default_y=-720.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.31, default_y=-710.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.22, default_y=-720.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=342.14, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=382.06):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=43.67, default_y=-735.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.29, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.91, default_y=-710.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.52, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.14, default_y=-735.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=227.37, default_y=-730.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.99, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.61, default_y=-705.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.22, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.84, default_y=-730.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=177.47, default_y=-746.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=276.5, default_y=-736.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.54, default_y=-721.29):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=474.57, default_y=-736.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=573.61, default_y=-746.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=303.96):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=304.89):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=307.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=306.18):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=46.82, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.99, default_y=-739.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.92, default_y=-729.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.86, default_y=-739.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.79, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=189.67, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=212.6, default_y=-739.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.54, default_y=-729.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.48, default_y=-739.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.41, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=321.34):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=58.0, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.24, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.0, default_y=-724.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.77, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.01, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=200.49, default_y=-744.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=223.73, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.49, default_y=-724.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.26, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.5, default_y=-744.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=303.1):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=36.47, default_y=-744.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=59.89, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.65, default_y=-729.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.42, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.84, default_y=-744.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=179.67, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.83, default_y=-739.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.25, default_y=-729.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.67, default_y=-739.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.08, default_y=-749.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=101.03, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.62, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.39, default_y=-715.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.15, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.75, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=240.93, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.53, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.29, default_y=-715.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.06, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.65, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=307.05):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=47.66, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.26, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.02, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.79, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.38, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=187.57, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=210.16, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.93, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.69, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.29, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=295.04):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=35.65, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.24, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.01, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.77, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.37, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=175.56, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=198.15, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.92, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.68, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.27, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=305.94):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=37.37, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=60.74, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.51, default_y=-715.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.28, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.65, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=180.39, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=203.77, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.53, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.3, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.67, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(684.77)
            with Note(default_x=77.74, default_y=-1885.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='25', width=322.74):
            with Note(default_x=21.04, default_y=-1885.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.07, default_y=-1885.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='26', width=277.79):
            with Note(default_x=13.06, default_y=-1885.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=147.79, default_y=-1885.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='27', width=308.04):
            with Attributes():
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=40.93, default_y=-1910.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.88, default_y=-1900.7):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.84, default_y=-1890.7):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.8, default_y=-1900.7):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.75, default_y=-1910.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=178.29, default_y=-1910.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.24, default_y=-1900.7):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.2, default_y=-1890.7):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.16, default_y=-1900.7):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.11, default_y=-1910.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=16.16, default_y=-1915.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=153.52, default_y=-1915.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=105.94, default_y=-793.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.52, default_y=-778.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.1, default_y=-768.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.68, default_y=-778.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.26, default_y=-793.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=238.6, default_y=-778.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=260.18, default_y=-768.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.76, default_y=-758.44):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.33, default_y=-768.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.91, default_y=-778.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=81.18, default_y=-803.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=217.02, default_y=-803.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
        with Measure(number='29', width=292.29):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=37.03, default_y=-778.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.26, default_y=-753.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.48, default_y=-778.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.71, default_y=-753.44):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.94, default_y=-778.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=164.4, default_y=-788.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.62, default_y=-763.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.85, default_y=-788.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.08, default_y=-768.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.31, default_y=-788.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-798.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=143.17, default_y=-798.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
        with Measure(number='30', width=329.43):
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=37.92, default_y=-738.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.77, default_y=-728.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.63, default_y=-713.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.49, default_y=-728.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.35, default_y=-738.44):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=203.53, default_y=-743.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.39, default_y=-728.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.25, default_y=-718.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.11, default_y=-728.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.97, default_y=-743.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=297.05):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=35.94, default_y=-743.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.82, default_y=-733.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.58, default_y=-718.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.35, default_y=-733.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.23, default_y=-743.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=176.99, default_y=-743.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.87, default_y=-733.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.64, default_y=-718.44):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.41, default_y=-733.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.29, default_y=-743.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(674.4)
            with Note(default_x=78.43, default_y=-1996.43):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='33', width=393.74):
            with Attributes():
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=47.49, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.82, default_y=-2006.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.16, default_y=-1996.43):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.49, default_y=-2006.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.82, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=235.48, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=266.82, default_y=-2006.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.15, default_y=-1996.43):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.48, default_y=-2006.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.81, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='34', width=431.4):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=67.68, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.6, default_y=-2011.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.52, default_y=-2001.43):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.44, default_y=-2011.43):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.36, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=265.2, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.12, default_y=-2006.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.04, default_y=-1996.43):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.96, default_y=-2006.43):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=396.88, default_y=-2021.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=110.98, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.43, default_y=-779.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.87, default_y=-769.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.32, default_y=-779.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.76, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=287.65, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=317.09, default_y=-779.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.54, default_y=-769.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.98, default_y=-779.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=406.69, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=403.6):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=47.15, default_y=-809.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.49, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.84, default_y=-774.06):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.19, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.54, default_y=-809.06):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=235.23, default_y=-804.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=266.58, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.92, default_y=-779.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.27, default_y=-794.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=360.62, default_y=-804.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='37', width=426.87):
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=50.28, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.45, default_y=-724.06):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.53, default_y=-719.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.61, default_y=-724.06):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.69, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=254.86, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=288.94, default_y=-724.06):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.02, default_y=-719.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.11, default_y=-724.06):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.19, default_y=-734.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=103.0, default_y=-730.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.57, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.33, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.1, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.66, default_y=-730.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=250.79, default_y=-730.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=275.36, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.13, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.89, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.46, default_y=-730.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=294.39):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=36.37, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.73, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.5, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.26, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.63, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=175.36, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=197.73, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.5, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.26, default_y=-720.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.63, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=294.39):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=36.37, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=58.73, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.5, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.26, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.63, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=175.36, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=197.73, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.5, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.26, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.63, default_y=-735.15):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=304.04):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=36.65, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=60.25, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.01, default_y=-710.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.78, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.38, default_y=-740.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=180.57, default_y=-730.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.16, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.93, default_y=-715.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.69, default_y=-725.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.29, default_y=-730.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.54, default_y=-1834.0):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=274.25, default_y=-1839.0):
                with Pitch():
                    Step('E')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='43', width=396.37):
            with Note(default_x=19.28, default_y=-1844.0):
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=207.02, default_y=-1864.0):
                with Pitch():
                    Step('G')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='44', width=403.52):
            with Note(default_x=16.5, default_y=-1849.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=209.21, default_y=-1839.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=337.69, default_y=-1829.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(48.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=209.21, default_y=-1849.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('2')
                Type('quarter')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(773.22)
            with Note(default_x=81.18, default_y=-3155.22):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=272.1, default_y=-3190.22):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='46', width=404.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=28.03, relative_y=-862.41):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.54, default_y=-3155.22):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=212.46, default_y=-3155.22):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='47', width=398.85):
            with Note(default_x=23.81, default_y=-3155.22):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=210.53, default_y=-3190.22):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(781.21)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=70.14, relative_y=-868.26):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=92.75, default_y=-3008.41):
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=267.99, default_y=-3008.41):
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='49', width=445.72):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=49.52, default_y=-2983.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.11, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.7, default_y=-2958.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.3, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.89, default_y=-2983.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=281.15, default_y=-2983.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=313.74, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.33, default_y=-2958.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.93, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.52, default_y=-2983.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='50', width=377.9):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=52.26, default_y=-2988.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.72, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.18, default_y=-2963.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.64, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.09, default_y=-2988.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=229.01, default_y=-2988.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=258.47, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.92, default_y=-2963.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.38, default_y=-2978.41):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.84, default_y=-2988.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(812.62)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=121.5, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.42, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.34, default_y=-2099.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.26, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.17, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=381.15, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=414.07, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=446.99, default_y=-2099.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=479.91, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=512.83, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='52', width=380.48):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=46.41, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=76.62, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.83, default_y=-2099.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.04, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.25, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=227.68, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.89, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.25, default_y=-2099.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.46, default_y=-2109.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.67, default_y=-2124.6):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='53', width=340.62):
            with Note(default_x=16.12, default_y=-2149.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.07, default_y=-1883.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='55', width=409.79):
            with Note(default_x=16.2, default_y=-1888.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=212.19, default_y=-1883.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='56', width=398.76):
            with Note(default_x=13.06, default_y=-1883.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=205.11, default_y=-1883.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=269.13, default_y=-1873.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=333.14, default_y=-1863.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-2383.86):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=285.06, default_y=-2388.86):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='58', width=388.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=15.22, relative_y=-866.62):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=16.56, default_y=-2403.86):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
        with Measure(number='59', width=389.8):
            with Note(default_x=15.44, default_y=-2408.86):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=61.06, relative_y=-864.62):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=86.54, default_y=-1881.9):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=271.11, default_y=-1881.9):
                with Pitch():
                    Step('B')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='61', width=407.82):
            with Note(default_x=19.91, default_y=-1876.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=213.06, default_y=-1876.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='62', width=403.34):
            with Note(default_x=15.8, default_y=-1876.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=208.77, default_y=-1876.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=337.42, default_y=-1876.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(823.58)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=66.36, relative_y=-906.49):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=81.18, default_y=-3303.61):
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=296.31, default_y=-3283.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.04, default_y=-3268.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.78, default_y=-3258.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=388.51, default_y=-3268.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.24, default_y=-3283.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='64', width=405.25):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=48.32, default_y=-3283.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.43, default_y=-3273.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.6, default_y=-3263.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.72, default_y=-3273.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.83, default_y=-3283.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=243.07, default_y=-3283.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=275.18, default_y=-3273.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.3, default_y=-3263.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.42, default_y=-3273.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.54, default_y=-3283.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='65', width=411.62):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=48.98, default_y=-3278.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.8, default_y=-3268.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.63, default_y=-3258.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.45, default_y=-3268.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.27, default_y=-3278.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=245.91, default_y=-3278.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=278.73, default_y=-3268.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.56, default_y=-3258.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=344.38, default_y=-3268.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=377.2, default_y=-3278.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=116.59, default_y=-1789.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.64, default_y=-1769.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.7, default_y=-1759.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.75, default_y=-1769.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.8, default_y=-1789.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=296.91, default_y=-1789.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=326.96, default_y=-1769.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.01, default_y=-1759.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.06, default_y=-1769.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=417.12, default_y=-1789.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='67', width=425.57):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=46.97, default_y=-1784.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=77.77, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.58, default_y=-1759.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.39, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.2, default_y=-1784.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=231.81, default_y=-1784.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=262.62, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=293.42, default_y=-1759.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.04, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.55, default_y=-1784.8):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='68', width=394.11):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=46.54, default_y=-1789.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=76.92, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.31, default_y=-1759.8):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.69, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.07, default_y=-1789.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=228.83, default_y=-1779.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=259.21, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.59, default_y=-1764.8):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.97, default_y=-1774.8):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.36, default_y=-1779.8):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=108.53, default_y=-800.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.88, default_y=-790.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.23, default_y=-775.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.58, default_y=-790.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.93, default_y=-800.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=245.28, default_y=-790.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='70', width=334.6):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
            with Note(default_x=199.69, default_y=-805.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.35, default_y=-795.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.01, default_y=-790.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=279.67, default_y=-795.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.34, default_y=-805.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='71', width=372.71):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=198.02, default_y=-810.91):
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='72', width=150.16):
            with Note(default_x=15.8, default_y=-845.91):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P9'):
        with Measure(number='1', width=453.1):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(698.28)
            with Attributes():
                Divisions(16.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=79.09, relative_y=-786.88):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=98.37, default_y=-2696.86):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=274.94, default_y=-2701.86):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='2', width=384.58):
            with Note(default_x=13.06, default_y=-2706.86):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=198.02, default_y=-2726.86):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='3', width=367.78):
            with Note(default_x=13.06, default_y=-2711.86):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=189.62, default_y=-2711.86):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=359.06):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-1321.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=217.57, default_y=-1356.67):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=293.68):
            with Note(default_x=13.06, default_y=-1321.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=152.19, default_y=-1321.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=302.08):
            with Note(default_x=13.06, default_y=-1321.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=156.77, default_y=-1356.67):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=313.62):
            with Note(default_x=16.2, default_y=-1331.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=164.11, default_y=-1331.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='8', width=512.74):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-855.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=312.57, default_y=-855.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=373.66):
            with Note(default_x=13.06, default_y=-850.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=192.56, default_y=-870.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='10', width=382.06):
            with Note(default_x=13.06, default_y=-865.0):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=196.76, default_y=-865.0):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='11', width=1268.45):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-861.29):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=672.64, default_y=-866.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='12', width=352.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-890.34):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.44, default_y=-910.34):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='13', width=303.96):
            with Note(default_x=13.06, default_y=-895.34):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=157.71, default_y=-895.34):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='14', width=304.89):
            with Note(default_x=13.98, default_y=-880.34):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=158.64, default_y=-915.34):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='15', width=307.06):
            with Note(default_x=16.16, default_y=-880.34):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=160.81, default_y=-880.34):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=337.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-859.06):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=207.67, default_y=-894.06):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='17', width=306.18):
            with Note(default_x=23.88, default_y=-859.06):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=166.73, default_y=-859.06):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='18', width=321.34):
            with Note(default_x=34.76, default_y=-864.06):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=177.25, default_y=-874.06):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='19', width=303.1):
            with Note(default_x=13.06, default_y=-869.06):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=156.25, default_y=-889.06):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=360.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-865.15):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=218.34, default_y=-840.15):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='21', width=307.05):
            with Note(default_x=25.07, default_y=-850.15):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=164.97, default_y=-850.15):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='22', width=295.04):
            with Note(default_x=13.06, default_y=-850.15):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=152.96, default_y=-850.15):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='23', width=305.94):
            with Note(default_x=14.0, default_y=-880.15):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=157.02, default_y=-880.15):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=359.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.79)
            with Note(default_x=77.38, default_y=-2001.49):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='25', width=322.74):
            with Note(default_x=21.04, default_y=-2001.49):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='26', width=277.79):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=308.04):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=349.68):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.79)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='29', width=292.29):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=329.43):
            with Note(default_x=13.06, default_y=-889.23):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=178.68, default_y=-889.23):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='31', width=297.05):
            with Note(default_x=13.06, default_y=-884.23):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=154.11, default_y=-884.23):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='32', width=443.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=393.74):
            with Note(default_x=16.16, default_y=-2111.43):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=204.15, default_y=-2111.43):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='34', width=431.4):
            with Note(default_x=34.76, default_y=-2106.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=232.28, default_y=-2111.43):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=437.98):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='36', width=403.6):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=426.87):
            with Note(default_x=16.2, default_y=-884.06):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=220.78, default_y=-884.06):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='38', width=375.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-870.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=226.23, default_y=-870.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='39', width=294.39):
            with Note(default_x=14.0, default_y=-870.15):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=153.0, default_y=-870.15):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='40', width=294.39):
            with Note(default_x=14.0, default_y=-865.15):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=153.0, default_y=-865.15):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='41', width=304.04):
            with Note(default_x=13.06, default_y=-865.15):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=156.97, default_y=-865.15):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='42', width=468.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.54, default_y=-1974.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=81.54, default_y=-1939.0):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=274.25, default_y=-1979.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=274.25, default_y=-1944.0):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='43', width=396.37):
            with Note(default_x=19.28, default_y=-1984.0):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=19.28, default_y=-1949.0):
                Chord()
                with Pitch():
                    Step('D')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=207.02, default_y=-1969.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='44', width=403.52):
            with Note(default_x=16.5, default_y=-1989.0):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=16.5, default_y=-1954.0):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=209.21, default_y=-1989.0):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=209.21, default_y=-1954.0):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='45', width=464.62):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(881.92)
            with Note(default_x=81.18, default_y=-4112.14):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=81.18, default_y=-4077.14):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=272.1, default_y=-4112.14):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=272.1, default_y=-4077.14):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='46', width=404.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=28.03, relative_y=-949.53):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.54, default_y=-4112.14):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=21.54, default_y=-4077.14):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=212.46, default_y=-4112.14):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=212.46, default_y=-4077.14):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='47', width=398.85):
            with Note(default_x=23.81, default_y=-4112.14):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=23.81, default_y=-4077.14):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=210.53, default_y=-4112.14):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='48', width=444.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(887.77)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=66.36, relative_y=-953.12):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=92.75, default_y=-3971.19):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=92.75, default_y=-3936.19):
                Chord()
                with Pitch():
                    Step('D')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=267.99, default_y=-3971.19):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=267.99, default_y=-3936.19):
                Chord()
                with Pitch():
                    Step('D')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='49', width=445.72):
            with Note(default_x=16.92, default_y=-3931.19):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.55, default_y=-3931.19):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='50', width=377.9):
            with Note(default_x=22.8, default_y=-3926.19):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=199.55, default_y=-3926.19):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='51', width=547.34):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.58, default_y=-2259.6):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=88.58, default_y=-2224.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=348.24, default_y=-2259.6):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=348.24, default_y=-2224.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='52', width=380.48):
            with Note(default_x=16.2, default_y=-2254.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=16.2, default_y=-2219.6):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=197.46, default_y=-2254.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=197.46, default_y=-2219.6):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='53', width=340.62):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='54', width=459.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.43, default_y=-2013.55):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=78.43, default_y=-1978.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=268.37, default_y=-2013.55):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=268.37, default_y=-1978.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='55', width=409.79):
            with Note(default_x=16.2, default_y=-2008.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=16.2, default_y=-1973.55):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=212.19, default_y=-2013.55):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=212.19, default_y=-1978.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='56', width=398.76):
            with Note(default_x=13.06, default_y=-2013.55):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=13.06, default_y=-1978.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=205.11, default_y=-2013.55):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=205.11, default_y=-1978.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='57', width=489.94):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(886.13)
            with Note(default_x=81.18, default_y=-3364.99):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=81.18, default_y=-3329.99):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=312.04, relative_y=-957.34):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=285.06, default_y=-3359.99):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=285.06, default_y=-3324.99):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='58', width=388.71):
            with Note(default_x=16.92, default_y=-3349.99):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=202.02, default_y=-3349.99):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='59', width=389.8):
            with Note(default_x=15.8, default_y=-3379.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(0)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-3344.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=202.0, default_y=-3379.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(0)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=202.0, default_y=-3344.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='60', width=457.29):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(884.13)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=78.06, relative_y=-967.47):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=86.54, default_y=-2806.04):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=271.11, default_y=-2806.04):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='61', width=407.82):
            with Note(default_x=19.91, default_y=-2801.04):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=213.06, default_y=-2801.04):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='62', width=403.34):
            with Note(default_x=15.8, default_y=-2801.04):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=208.77, default_y=-2836.04):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=208.77, default_y=-2801.04):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=337.42, default_y=-2836.04):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=337.42, default_y=-2801.04):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
        with Measure(number='63', width=451.58):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(926.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=66.36, relative_y=-1000.99):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=81.18, default_y=-4304.62):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=81.18, default_y=-4269.62):
                Chord()
                with Pitch():
                    Step('D')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=265.58, default_y=-4269.62):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='64', width=405.25):
            with Note(default_x=16.2, default_y=-4274.62):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=210.95, default_y=-4274.62):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='65', width=411.62):
            with Note(default_x=16.16, default_y=-4279.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=213.09, default_y=-4279.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('quarter')
        with Measure(number='66', width=448.77):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=86.54, default_y=-1919.8):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=266.85, default_y=-1919.8):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='67', width=425.57):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.77, default_y=-1914.8):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=262.62, default_y=-1914.8):
                with Pitch():
                    Step('C')
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
        with Measure(number='68', width=394.11):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=76.92, default_y=-1914.8):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=259.21, default_y=-1914.8):
                with Pitch():
                    Step('C')
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
        with Measure(number='69', width=410.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=81.18, default_y=-915.91):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
        with Measure(number='70', width=334.6):
            with Note(default_x=13.06, default_y=-915.91):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=173.03, default_y=-930.91):
                with Pitch():
                    Step('C')
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
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='71', width=372.71):
            with Note(default_x=24.94, default_y=-950.91):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=198.02, default_y=-915.91):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('eighth')
        with Measure(number='72', width=150.16):
            with Note(default_x=15.8, default_y=-950.91):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(32.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')