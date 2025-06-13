with ScorePartwise(version='3.1'):
    MovementTitle('titulo')
    with Identification():
        Creator('W. A. Mozart', type='composer')
        Rights('Copyright')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.23192)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1642.31)
            PageWidth(1161.84)
            with PageMargins(type='even'):
                LeftMargin(55.3104)
                RightMargin(55.3104)
                TopMargin(55.3104)
                BottomMargin(110.621)
            with PageMargins(type='odd'):
                LeftMargin(55.3104)
                RightMargin(55.3104)
                TopMargin(55.3104)
                BottomMargin(110.621)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Times New Roman', font_size='13.7')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('1/3', default_x=1106.53, default_y=1482.0, justify='right', valign='bottom')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('W. A. Mozart\n', default_x=1106.53, default_y=1482.0, justify='right', valign='bottom', font_style='italic', font_size='11')
        CreditWords('(1756 - 1791)')
    with Credit(page=1):
        CreditType('title')
        CreditWords('6  NOTTURNI', default_x=580.919, default_y=1587.0, justify='center', valign='top', font_weight='bold', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('2.  SE LONTAN BEN MIO (KV 438)', default_x=580.919, default_y=1531.69, justify='center', valign='top', font_weight='bold', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Copyright', default_x=580.919, default_y=110.621, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Copyright', default_x=580.919, default_y=110.621, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Copyright', default_x=580.919, default_y=110.621, justify='center', valign='bottom', font_size='8')
    with Credit(page=4):
        CreditType('rights')
        CreditWords('Copyright', default_x=580.919, default_y=110.621, justify='center', valign='bottom', font_size='8')
    with Credit(page=5):
        CreditType('rights')
        CreditWords('Copyright', default_x=580.919, default_y=110.621, justify='center', valign='bottom', font_size='8')
    with Credit(page=6):
        CreditType('rights')
        CreditWords('Copyright', default_x=580.919, default_y=110.621, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(79.5276)
                Pan(33.0)
        with ScorePart(id='P2'):
            PartName('Mezzo-Soprano')
            PartAbbreviation('MS.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Mezzo-Soprano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(79.5276)
                Pan(10.0)
        with ScorePart(id='P3'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(79.5276)
                Pan(-12.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P4'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(79.5276)
                Pan(-34.0)
    with Part(id='P1'):
        with Measure(number='1', width=363.58):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(181.93)
                        RightMargin(-0.0)
                    TopSystemDistance(175.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', default_x=-37.31, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=55.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', default_x=-37.31, default_y=26.85, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=55.0)
            with Note(default_x=122.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Se')
            with Note(default_x=175.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lon')
            with Note(default_x=209.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=242.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=295.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben')
                    Extend()
            with Note(default_x=328.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='2', width=272.16):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=10.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio')
                    Extend()
            with Note(default_x=45.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
                    Extend()
            with Note(default_x=122.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=158.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=214.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
        with Measure(number='3', width=233.56):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=126.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=179.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='4', width=322.67):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.05)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=103.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=158.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni‿i')
            with Note(default_x=212.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=266.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='5', width=215.25):
            with Note(default_x=13.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.39, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
                    Extend()
            with Note(default_x=84.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=149.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=181.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
        with Measure(number='6', width=238.54):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=17.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-81.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=45.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=72.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=99.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('i')
            with Note(default_x=127.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=182.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
        with Measure(number='7', width=201.72):
            with Note(default_x=19.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.05, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=132.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('se')
            with Note(default_x=162.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lon')
        with Measure(number='8', width=978.17):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.05)
                        RightMargin(-0.0)
                    SystemDistance(144.48)
            with Note(default_x=115.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-42.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
                    Extend()
            with Note(default_x=330.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=761.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
        with Measure(number='9', width=378.66):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.05)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=111.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=170.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.09, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=266.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-53.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
                    Extend()
            with Note(default_x=303.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=340.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
        with Measure(number='10', width=410.47):
            with Note(default_x=20.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.09, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=63.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=106.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=149.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni‿i')
            with Direction(placement='above'):
                with DirectionType():
                    Words('rit.', relative_y=20.0, font_style='italic')
            with Note(default_x=192.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-53.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
                    Extend()
            with Note(default_x=219.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=300.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-53.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
                    Extend()
            with Note(default_x=327.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=354.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=189.05):
            with Note(default_x=15.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.39, default_y=-53.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('me!')
                    Extend()
            with Note(default_x=101.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='12', width=418.51):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.05)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=97.78)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', relative_y=20.0, font_style='italic')
            with Note(default_x=118.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural', parentheses='yes')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=174.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mo')
            with Note(default_x=200.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=277.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=334.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('ti‿i')
                    Extend()
            with Note(default_x=375.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='13', width=288.88):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=10.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gior')
            with Note(default_x=48.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
                    Extend()
            with Note(default_x=125.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=164.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mie')
            with Note(default_x=225.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='14', width=270.78):
            with Note(default_x=16.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('i')
            with Note(default_x=47.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=78.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('dol')
                    Extend()
            with Note(default_x=109.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=139.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.39, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,')
                    Extend()
            with Note(default_x=176.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=207.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=238.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='15', width=320.96):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.05)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=100.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=125.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
                    Extend()
            with Note(default_x=204.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=229.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
                    Extend()
            with Note(default_x=269.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=215.31):
            with Note(default_x=16.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('i')
            with Note(default_x=39.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=62.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('dol')
                    Extend()
            with Note(default_x=85.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.39, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,')
                    Extend()
            with Note(default_x=145.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=190.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='17', width=237.51):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=12.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=38.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=64.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no‿a')
            with Note(default_x=100.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=136.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-83.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=204.39):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=146.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='19', width=398.53):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(73.05)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=100.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=165.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=250.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=289.02):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Note(default_x=206.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='21', width=290.62):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=74.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=157.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=363.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(103.99)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=122.68, default_y=-183.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Se')
            with Note(default_x=175.86, default_y=-188.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lon')
            with Note(default_x=242.33, default_y=-193.99):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=295.51, default_y=-188.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben')
                    Extend()
            with Note(default_x=328.74, default_y=-183.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='2', width=272.16):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=10.12, default_y=-173.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio')
                    Extend()
            with Note(default_x=45.27, default_y=-178.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.77, default_y=-178.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
                    Extend()
            with Note(default_x=122.92, default_y=-183.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=158.07, default_y=-183.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=214.31, default_y=-188.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='3', width=233.56):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=126.86, default_y=-173.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=179.41, default_y=-178.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='4', width=322.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=103.7, default_y=-186.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=158.04, default_y=-186.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni‿i')
            with Note(default_x=212.38, default_y=-186.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=266.72, default_y=-186.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='5', width=215.25):
            with Note(default_x=13.64, default_y=-186.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.05, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.04, default_y=-181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
                    Extend()
            with Note(default_x=149.24, default_y=-176.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=181.44, default_y=-171.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
        with Measure(number='6', width=238.54):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=17.66, default_y=-176.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=72.48, default_y=-171.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=99.89, default_y=-181.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('i')
            with Note(default_x=127.3, default_y=-186.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=182.12, default_y=-191.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
        with Measure(number='7', width=201.72):
            with Note(default_x=19.35, default_y=-186.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=9.05, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='8', width=978.17):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.0)
            with Note(default_x=115.75, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('se')
            with Note(default_x=330.95, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lon')
            with Note(default_x=546.16, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
            with Note(default_x=761.36, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
        with Measure(number='9', width=378.66):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.0)
            with Note(default_x=111.58, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=170.58, default_y=-178.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=303.31, default_y=-178.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=340.18, default_y=-178.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
        with Measure(number='10', width=410.47):
            with Note(default_x=20.0, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=106.41, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni‿i')
            with Note(default_x=192.83, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=300.85, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
        with Measure(number='11', width=189.05):
            with Note(default_x=15.84, default_y=-173.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.39, default_y=-63.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('me!')
                    Extend()
            with Note(default_x=101.46, default_y=-178.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='12', width=418.51):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(108.03)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=97.78)
            with Note(default_x=118.36, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=174.98, default_y=-193.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mo')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=277.93, default_y=-198.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=334.55, default_y=-193.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('ti‿i')
                    Extend()
            with Note(default_x=375.73, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='13', width=288.88):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=10.12, default_y=-178.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gior')
            with Note(default_x=48.61, default_y=-183.03):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=87.11, default_y=-183.03):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
                    Extend()
            with Note(default_x=125.6, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=164.1, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mie')
            with Note(default_x=225.69, default_y=-193.03):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='14', width=270.78):
            with Note(default_x=16.64, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('i')
            with Note(default_x=78.24, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('dol')
            with Note(default_x=139.84, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.34, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,')
            with Note(default_x=207.58, default_y=-188.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='15', width=320.96):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(109.11)
            with Note(default_x=100.38, default_y=-194.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=125.3, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.22, default_y=-184.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
                    Extend()
            with Note(default_x=204.72, default_y=-179.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=229.65, default_y=-184.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
                    Extend()
            with Note(default_x=269.52, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=215.31):
            with Note(default_x=16.64, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('i')
            with Note(default_x=62.11, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('dol')
            with Note(default_x=108.13, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.34, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,')
            with Note(default_x=167.81, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='17', width=237.51):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=12.78, default_y=-179.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=38.42, default_y=-184.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=64.05, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no‿a')
            with Note(default_x=100.27, default_y=-194.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=136.49, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-83.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=204.39):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=146.48, default_y=-189.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='19', width=398.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.01)
            with Note(default_x=100.38, default_y=-182.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=165.31, default_y=-192.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=250.83, default_y=-187.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=289.02):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Note(default_x=206.65, default_y=-187.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='21', width=290.62):
            with Note(default_x=13.8, default_y=-182.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=74.84, default_y=-192.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=157.93, default_y=-187.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=363.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(125.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Sound(dynamics=83.33)
            with Note(default_x=122.68, default_y=-323.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Se')
            with Note(default_x=175.86, default_y=-338.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lon')
            with Note(default_x=209.1, default_y=-338.99):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=242.33, default_y=-333.99):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=272.16):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.27, default_y=-338.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben')
            with Note(default_x=87.77, default_y=-328.99):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio')
            with Note(default_x=122.92, default_y=-323.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
            with Note(default_x=158.07, default_y=-303.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se')
            with Note(default_x=214.31, default_y=-338.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
        with Measure(number='3', width=233.56):
            with Note(default_x=21.76, default_y=-323.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=74.31, default_y=-303.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=126.86, default_y=-288.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=179.41, default_y=-293.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ni,e')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='4', width=322.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(115.53)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=103.7, default_y=-292.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=158.04, default_y=-297.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni‿i')
            with Note(default_x=212.38, default_y=-302.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=266.72, default_y=-307.2):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='5', width=215.25):
            with Note(default_x=13.64, default_y=-312.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.77, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Note(default_x=84.84, default_y=-322.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=181.44, default_y=-322.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
        with Measure(number='6', width=238.54):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=17.66, default_y=-317.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=72.48, default_y=-302.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni‿i')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=127.3, default_y=-297.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=182.12, default_y=-332.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='7', width=201.72):
            with Note(default_x=19.35, default_y=-317.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        BreathMark(None)
                with Lyric(number='1', default_x=9.77, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=95.9, default_y=-307.2):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('se')
            with Note(default_x=162.56, default_y=-307.2):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-81.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lon')
        with Measure(number='8', width=978.17):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.0)
            with Note(default_x=115.38, default_y=-256.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
            with Note(default_x=545.8, default_y=-266.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('tu')
        with Measure(number='9', width=378.66):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(108.31)
            with Note(default_x=111.22, default_y=-276.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=229.57, default_y=-276.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('son')
            with Note(default_x=303.31, default_y=-276.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
        with Measure(number='10', width=410.47):
            with Note(default_x=20.0, default_y=-271.31):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter')
            with Note(default_x=149.62, default_y=-271.31):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni‿i')
            with Note(default_x=192.83, default_y=-281.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dì')
            with Note(default_x=354.86, default_y=-281.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('per')
        with Measure(number='11', width=189.05):
            with Note(default_x=12.88, default_y=-276.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Fermata(None, type='upright', default_y=4.6, relative_y=10.0)
                with Lyric(number='1', default_x=13.12, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('me!')
        with Measure(number='12', width=418.51):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(115.4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=97.78)
            with Note(default_x=118.36, default_y=-318.43):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=174.98, default_y=-333.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mo')
            with Note(default_x=226.45, default_y=-333.43):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=277.93, default_y=-328.43):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=334.55, default_y=-328.43):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ti')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='13', width=288.88):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=48.61, default_y=-333.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('i')
            with Note(default_x=87.11, default_y=-323.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gior')
            with Note(default_x=125.6, default_y=-318.43):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('ni')
            with Note(default_x=164.1, default_y=-298.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mie')
            with Note(default_x=225.69, default_y=-298.43):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('i')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='14', width=270.78):
            with Note(default_x=16.64, default_y=-318.43):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('i')
            with Note(default_x=47.44, default_y=-313.43):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.24, default_y=-308.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('dol')
                    Extend()
            with Note(default_x=109.04, default_y=-303.43):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=139.84, default_y=-303.43):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.39, default_y=-84.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,')
                    Extend()
            with Note(default_x=176.78, default_y=-308.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=207.58, default_y=-313.43):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-84.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=238.38, default_y=-318.43):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=320.96):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(111.01)
            with Note(default_x=100.38, default_y=-295.12):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=150.22, default_y=-330.12):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=229.65, default_y=-315.12):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-80.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='16', width=215.31):
            with Note(default_x=16.64, default_y=-315.12):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-80.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('i')
            with Note(default_x=39.38, default_y=-310.12):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=62.11, default_y=-305.12):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-80.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('dol')
                    Extend()
            with Note(default_x=85.4, default_y=-300.12):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.13, default_y=-300.12):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.39, default_y=-80.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,')
                    Extend()
            with Note(default_x=145.07, default_y=-305.12):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=167.81, default_y=-310.12):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-80.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
            with Note(default_x=190.54, default_y=-315.12):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=237.51):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=12.78, default_y=-295.12):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=64.05, default_y=-330.12):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no‿a')
            with Note(default_x=136.49, default_y=-315.12):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-80.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('te,')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=203.13, default_y=-330.12):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='18', width=204.39):
            with Note(default_x=12.78, default_y=-315.12):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=61.23, default_y=-305.12):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=106.17, default_y=-295.12):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-80.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
            with Note(default_x=171.67, default_y=-295.12):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-80.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='19', width=398.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.01)
            with Note(default_x=100.38, default_y=-324.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=205.89, default_y=-324.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=250.83, default_y=-309.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Sound(dynamics=40.0)
            with Note(default_x=356.35, default_y=-324.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='20', width=289.02):
            with Note(default_x=12.78, default_y=-309.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=77.4, default_y=-299.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=142.02, default_y=-289.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,')
            with Note(default_x=247.03, default_y=-289.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vi')
        with Measure(number='21', width=290.62):
            with Note(default_x=13.8, default_y=-324.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ci')
            with Note(default_x=112.99, default_y=-324.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('no‿a')
            with Note(default_x=157.93, default_y=-309.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-83.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('te.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=363.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(128.66)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-3)
                    Mode('major')
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
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-51.02, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=83.33)
            with Note(default_x=122.68, default_y=-507.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=175.86, default_y=-512.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=209.1, default_y=-507.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=242.33, default_y=-517.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=295.51, default_y=-512.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=328.74, default_y=-507.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.68, default_y=-517.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=175.86, default_y=-522.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=242.33, default_y=-527.65):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=295.51, default_y=-522.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=328.74, default_y=-517.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=122.68, default_y=-597.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.86, default_y=-612.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=209.1, default_y=-612.65):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=242.33, default_y=-607.65):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='2', width=272.16):
            with Note(default_x=10.12, default_y=-497.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.27, default_y=-502.65):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.77, default_y=-502.65):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=122.92, default_y=-507.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=158.07, default_y=-507.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=214.31, default_y=-512.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.12, default_y=-507.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=45.27, default_y=-512.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.77, default_y=-512.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=122.92, default_y=-517.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=158.07, default_y=-517.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=214.31, default_y=-522.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=45.27, default_y=-612.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=87.77, default_y=-602.65):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=122.92, default_y=-597.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=158.07, default_y=-577.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=214.31, default_y=-612.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=233.56):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=131.16, default_y=-517.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=179.41, default_y=-497.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=126.86, default_y=-507.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=179.41, default_y=-512.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.76, default_y=-597.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=74.31, default_y=-577.65):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=126.86, default_y=-562.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=179.41, default_y=-567.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='4', width=322.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(147.64)
                with StaffLayout(number=2):
                    StaffDistance(65.45)
            with Note(default_x=103.7, default_y=-494.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.04, default_y=-499.84):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=212.38, default_y=-504.84):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=266.72, default_y=-509.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=100.38, default_y=-529.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=103.7, default_y=-585.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.04, default_y=-590.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.38, default_y=-595.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=266.72, default_y=-600.29):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=215.25):
            with Note(default_x=13.64, default_y=-514.84):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=84.84, default_y=-514.84):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=149.24, default_y=-509.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=181.44, default_y=-504.84):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.64, default_y=-529.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=84.84, default_y=-524.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=149.24, default_y=-519.84):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=181.44, default_y=-514.84):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.64, default_y=-605.29):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=84.48, default_y=-615.29):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=238.54):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-88.53)
                Staff(1)
            with Note(default_x=17.66, default_y=-509.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.07, default_y=-494.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=72.48, default_y=-504.84):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=99.89, default_y=-514.84):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=127.3, default_y=-519.84):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=154.71, default_y=-509.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.12, default_y=-514.84):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.53, default_y=-524.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.66, default_y=-519.84):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=72.48, default_y=-514.84):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.89, default_y=-524.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=127.3, default_y=-529.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=154.71, default_y=-519.84):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.12, default_y=-524.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.53, default_y=-534.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.66, default_y=-610.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.48, default_y=-630.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.3, default_y=-625.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=182.12, default_y=-625.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=201.72):
            with Note(default_x=19.35, default_y=-529.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.35, default_y=-529.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=19.35, default_y=-610.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=95.54, default_y=-635.29):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='8', width=978.17):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(98.92)
                with StaffLayout(number=2):
                    StaffDistance(71.68)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=330.95, default_y=-434.92):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=546.16, default_y=-434.92):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=761.36, default_y=-434.92):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=330.95, default_y=-444.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=546.16, default_y=-444.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=761.36, default_y=-444.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(16.0)
            with Note(default_x=115.38, default_y=-541.6):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=545.8, default_y=-551.6):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=378.66):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(112.28)
                with StaffLayout(number=2):
                    StaffDistance(66.38)
            with Note(default_x=111.58, default_y=-463.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.58, default_y=-468.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=111.58, default_y=-473.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=170.58, default_y=-478.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=111.22, default_y=-569.98):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=229.57, default_y=-569.98):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=303.31, default_y=-569.98):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='10', width=410.47):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=106.41, default_y=-463.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    Words('rit.', default_y=23.62, relative_y=20.0, font_style='italic')
                Staff(1)
            with Note(default_x=192.83, default_y=-463.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=300.85, default_y=-463.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=106.41, default_y=-473.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=192.83, default_y=-473.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=300.85, default_y=-473.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(16.0)
            with Note(default_x=19.64, default_y=-564.98):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=192.47, default_y=-574.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=189.05):
            with Note(default_x=15.84, default_y=-463.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.46, default_y=-468.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', default_y=2.57, relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.84, default_y=-473.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=101.46, default_y=-478.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='inverted', default_y=-64.81, relative_y=-10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.88, default_y=-569.98):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='12', width=418.51):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(141.15)
                with StaffLayout(number=2):
                    StaffDistance(69.88)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-51.02, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=97.78)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', relative_y=20.0, font_style='italic')
                Staff(1)
            with Note(default_x=118.36, default_y=-514.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural', parentheses='yes')
                Stem('up')
                Staff(1)
            with Note(default_x=174.98, default_y=-519.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=200.72, default_y=-504.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.45, default_y=-509.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.19, default_y=-519.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=277.93, default_y=-524.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=334.55, default_y=-519.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=375.73, default_y=-514.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.36, default_y=-524.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=174.98, default_y=-529.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=277.93, default_y=-534.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=334.55, default_y=-529.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=375.73, default_y=-524.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=118.36, default_y=-609.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.98, default_y=-624.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=226.45, default_y=-624.46):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=277.93, default_y=-619.46):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='13', width=288.88):
            with Note(default_x=10.12, default_y=-504.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.61, default_y=-509.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.11, default_y=-509.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.6, default_y=-514.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.1, default_y=-514.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=225.69, default_y=-519.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.12, default_y=-514.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.61, default_y=-519.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.11, default_y=-519.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=125.6, default_y=-524.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.1, default_y=-524.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=225.69, default_y=-529.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=48.61, default_y=-624.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat', parentheses='yes')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=87.11, default_y=-614.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=125.6, default_y=-609.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.1, default_y=-589.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=225.69, default_y=-624.46):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='14', width=270.78):
            with Note(default_x=16.64, default_y=-514.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.44, default_y=-509.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.24, default_y=-504.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.04, default_y=-499.58):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.84, default_y=-499.58):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=176.78, default_y=-504.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=207.58, default_y=-509.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.38, default_y=-514.58):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.32, default_y=-524.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.64, default_y=-609.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.44, default_y=-604.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=78.24, default_y=-599.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.04, default_y=-594.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.84, default_y=-594.46):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=176.78, default_y=-599.46):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.58, default_y=-604.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.38, default_y=-609.46):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=320.96):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(136.43)
                with StaffLayout(number=2):
                    StaffDistance(65.87)
            with Note(default_x=100.38, default_y=-511.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.3, default_y=-506.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.22, default_y=-501.55):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.72, default_y=-496.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=229.65, default_y=-501.55):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=269.52, default_y=-506.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=100.38, default_y=-521.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=125.3, default_y=-516.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.22, default_y=-511.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.72, default_y=-506.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=229.65, default_y=-511.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=269.52, default_y=-516.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(14.0)
            with Note(default_x=100.38, default_y=-577.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.22, default_y=-612.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=229.65, default_y=-597.42):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='16', width=215.31):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=40.0)
            with Note(default_x=16.64, default_y=-506.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.38, default_y=-501.55):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.11, default_y=-496.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.4, default_y=-491.55):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=108.13, default_y=-491.55):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.07, default_y=-496.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.81, default_y=-501.55):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.54, default_y=-506.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.32, default_y=-516.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.64, default_y=-597.42):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.38, default_y=-592.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.11, default_y=-587.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.4, default_y=-582.42):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=108.13, default_y=-582.42):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.07, default_y=-587.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=167.81, default_y=-592.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.54, default_y=-597.42):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=237.51):
            with Note(default_x=12.78, default_y=-496.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.42, default_y=-501.55):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=64.05, default_y=-506.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.27, default_y=-511.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.49, default_y=-516.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.78, default_y=-506.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=38.42, default_y=-511.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=64.05, default_y=-516.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.27, default_y=-521.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.49, default_y=-516.55):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=12.78, default_y=-577.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.05, default_y=-612.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=136.49, default_y=-597.42):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='18', width=204.39):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
        with Measure(number='19', width=398.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(149.31)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=315.76, default_y=-618.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='20', width=289.02):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=40.0)
            with Note(default_x=206.65, default_y=-478.33):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=206.65, default_y=-488.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.78, default_y=-603.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.4, default_y=-593.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=141.66, default_y=-583.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=290.62):
            with Note(default_x=13.8, default_y=-473.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=74.84, default_y=-493.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=157.93, default_y=-488.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-493.33):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.84, default_y=-508.33):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=157.93, default_y=-513.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.44, default_y=-618.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.93, default_y=-603.33):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')