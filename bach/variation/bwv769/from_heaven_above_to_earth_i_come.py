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
            Millimeters(6.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1898.98)
            PageWidth(1342.71)
            with PageMargins(type='even'):
                LeftMargin(63.9386)
                RightMargin(63.9386)
                TopMargin(63.9386)
                BottomMargin(63.9386)
            with PageMargins(type='odd'):
                LeftMargin(63.9386)
                RightMargin(63.9386)
                TopMargin(63.9386)
                BottomMargin(63.9386)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Vom Himmel hoch da komm ich her', default_x=671.355, default_y=1835.04, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Hans Leo Haßler 1608', default_x=1278.77, default_y=1735.04, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Sopran')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Sopran')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(57.4803)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alt')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alt')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(59.0551)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(60.6299)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(28)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=139.51):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(76.32)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1. Alle', relative_y=40.0)
            with Note(default_x=80.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Vom')
        with Measure(number='2', width=265.92):
            with Note(default_x=31.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=89.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
            with Note(default_x=148.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=206.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='3', width=248.53):
            with Note(default_x=35.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm')
            with Note(default_x=84.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=133.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.83, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('her,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
        with Measure(number='4', width=269.59):
            with Note(default_x=28.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('bring')
            with Note(default_x=87.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
            with Note(default_x=150.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=209.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='5', width=214.97):
            with Note(default_x=21.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('neu')
            with Note(default_x=65.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=108.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mär,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='6', width=332.56):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(31.65)
                        RightMargin(-0.0)
                    SystemDistance(162.1)
            with Note(default_x=62.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=129.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=196.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mär')
            with Note(default_x=263.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('bring')
        with Measure(number='7', width=299.94):
            with Note(default_x=25.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=89.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=153.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.08, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('viel,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=258.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
        with Measure(number='8', width=296.66):
            with Note(default_x=21.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('von')
            with Note(default_x=89.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=158.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text("sing'n")
            with Note(default_x=226.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=254.03):
            with Note(default_x=21.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-50.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=54.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=86.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=139.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.76, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('will.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=139.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(67.6)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=80.83, default_y=-137.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('Vom')
        with Measure(number='2', width=265.92):
            with Note(default_x=31.81, default_y=-137.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=89.94, default_y=-142.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('end')
                    Text('mel')
            with Note(default_x=148.07, default_y=-152.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=206.2, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='3', width=248.53):
            with Note(default_x=35.19, default_y=-152.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('komm')
            with Note(default_x=84.56, default_y=-152.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=133.93, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.09, default_y=-60.46, relative_x=2.26, relative_y=-50.0):
                    Syllabic('single')
                    Text('her,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.15, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('ich')
        with Measure(number='4', width=269.59):
            with Note(default_x=28.65, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('bring')
            with Note(default_x=87.77, default_y=-152.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('euch')
            with Note(default_x=150.04, default_y=-157.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=209.01, default_y=-162.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='5', width=214.97):
            with Note(default_x=21.21, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('begin')
                    Text('neu')
            with Note(default_x=65.04, default_y=-152.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=108.87, default_y=-157.6):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=11.01, default_y=-60.46, relative_x=2.26, relative_y=-50.0):
                    Syllabic('single')
                    Text('Mär,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.09, default_y=-157.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.46, relative_y=-50.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='6', width=332.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.62)
            with Note(default_x=62.51, default_y=-181.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=129.62, default_y=-166.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=196.73, default_y=-176.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('single')
                    Text('Mär')
            with Note(default_x=263.84, default_y=-161.62):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('single')
                    Text('bring')
        with Measure(number='7', width=299.94):
            with Note(default_x=25.04, default_y=-171.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=89.35, default_y=-176.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=153.65, default_y=-186.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.34, default_y=-65.94, relative_x=2.26, relative_y=-50.0):
                    Syllabic('end')
                    Text('viel,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=258.15, default_y=-171.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('begin')
                    Text('da')
        with Measure(number='8', width=296.66):
            with Note(default_x=21.43, default_y=-171.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('end')
                    Text('von')
            with Note(default_x=89.84, default_y=-181.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=158.25, default_y=-181.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('single')
                    Text("sing'n")
            with Note(default_x=226.65, default_y=-181.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=254.03):
            with Note(default_x=21.21, default_y=-181.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=86.86, default_y=-186.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-65.94, relative_y=-50.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=139.38, default_y=-196.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.89, default_y=-65.94, relative_x=1.13, relative_y=-50.0):
                    Syllabic('single')
                    Text('will.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=139.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(108.57)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=80.83, default_y=-261.17):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Vom')
        with Measure(number='2', width=265.92):
            with Note(default_x=31.81, default_y=-261.17):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=89.94, default_y=-271.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
            with Note(default_x=148.07, default_y=-276.17):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
            with Note(default_x=206.2, default_y=-271.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='3', width=248.53):
            with Note(default_x=35.19, default_y=-281.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('konam')
            with Note(default_x=84.56, default_y=-286.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=133.93, default_y=-286.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.83, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('her,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.15, default_y=-286.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
        with Measure(number='4', width=269.59):
            with Note(default_x=28.65, default_y=-281.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('bring')
            with Note(default_x=87.77, default_y=-301.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
            with Note(default_x=150.04, default_y=-296.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=209.01, default_y=-286.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
        with Measure(number='5', width=214.97):
            with Note(default_x=21.21, default_y=-296.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('neu')
            with Note(default_x=65.04, default_y=-281.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=108.87, default_y=-281.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mär,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.09, default_y=-286.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='6', width=332.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(126.62)
            with Note(default_x=62.51, default_y=-323.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
            with Note(default_x=129.62, default_y=-308.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=196.73, default_y=-318.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mär')
            with Note(default_x=263.84, default_y=-328.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('bring')
        with Measure(number='7', width=299.94):
            with Note(default_x=25.04, default_y=-328.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=89.35, default_y=-333.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('so')
            with Note(default_x=153.65, default_y=-328.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.08, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('viel,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=258.15, default_y=-338.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
        with Measure(number='8', width=296.66):
            with Note(default_x=21.43, default_y=-328.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('von')
            with Note(default_x=89.84, default_y=-323.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=158.25, default_y=-338.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text("sing'n")
            with Note(default_x=226.65, default_y=-338.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=254.03):
            with Note(default_x=21.21, default_y=-323.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=54.03, default_y=-313.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=86.86, default_y=-328.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=139.38, default_y=-338.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.76, default_y=-46.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('will.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=139.51):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(75.35)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=80.83, default_y=-396.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-14.32, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.Vom')
                with Lyric(number='2', default_x=-15.68, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.Es')
                with Lyric(number='3', default_x=-16.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.Er')
                with Lyric(number='4', default_x=-25.38, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('15.Lob,')
        with Measure(number='2', width=265.92):
            with Note(default_x=31.81, default_y=-386.52):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('bringt')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ehr')
            with Note(default_x=89.94, default_y=-381.52):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=148.07, default_y=-376.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('hoch')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=206.2, default_y=-386.52):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                with Lyric(number='2', default_x=9.17, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Christ,')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='3', width=248.53):
            with Note(default_x=35.19, default_y=-381.52):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Se')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('höch')
            with Note(default_x=84.56, default_y=-376.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lig')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('sten')
            with Note(default_x=133.93, default_y=-396.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.83, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('her,')
                with Lyric(number='2', default_x=9.03, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott,')
                with Lyric(number='3', default_x=8.99, default_y=-95.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('keit,')
                with Lyric(number='4', default_x=8.85, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thron,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.15, default_y=-396.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='4', width=269.59):
            with Note(default_x=28.65, default_y=-406.52):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('bring')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('will')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=87.77, default_y=-401.52):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('schenkt')
            with Note(default_x=150.04, default_y=-396.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text("führ'n")
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
            with Note(default_x=209.01, default_y=-386.52):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
        with Measure(number='5', width=214.97):
            with Note(default_x=21.21, default_y=-396.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('neu')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
                with Lyric(number='4', default_x=8.54, default_y=-121.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text("ein'")
            with Note(default_x=65.04, default_y=-391.52):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=108.87, default_y=-406.52):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.76, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mär,')
                with Lyric(number='2', default_x=8.97, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Not,')
                with Lyric(number='3', default_x=8.81, default_y=-95.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('reit.')
                with Lyric(number='4', default_x=8.77, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sohn.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.09, default_y=-396.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-69.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                with Lyric(number='3', default_x=6.58, default_y=-95.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='4', default_x=6.58, default_y=-121.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('Des')
        with Measure(number='6', width=332.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.62)
            with Direction(placement='below'):
                with DirectionType():
                    Words(' S-2. Euch ist ein Kindlein heut geborn / von einer Jungfrau auserkorn, /\n', default_x=83.76, default_y=-190.05, valign='top', font_size='12')
                    Words("     ein Kindelein so zart und fein, / das soll eu'r Freud und Wonne sein.\n")
                    Words(' ATB-3. Es ist der Herr Christ, unser Gott, / der will euch führn aus aller Not, /\n')
                    Words("     er will eu'r Heiland selber sein, / von allen Sünden machen rein.\n")
                    Words(" Alle-4. Er bringt euch alle Seligkeit, / die Gott der Vater hat bereit', /\n")
                    Words('     daß ihr mit uns im Himmelreich / sollt leben nun und ewiglich.\n')
                    Words(' 5. So merket nun das Zeichen recht: / die Krippe, Windelein so schlecht, /\n')
                    Words('     da findet ihr das Kind gelegt, / das alle Welt erhält und trägt.\n')
                    Words(' SA-6. Des laßt uns alle fröhlich sein / und mit den Hirten gehn hinein, /\n')
                    Words('     zu sehn, was Gott uns hat beschert, / mit seinem lieben Sohn verehrt.\n')
                    Words("Alle-15. Lob, Ehr sei Gott im höchsten Thron, / der uns schenkt seinen ein'gen Sohn. /\n")
                    Words('     Des freuet sich der Engel Schar / und singet uns solch neues Jahr.')
            with Note(default_x=62.51, default_y=-437.87):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gu')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('will')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('freu')
            with Note(default_x=129.62, default_y=-447.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('single')
                    Text("eu'r")
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('et')
            with Note(default_x=196.73, default_y=-432.87):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mär')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hei')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('sich')
            with Note(default_x=263.84, default_y=-442.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('bring')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('land')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
        with Measure(number='7', width=299.94):
            with Note(default_x=25.04, default_y=-452.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sel')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=89.35, default_y=-447.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('ber')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mel')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('gel')
            with Note(default_x=153.65, default_y=-467.87):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.08, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('viel,')
                with Lyric(number='2', default_x=9.23, default_y=-71.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein,')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('reich')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schar')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=258.15, default_y=-462.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('sollt')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='8', width=296.66):
            with Note(default_x=21.43, default_y=-442.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('von')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('le')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sin')
            with Note(default_x=89.84, default_y=-437.87):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('len')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('get')
            with Note(default_x=158.25, default_y=-452.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text("sing'n")
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sün')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('nun')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=226.65, default_y=-452.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('solch')
        with Measure(number='9', width=254.03):
            with Note(default_x=21.21, default_y=-472.87):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('sa')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('neu')
            with Note(default_x=86.86, default_y=-467.87):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-71.41, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
                with Lyric(number='3', default_x=6.58, default_y=-97.38, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wig')
                with Lyric(number='4', default_x=6.58, default_y=-123.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
            with Note(default_x=139.38, default_y=-452.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=8.76, default_y=-45.43, relative_y=-30.0):
                    Syllabic('single')
                    Text('will.')
                with Lyric(number='2', default_x=8.79, default_y=-71.41, relative_y=-30.0):
                    Syllabic('single')
                    Text('rein.')
                with Lyric(number='3', default_x=8.75, default_y=-97.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich.')
                with Lyric(number='4', default_x=8.51, default_y=-123.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('Jahr.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')