with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Kantate')
    with Identification():
        Creator('Johann Sebastian Bach (1685-1750)', type='composer')
        Creator('BWV 211', type='lyricist')
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
        CreditWords('Kantate', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_weight='bold', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords("'Schweight stille, plaudert nicht' \n", default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
        CreditWords('(\n')
        CreditWords("'Kaffeekantate'\n", font_style='italic')
        CreditWords(')\n', font_style='normal')
        CreditWords(None)
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685-1750)', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('BWV 211', default_x=56.6929, default_y=1526.67, justify='left', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Tenore')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Violoncello')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Violoncello')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Cembalo')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Harpsichord')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(5)
                MidiProgram(7)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=492.45):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(140.2)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('RECITATIV.', default_x=-46.8, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=71.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.16, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=219.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schweight')
            with Note(default_x=279.95, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stil')
            with Note(default_x=325.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.4, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('le,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=415.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('plau')
            with Note(default_x=457.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('dert')
        with Measure(number='2', width=444.84):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Largo', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=50.0)
            with Note(default_x=25.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.42, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=102.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=132.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hö')
            with Note(default_x=179.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.53, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=274.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=309.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('jetz')
            with Note(default_x=348.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('und')
            with Note(default_x=395.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-45.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='3', width=584.72):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(96.49)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=50.0)
            with Note(default_x=84.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.4, default_y=-50.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('schicht:')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=276.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Da')
            with Note(default_x=353.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('kömmt')
            with Note(default_x=410.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr')
            with Note(default_x=468.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schlen')
            with Note(default_x=525.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('dri')
        with Measure(number='4', width=471.77):
            with Note(default_x=13.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('an')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=104.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit')
            with Note(default_x=153.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
            with Note(default_x=205.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('ner')
            with Note(default_x=258.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Toch')
            with Note(default_x=311.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
            with Note(default_x=364.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lies')
            with Note(default_x=417.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
        with Measure(number='5', width=564.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(96.49)
            with Note(default_x=80.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.77, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('her;')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
            with Note(default_x=177.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
            with Note(default_x=228.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('brummt')
            with Note(default_x=283.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja')
            with Note(default_x=339.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('wie')
            with Note(default_x=395.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ein')
            with Note(default_x=451.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Zie')
            with Note(default_x=507.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('del')
        with Measure(number='6', width=491.85):
            with Note(default_x=19.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.0, default_y=-50.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('Bär;')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=315.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('hört')
            with Note(default_x=368.04, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sel')
            with Note(default_x=420.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.34, default_y=-50.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('ber.')
        with Measure(number='7', width=713.21):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=153.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=202.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
            with Note(default_x=252.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihm')
            with Note(default_x=320.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.32, default_y=-50.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Note(default_x=389.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=9.17, default_y=-50.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('than!')
            with Note(default_x=457.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='8', width=343.28):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=492.45):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(66.25)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=112.39, default_y=-111.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=370.27, default_y=-111.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
        with Measure(number='2', width=444.84):
            with Note(default_x=25.58, default_y=-111.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=226.92, default_y=-116.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=584.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.8)
            with Note(default_x=84.6, default_y=-117.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Words('con pompa', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='11')
            with Note(default_x=142.01, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=192.93, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=219.03, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=276.44, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=327.36, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=353.46, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=471.77):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=66.54, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.01, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=153.03, default_y=-152.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=564.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.25)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=136.41, default_y=-171.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=202.37, default_y=-171.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=228.17, default_y=-171.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=491.85):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=71.4, default_y=-166.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.69, default_y=-166.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=141.42, default_y=-166.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=193.62, default_y=-166.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=239.91, default_y=-166.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=263.64, default_y=-166.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=420.24, default_y=-151.25):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=466.53, default_y=-151.25):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='7', width=713.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.8)
            with Note(default_x=84.6, default_y=-155.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=252.53, default_y=-165.8):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=389.36, default_y=-150.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=457.78, default_y=-150.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=518.45, default_y=-150.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=551.42, default_y=-150.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=619.84, default_y=-150.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=680.51, default_y=-150.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='8', width=343.28):
            with Note(default_x=19.76, default_y=-170.8):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(32.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=492.45):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(1)
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
            with Note(default_x=112.39, default_y=-266.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-9.76, default_y=-24.6)
            with Note(default_x=112.39, default_y=-256.25):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-9.76, default_y=-24.6)
            with Note(default_x=112.39, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-9.76, default_y=-24.6)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=370.27, default_y=-266.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=370.27, default_y=-256.25):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=370.27, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=112.39, default_y=-321.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=370.27, default_y=-321.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='2', width=444.84):
            with Note(default_x=25.58, default_y=-261.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=25.58, default_y=-251.25):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=25.58, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=226.92, default_y=-256.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=226.92, default_y=-246.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=226.92, default_y=-236.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=226.92, default_y=-226.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=25.58, default_y=-321.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=226.92, default_y=-336.25):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='3', width=584.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=84.6, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=84.6, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=84.6, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('con pompa', default_y=-46.6, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=142.01, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=142.01, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=142.01, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=192.93, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=192.93, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=192.93, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=219.03, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=219.03, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=219.03, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=276.44, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=276.44, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=276.44, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=327.36, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=327.36, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=327.36, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=353.46, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=353.46, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=353.46, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=84.6, default_y=-327.8):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=142.01, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=192.93, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=219.03, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=276.44, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=327.36, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=353.46, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='4', width=471.77):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=66.54, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=66.54, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=66.54, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=129.01, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=129.01, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=129.01, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=153.03, default_y=-272.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.03, default_y=-262.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=153.03, default_y=-247.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=66.54, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.01, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=153.03, default_y=-362.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='5', width=564.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=136.41, default_y=-266.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.41, default_y=-256.25):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=136.41, default_y=-246.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=202.37, default_y=-266.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=202.37, default_y=-256.25):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=202.37, default_y=-246.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=228.17, default_y=-266.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=228.17, default_y=-256.25):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=228.17, default_y=-246.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=136.41, default_y=-381.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=202.37, default_y=-381.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=228.17, default_y=-381.25):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='6', width=491.85):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=71.4, default_y=-261.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.4, default_y=-251.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=71.4, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=117.69, default_y=-261.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=117.69, default_y=-251.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=117.69, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=141.42, default_y=-261.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.42, default_y=-251.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=141.42, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=193.62, default_y=-261.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=193.62, default_y=-251.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=193.62, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=239.91, default_y=-261.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=239.91, default_y=-251.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=239.91, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=263.64, default_y=-261.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=263.64, default_y=-251.25):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=263.64, default_y=-241.25):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=420.24, default_y=-271.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=420.24, default_y=-261.25):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=420.24, default_y=-246.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=466.53, default_y=-271.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=466.53, default_y=-261.25):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=466.53, default_y=-246.25):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=71.4, default_y=-376.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.69, default_y=-376.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=141.42, default_y=-376.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=193.62, default_y=-376.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=239.91, default_y=-376.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=263.64, default_y=-376.25):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=420.24, default_y=-361.25):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=466.53, default_y=-361.25):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='7', width=713.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=84.6, default_y=-275.8):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=84.6, default_y=-265.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=84.6, default_y=-250.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=252.53, default_y=-260.8):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=252.53, default_y=-250.8):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=252.53, default_y=-240.8):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=252.53, default_y=-230.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=389.36, default_y=-265.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=389.36, default_y=-255.8):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=389.36, default_y=-245.8):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=457.78, default_y=-265.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=457.78, default_y=-255.8):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=457.78, default_y=-245.8):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=518.45, default_y=-265.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=518.45, default_y=-255.8):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=518.45, default_y=-245.8):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=551.42, default_y=-270.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=551.42, default_y=-260.8):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=551.42, default_y=-245.8):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=619.84, default_y=-270.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=619.84, default_y=-260.8):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=619.84, default_y=-245.8):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=680.51, default_y=-270.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=680.51, default_y=-260.8):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=680.51, default_y=-245.8):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=84.6, default_y=-365.8):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=252.53, default_y=-375.8):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=389.36, default_y=-360.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=457.78, default_y=-360.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=518.45, default_y=-360.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=551.42, default_y=-360.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=619.84, default_y=-360.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=680.51, default_y=-360.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='8', width=343.28):
            with Note(default_x=19.76, default_y=-265.8):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                    Arpeggiate(default_x=-15.28, default_y=-4.6)
            with Note(default_x=19.76, default_y=-255.8):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-15.28, default_y=-4.6)
            with Note(default_x=19.76, default_y=-245.8):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-15.28, default_y=-4.6)
            with Note(default_x=19.76, default_y=-230.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(32.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-15.28, default_y=-4.6)
            with Backup():
                Duration(32.0)
            with Note(default_x=19.76, default_y=-380.8):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(32.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')