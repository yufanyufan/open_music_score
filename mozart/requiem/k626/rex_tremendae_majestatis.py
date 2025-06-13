with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Rex tremendae majestatis')
    with Identification():
        Creator('Wolfgang Amadeus Mozart', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(5.9944)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2033.9)
            PageWidth(1440.68)
            with PageMargins(type='even'):
                LeftMargin(66.1017)
                RightMargin(66.1017)
                TopMargin(66.1017)
                BottomMargin(133.898)
            with PageMargins(type='odd'):
                LeftMargin(66.1017)
                RightMargin(66.1017)
                TopMargin(66.1017)
                BottomMargin(133.898)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Rex tremendae majestatis', default_x=720.339, default_y=1967.8, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('From "Requiem in D Minor"', default_x=720.339, default_y=1901.07, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Wolfgang Amadeus Mozart', default_x=1374.58, default_y=1816.79, justify='right', valign='bottom', font_size='12')
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
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
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
                Volume(89.7638)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P5'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(1)
                Volume(48.8189)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=480.84):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(225.34)
                        RightMargin(0.0)
                    TopSystemDistance(202.41)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Grave', default_x=-37.31, relative_x=-25.1, relative_y=34.45, font_weight='bold', font_size='12')
                Sound(tempo=45.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='2', width=224.16):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='3', width=378.14):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=5.35, relative_x=0.52, relative_y=15.72):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=83.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.44, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='4', width=498.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    SystemDistance(92.61)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=171.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=410.93):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=90.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=325.87):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-0.87, relative_y=15.72):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=74.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=125.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=162.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=213.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=244.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=295.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='7', width=691.12):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=100.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=179.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-47.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
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
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-3.13, relative_y=21.27):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=535.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=643.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
        with Measure(number='8', width=544.68):
            with Note(default_x=20.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=280.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=370.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=409.97, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=500.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='9', width=603.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=89.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=343.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=432.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-51.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=470.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=559.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
        with Measure(number='10', width=632.42):
            with Note(default_x=20.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=317.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=440.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=484.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=585.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='11', width=578.54):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=88.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=144.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    with Articulations():
                        BreathMark(None)
                with Lyric(number='1', default_x=8.8, default_y=-51.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=200.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=265.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=305.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=370.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=410.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=526.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='12', width=657.26):
            with Note(default_x=17.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=90.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-51.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=335.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=565.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
        with Measure(number='13', width=649.86):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=92.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.56, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=153.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.56, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
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
            with Note(default_x=512.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.56, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=605.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.56, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
        with Measure(number='14', width=585.94):
            with Note(default_x=19.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.56, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=83.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-41.56, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=298.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.56, relative_y=-30.0):
                    Syllabic('begin')
                    Text('rex')
            with Note(default_x=395.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.56, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tre')
            with Note(default_x=439.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.56, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
        with Measure(number='15', width=676.31):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=97.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=192.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-55.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae,')
            with Note(default_x=233.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=331.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=385.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=498.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=539.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=631.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='16', width=559.49):
            with Note(default_x=17.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=97.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-55.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=1.9, relative_y=22.66):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=222.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note(default_x=263.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=296.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=358.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=483.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=525.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
        with Measure(number='17', width=666.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=92.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=177.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='18', width=569.24):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=0.35, relative_x=-5.03, relative_y=15.72):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=16.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=78.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=117.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.53, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('me!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='19', width=498.53):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.68)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='20', width=283.0):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Sound(tempo=40.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=5.46, relative_x=-18.8, relative_y=15.61):
                        Pp()
                Sound(dynamics=44.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=27.35)
            with Note(default_x=22.27, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=3.81, default_y=-41.8, relative_x=-2.77, relative_y=-37.23):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=116.26, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=147.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.06, default_y=-41.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=1.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('35')
                Sound(tempo=35.0)
            with Note(default_x=187.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('fons')
            with Note(default_x=218.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi')
            with Note(default_x=250.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='21', width=249.77):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('30')
                Sound(tempo=30.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-9.9, relative_y=14.22):
                        Pp()
                Sound(dynamics=17.78)
            with Note(default_x=26.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-41.8, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ta')
            with Note(default_x=81.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=192.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=204.5):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.27, default_y=-41.8, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis!')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=480.84):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='2', width=224.16):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='3', width=378.14):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=3.29, relative_y=11.56):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=83.18, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.44, default_y=-47.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='4', width=498.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.34)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=171.02, default_y=-157.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.34, default_y=-52.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('res!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=410.93):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=90.38, default_y=-162.34):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.48, default_y=-52.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=325.87):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=12.52, relative_x=2.42, relative_y=8.78):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=74.64, default_y=-162.34):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=125.55, default_y=-162.34):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=162.65, default_y=-157.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=213.56, default_y=-157.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=244.31, default_y=-157.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=295.21, default_y=-157.34):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='7', width=691.12):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=100.82, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=179.13, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-51.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.88, relative_x=10.74, relative_y=10.17):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=246.62, default_y=-180.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=354.5, default_y=-180.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=399.88, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
        with Measure(number='8', width=544.68):
            with Note(default_x=20.72, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=110.86, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=150.47, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=240.61, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
            with Note(default_x=279.86, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
        with Measure(number='9', width=603.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=89.72, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=177.99, default_y=-170.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-52.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=216.79, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=305.07, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=343.5, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-52.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
        with Measure(number='10', width=632.42):
            with Note(default_x=20.72, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=120.7, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=164.64, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=265.92, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
            with Note(default_x=317.78, default_y=-170.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-52.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=550.53, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=607.66, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='11', width=578.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=88.78, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=200.34, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=265.02, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=305.59, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=370.27, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=410.84, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=526.23, default_y=-175.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='12', width=657.26):
            with Note(default_x=17.19, default_y=-170.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=90.87, default_y=-170.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='13', width=649.86):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-180.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=294.48, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=377.37, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.14, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=438.77, default_y=-185.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=585.94):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=160.36, default_y=-185.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=254.89, default_y=-170.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
            with Note(default_x=298.93, default_y=-170.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=362.72, default_y=-190.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-56.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='15', width=676.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=97.58, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=299.25, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=385.54, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=498.81, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=539.27, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=631.32, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='16', width=559.49):
            with Note(default_x=17.19, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=97.17, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-49.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=3.81, relative_y=28.21):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=222.07, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note(default_x=263.36, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=296.46, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=358.91, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=483.81, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=525.1, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.3, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
        with Measure(number='17', width=666.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=177.05, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='18', width=569.24):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-4.52, relative_y=18.5):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=16.72, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=78.84, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=117.8, default_y=-170.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.53, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('me!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='19', width=498.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='20', width=283.0):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-6.31, relative_y=-4.76):
                        Pp()
                Sound(dynamics=44.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=19.33)
            with Note(default_x=22.27, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=116.26, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=147.59, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.06, default_y=-51.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Note(default_x=187.41, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('fons')
            with Note(default_x=218.74, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi')
            with Note(default_x=250.07, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='21', width=249.77):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=0.55, relative_x=9.52, relative_y=10.49):
                        Pp()
                Sound(dynamics=17.78)
            with Note(default_x=26.03, default_y=-155.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ta')
            with Note(default_x=81.2, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='22', width=204.5):
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.27, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis!')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=480.84):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(96.99)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='2', width=224.16):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='3', width=378.14):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=0.52, relative_y=15.72):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=83.18, default_y=-281.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.44, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='4', width=498.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(111.61)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=171.02, default_y=-283.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-41.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=410.93):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=90.38, default_y=-283.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-41.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=325.87):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=9.85, relative_x=-3.64, relative_y=15.72):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=74.64, default_y=-288.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=125.55, default_y=-288.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=162.65, default_y=-283.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=213.56, default_y=-283.95):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=244.31, default_y=-298.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=295.21, default_y=-298.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('je')
        with Measure(number='7', width=691.12):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=100.82, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sta')
            with Note(default_x=179.13, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-46.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-2.26, relative_y=11.56):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=400.24, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=606.89, default_y=-265.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
        with Measure(number='8', width=544.68):
            with Note(default_x=20.72, default_y=-265.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=79.17, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
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
            with Note(default_x=409.97, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=500.1, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
        with Measure(number='9', width=603.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=89.72, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=146.96, default_y=-290.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
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
            with Note(default_x=470.94, default_y=-290.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note(default_x=559.21, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
        with Measure(number='10', width=632.42):
            with Note(default_x=20.72, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=85.55, default_y=-295.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=317.78, default_y=-295.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=440.47, default_y=-295.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
            with Note(default_x=484.41, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
        with Measure(number='11', width=578.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=88.78, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=144.56, default_y=-290.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=200.34, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=265.02, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=305.59, default_y=-290.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=370.27, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=410.84, default_y=-300.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=526.23, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='12', width=657.26):
            with Note(default_x=17.19, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=90.87, default_y=-295.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=164.55, default_y=-295.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=285.28, default_y=-295.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=334.86, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
        with Measure(number='13', width=649.86):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=185.26, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=228.07, default_y=-265.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=325.75, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
            with Note(default_x=377.01, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
        with Measure(number='14', width=585.94):
            with Note(default_x=19.31, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.33, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-46.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=160.36, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('res')
            with Note(default_x=254.89, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=298.57, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
        with Measure(number='15', width=676.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=97.58, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=192.67, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-50.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae,')
            with Note(default_x=233.12, default_y=-265.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=331.62, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=385.54, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=498.81, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=539.27, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=631.32, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='16', width=559.49):
            with Note(default_x=17.19, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=97.17, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-50.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=4.68, relative_y=25.43):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=222.07, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note(default_x=263.36, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=296.46, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=358.91, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=483.81, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=525.1, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.36, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
        with Measure(number='17', width=666.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=177.05, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='18', width=569.24):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='19', width=498.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-6.42, relative_y=21.27):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.58, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=137.22, default_y=-285.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=165.22, default_y=-290.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.53, default_y=-47.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('me!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='20', width=283.0):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=4.3, relative_x=-14.64, relative_y=6.77):
                        Pp()
                Sound(dynamics=44.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=30.43)
            with Note(default_x=22.27, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=116.26, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=147.59, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.06, default_y=-47.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Note(default_x=187.41, default_y=-280.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('fons')
            with Note(default_x=218.74, default_y=-265.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi')
            with Note(default_x=250.07, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='21', width=249.77):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=13.68, relative_y=27.58):
                        Pp()
                Sound(dynamics=17.78)
            with Note(default_x=26.03, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_y=-47.44, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ta')
            with Note(default_x=81.57, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=136.74, default_y=-275.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='22', width=204.5):
            with Note(default_x=15.8, default_y=-270.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.27, default_y=-47.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis!')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=480.84):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='2', width=224.16):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='3', width=378.14):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=0.52, relative_y=15.72):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=83.18, default_y=-411.99):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.44, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='4', width=498.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.94)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=171.02, default_y=-416.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='5', width=410.93):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=90.38, default_y=-426.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=325.87):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=0.52, relative_y=32.37):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=74.64, default_y=-421.88):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=125.55, default_y=-421.88):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=162.65, default_y=-431.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('me')
            with Note(default_x=213.56, default_y=-431.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=244.31, default_y=-441.88):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=295.21, default_y=-441.88):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='7', width=691.12):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=100.82, default_y=-390.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=179.13, default_y=-425.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='8', width=544.68):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=0.52, relative_y=12.95):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=20.72, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=208.92, default_y=-395.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=280.22, default_y=-395.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('van')
            with Note(default_x=338.67, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('dos')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=603.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=216.79, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=305.07, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
            with Note(default_x=343.86, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=401.1, default_y=-420.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=632.42):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=164.64, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=265.92, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
            with Note(default_x=317.78, default_y=-425.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=550.53, default_y=-420.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=607.66, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='11', width=578.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=88.78, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-49.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=200.34, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=265.02, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=305.59, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=370.27, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=410.84, default_y=-420.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=526.23, default_y=-430.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='12', width=657.26):
            with Note(default_x=17.19, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=90.87, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-49.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
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
            with Note(default_x=482.59, default_y=-425.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=5.2, relative_x=-1.39, relative_y=14.33):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=605.72, default_y=-425.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
        with Measure(number='13', width=649.86):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=92.22, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=377.37, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=470.05, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=512.86, default_y=-395.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=605.54, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='14', width=585.94):
            with Note(default_x=18.95, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=298.93, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=395.95, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-41.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note(default_x=439.99, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=540.41, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
        with Measure(number='15', width=676.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=97.58, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=192.67, default_y=-400.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-53.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae,')
            with Note(default_x=233.12, default_y=-420.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('rex')
            with Note(default_x=331.62, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-53.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre')
            with Note(default_x=405.77, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=425.99, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('middle')
                    Text('men')
            with Note(default_x=498.81, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('dae')
            with Note(default_x=539.27, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma')
            with Note(default_x=631.32, default_y=-425.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('middle')
                    Text('je')
        with Measure(number='16', width=559.49):
            with Note(default_x=17.19, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=97.17, default_y=-440.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.8, default_y=-53.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-3.64, relative_y=24.04):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=222.07, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui')
            with Note(default_x=263.36, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=296.46, default_y=-390.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('middle')
                    Text('van')
            with Note(default_x=358.91, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('dos')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=483.81, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=525.1, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.68, relative_y=-30.0):
                    Syllabic('end')
                    Text('vas')
        with Measure(number='17', width=666.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-390.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gra')
            with Note(default_x=177.05, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='18', width=569.24):
            with Note():
                Rest(measure='yes')
                Duration(32.0)
                Voice('1')
        with Measure(number='19', width=498.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-2.26, relative_y=14.33):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.58, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=137.22, default_y=-420.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=165.22, default_y=-425.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.53, default_y=-47.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('me!')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
        with Measure(number='20', width=283.0):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=8.02, relative_x=-3.54, relative_y=3.04):
                        Pp()
                Sound(dynamics=44.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=26.27)
            with Note(default_x=22.27, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=116.26, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('va')
            with Note(default_x=147.59, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.06, default_y=-47.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('me,')
            with Note(default_x=187.41, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('fons')
            with Note(default_x=218.74, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi')
            with Note(default_x=250.07, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.44, relative_y=-30.0):
                    Syllabic('middle')
                    Text('e')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='21', width=249.77):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=15.07, relative_y=21.08):
                        Pp()
                Sound(dynamics=17.78)
            with Note(default_x=26.03, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-47.44, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ta')
            with Note(default_x=81.57, default_y=-415.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.33, default_y=-410.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=136.74, default_y=-405.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='22', width=204.5):
            with Note(default_x=15.8, default_y=-425.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.27, default_y=-47.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('tis!')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=480.84):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(100.0)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-2)
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
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=111.08, default_y=-576.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.08, default_y=-566.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=111.08, default_y=-556.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=111.08, default_y=-541.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.33, default_y=-611.99):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=146.33, default_y=-576.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=181.57, default_y=-591.99):
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
            with Note(default_x=181.57, default_y=-576.99):
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
            with Note(default_x=181.57, default_y=-566.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=212.82, default_y=-576.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=212.82, default_y=-541.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=228.84, default_y=-581.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.84, default_y=-546.99):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=260.1, default_y=-586.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=260.1, default_y=-551.99):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=276.11, default_y=-591.99):
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
            with Note(default_x=276.11, default_y=-556.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=307.37, default_y=-561.99):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=326.83, default_y=-566.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.09, default_y=-571.99):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=374.11, default_y=-576.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=405.36, default_y=-581.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=424.82, default_y=-586.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=456.08, default_y=-591.99):
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
            with Backup():
                Duration(32.0)
            with Note(default_x=111.08, default_y=-721.99):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=111.08, default_y=-686.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=146.33, default_y=-756.99):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=146.33, default_y=-721.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=181.57, default_y=-721.99):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.57, default_y=-686.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=-93.58)
                Staff(2)
            with Note(default_x=212.82, default_y=-686.99):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=228.84, default_y=-691.99):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.1, default_y=-696.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=276.11, default_y=-701.99):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=307.37, default_y=-706.99):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=307.37, default_y=-671.99):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=326.83, default_y=-711.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.83, default_y=-676.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=358.09, default_y=-716.99):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=358.09, default_y=-681.99):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=374.11, default_y=-721.99):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=374.11, default_y=-686.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=405.36, default_y=-726.99):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=405.36, default_y=-691.99):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=424.82, default_y=-731.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.82, default_y=-696.99):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=456.08, default_y=-736.99):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=456.08, default_y=-701.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=224.16):
            with Note(default_x=15.8, default_y=-596.99):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=41.64, default_y=-561.99):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=41.64, default_y=-551.99):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=41.64, default_y=-541.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=41.64, default_y=-526.99):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=93.33, default_y=-561.99):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.33, default_y=-551.99):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.33, default_y=-536.99):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=145.02, default_y=-566.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=145.02, default_y=-556.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=145.02, default_y=-541.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=196.71, default_y=-571.99):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=196.71, default_y=-556.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=196.71, default_y=-546.99):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-741.99):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-706.99):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=67.49, default_y=-706.99):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=67.49, default_y=-671.99):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=119.18, default_y=-701.99):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=119.18, default_y=-666.99):
                Chord()
                with Pitch():
                    Step('D')
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
            with Note(default_x=170.87, default_y=-736.99):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=170.87, default_y=-701.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='3', width=378.14):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=12.94, default_y=-576.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.94, default_y=-566.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-556.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=12.94, default_y=-541.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=48.06, default_y=-611.99):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.06, default_y=-576.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=83.18, default_y=-591.99):
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
            with Note(default_x=83.18, default_y=-576.99):
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
            with Note(default_x=83.18, default_y=-566.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=114.32, default_y=-576.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=114.32, default_y=-541.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=130.29, default_y=-581.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.29, default_y=-546.99):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=161.43, default_y=-586.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=161.43, default_y=-551.99):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=177.4, default_y=-591.99):
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
            with Note(default_x=177.4, default_y=-556.99):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=208.54, default_y=-561.99):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=228.01, default_y=-566.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.15, default_y=-571.99):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=275.12, default_y=-576.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=306.26, default_y=-566.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=322.23, default_y=-581.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.37, default_y=-566.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.52)
                Staff(2)
            with Note(default_x=12.94, default_y=-721.99):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=12.94, default_y=-686.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=48.06, default_y=-756.99):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.06, default_y=-721.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=83.18, default_y=-721.99):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.18, default_y=-686.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=-101.91)
                Staff(2)
            with Note(default_x=114.32, default_y=-686.99):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=130.29, default_y=-691.99):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.43, default_y=-696.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=177.4, default_y=-701.99):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.54, default_y=-706.99):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=208.54, default_y=-671.99):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=228.01, default_y=-711.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.01, default_y=-676.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=259.15, default_y=-716.99):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=259.15, default_y=-681.99):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=275.12, default_y=-721.99):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=275.12, default_y=-686.99):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=306.26, default_y=-711.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=306.26, default_y=-676.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=322.23, default_y=-726.99):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=322.23, default_y=-691.99):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=353.37, default_y=-711.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=353.37, default_y=-676.99):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(2)
        with Measure(number='4', width=498.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-611.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=131.8, default_y=-576.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=171.02, default_y=-626.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.02, default_y=-611.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=171.02, default_y=-601.88):
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
            with Note(default_x=171.02, default_y=-591.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=205.8, default_y=-611.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=205.8, default_y=-576.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=223.62, default_y=-616.88):
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
                Beam('continue', number=2)
            with Note(default_x=223.62, default_y=-581.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=258.4, default_y=-586.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=277.87, default_y=-591.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=314.77, default_y=-596.88):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=332.59, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=367.37, default_y=-606.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=386.84, default_y=-611.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=421.62, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=439.45, default_y=-616.88):
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
                Beam('continue', number=2)
            with Note(default_x=474.23, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-109.13)
                Staff(2)
            with Note(default_x=92.58, default_y=-756.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=92.58, default_y=-721.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=131.8, default_y=-721.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=131.8, default_y=-686.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=171.02, default_y=-756.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.02, default_y=-721.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=30.0)
                Staff(2)
            with Note(default_x=205.8, default_y=-721.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=223.62, default_y=-726.88):
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
                Beam('continue', number=2)
            with Note(default_x=258.4, default_y=-731.88):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=258.4, default_y=-696.88):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=277.87, default_y=-736.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=277.87, default_y=-701.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=314.77, default_y=-741.88):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=314.77, default_y=-706.88):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=332.59, default_y=-746.88):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.59, default_y=-711.88):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=367.37, default_y=-751.88):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=367.37, default_y=-716.88):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=386.84, default_y=-756.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=386.84, default_y=-721.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=421.62, default_y=-746.88):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=421.62, default_y=-711.88):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=439.45, default_y=-761.88):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=439.45, default_y=-726.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=474.23, default_y=-746.88):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=474.23, default_y=-711.88):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(2)
        with Measure(number='5', width=410.93):
            with Note(default_x=15.8, default_y=-621.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=53.09, default_y=-586.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=90.38, default_y=-611.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.38, default_y=-601.88):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=90.38, default_y=-586.88):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=90.38, default_y=-576.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=123.45, default_y=-576.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=140.4, default_y=-576.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.4, default_y=-541.88):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=173.46, default_y=-581.88):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=173.46, default_y=-546.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=196.73, default_y=-586.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=196.73, default_y=-551.88):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=229.8, default_y=-586.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=246.75, default_y=-586.88):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.75, default_y=-551.88):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=279.82, default_y=-591.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=279.82, default_y=-556.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=303.08, default_y=-596.88):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=303.08, default_y=-561.88):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=336.15, default_y=-596.88):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=353.1, default_y=-596.88):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.1, default_y=-561.88):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=386.17, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=386.17, default_y=-566.88):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-766.88):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-731.88):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=53.09, default_y=-731.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=53.09, default_y=-696.88):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=90.38, default_y=-766.88):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.38, default_y=-731.88):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=123.45, default_y=-766.88):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=140.4, default_y=-731.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.46, default_y=-726.88):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=196.73, default_y=-721.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=229.8, default_y=-756.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=246.75, default_y=-721.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=279.82, default_y=-726.88):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=303.08, default_y=-731.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=336.15, default_y=-766.88):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=353.1, default_y=-731.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.17, default_y=-721.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='6', width=325.87):
            with Note(default_x=17.23, default_y=-606.88):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=17.23, default_y=-571.88):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=74.64, default_y=-606.88):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=74.64, default_y=-596.88):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=74.64, default_y=-581.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=125.55, default_y=-606.88):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=125.55, default_y=-596.88):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=125.55, default_y=-581.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=162.65, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=162.65, default_y=-591.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=162.65, default_y=-581.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=213.56, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=213.56, default_y=-591.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=213.56, default_y=-581.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=244.31, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=244.31, default_y=-591.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=244.31, default_y=-581.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=295.21, default_y=-601.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=295.21, default_y=-591.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=295.21, default_y=-581.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.23, default_y=-726.88):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=30.0)
                Staff(2)
            with Note(default_x=74.64, default_y=-726.88):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=74.64, default_y=-691.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=125.55, default_y=-726.88):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=125.55, default_y=-691.88):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=162.65, default_y=-736.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.65, default_y=-701.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=213.56, default_y=-736.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=213.56, default_y=-701.88):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=244.31, default_y=-746.88):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=244.31, default_y=-711.88):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=295.21, default_y=-746.88):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=295.21, default_y=-711.88):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=691.12):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=100.82, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.82, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=100.82, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=145.44, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=179.13, default_y=-540.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.13, default_y=-530.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-54.51, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=223.75, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=223.75, default_y=-535.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=246.62, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.62, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=291.24, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=291.24, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=317.91, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.91, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=377.37, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=377.37, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=400.24, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=400.24, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=468.12, default_y=-525.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=468.12, default_y=-515.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=580.23, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=580.23, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=606.89, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=606.89, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=666.36, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=666.36, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=100.82, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=100.82, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=291.24, default_y=-695.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=291.24, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=317.91, default_y=-690.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.91, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=377.37, default_y=-685.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=377.37, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=400.24, default_y=-680.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=400.24, default_y=-670.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=444.86, default_y=-675.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=444.86, default_y=-665.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=468.12, default_y=-670.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=468.12, default_y=-660.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=512.74, default_y=-675.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=512.74, default_y=-665.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=535.61, default_y=-680.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=535.61, default_y=-670.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=580.23, default_y=-685.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=580.23, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=606.89, default_y=-690.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=606.89, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=666.36, default_y=-695.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=666.36, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=544.68):
            with Note(default_x=20.72, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=20.72, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=59.36, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=59.36, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=79.17, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.17, default_y=-535.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=130.66, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=130.66, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=150.47, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.47, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=189.11, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=189.11, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=208.92, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.92, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=260.41, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=260.41, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=280.22, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=280.22, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=338.67, default_y=-530.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=338.67, default_y=-520.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=448.61, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=448.61, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=468.42, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=468.42, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=519.91, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=519.91, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=20.72, default_y=-700.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=20.72, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=79.17, default_y=-655.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=79.17, default_y=-645.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=189.11, default_y=-700.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=189.11, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=208.92, default_y=-695.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.92, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=260.41, default_y=-690.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=260.41, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=280.22, default_y=-685.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=280.22, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=318.86, default_y=-680.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=318.86, default_y=-670.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=338.67, default_y=-675.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=338.67, default_y=-665.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=390.16, default_y=-680.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=390.16, default_y=-670.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=409.97, default_y=-685.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=409.97, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=448.61, default_y=-690.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=448.61, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=468.42, default_y=-695.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=468.42, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=519.91, default_y=-700.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=519.91, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=603.38):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=89.72, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.72, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=127.56, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=127.56, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=146.96, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.96, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=197.39, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=197.39, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=216.79, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=216.79, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=254.63, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=254.63, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=274.03, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.03, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=324.47, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=324.47, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=343.86, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=343.86, default_y=-570.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=401.1, default_y=-535.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=401.1, default_y=-525.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=508.78, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=508.78, default_y=-570.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=528.18, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=528.18, default_y=-565.0):
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
            with Note(default_x=578.61, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=578.61, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=89.72, default_y=-705.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=89.72, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=146.96, default_y=-660.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=146.96, default_y=-650.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=254.63, default_y=-705.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=254.63, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=274.03, default_y=-700.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.03, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=324.47, default_y=-695.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=324.47, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=343.86, default_y=-690.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=343.86, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=381.71, default_y=-685.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=381.71, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=401.1, default_y=-680.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=401.1, default_y=-670.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=451.54, default_y=-685.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=451.54, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=470.94, default_y=-690.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=470.94, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=508.78, default_y=-695.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=508.78, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=528.18, default_y=-700.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=528.18, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=578.61, default_y=-705.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=578.61, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=632.42):
            with Note(default_x=20.72, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=20.72, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=63.58, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=63.58, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=85.55, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.55, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=142.67, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=142.67, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=164.64, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.64, default_y=-535.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=207.5, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=230.77, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.77, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=287.89, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=287.89, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=317.78, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=405.32, default_y=-530.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=527.27, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=550.53, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=607.66, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(32.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=333.95, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=373.81, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=405.32, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.44, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=484.41, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=527.27, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=550.53, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=607.66, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(32.0)
            with Note(default_x=20.72, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=20.72, default_y=-700.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=85.55, default_y=-665.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=85.55, default_y=-655.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=-97.75)
                Staff(2)
            with Note(default_x=207.5, default_y=-745.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=207.5, default_y=-710.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=230.77, default_y=-740.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(0)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.77, default_y=-705.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=287.89, default_y=-735.0):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=287.89, default_y=-700.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=317.78, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=317.78, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=373.81, default_y=-725.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=373.81, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=405.32, default_y=-720.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.32, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=462.44, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=462.44, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=484.41, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=484.41, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=527.27, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=527.27, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=550.53, default_y=-725.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=550.53, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=607.66, default_y=-720.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=607.66, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
        with Measure(number='11', width=578.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=88.78, default_y=-585.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=88.78, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=200.34, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=200.34, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=200.34, default_y=-535.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=265.02, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=265.02, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=265.02, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=305.59, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=305.59, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=370.27, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=370.27, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=410.84, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=410.84, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=460.3, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=485.66, default_y=-520.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=551.58, default_y=-525.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(32.0)
            with Note(default_x=88.78, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=88.78, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=200.34, default_y=-705.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=200.34, default_y=-670.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=265.02, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=265.02, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=305.59, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=305.59, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=370.27, default_y=-720.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=370.27, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=410.84, default_y=-725.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=410.84, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=526.23, default_y=-735.0):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=526.23, default_y=-700.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='12', width=657.26):
            with Note(default_x=17.19, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=17.19, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=17.19, default_y=-530.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=65.9, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=90.87, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.87, default_y=-530.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=139.58, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=139.58, default_y=-535.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=164.55, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.55, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=213.27, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=245.33, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.33, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=310.25, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=310.25, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=335.22, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=335.22, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=408.9, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=531.3, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=531.3, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=565.77, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=565.77, default_y=-535.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=630.69, default_y=-540.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=630.69, default_y=-530.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.19, default_y=-720.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=17.19, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=213.27, default_y=-675.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=213.27, default_y=-665.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=245.33, default_y=-670.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.33, default_y=-660.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=310.25, default_y=-665.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=310.25, default_y=-655.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=335.22, default_y=-660.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=335.22, default_y=-650.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=383.93, default_y=-655.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=383.93, default_y=-645.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=408.9, default_y=-650.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.9, default_y=-640.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=457.62, default_y=-655.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=457.62, default_y=-645.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=482.59, default_y=-660.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=482.59, default_y=-650.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=531.3, default_y=-665.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=531.3, default_y=-655.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=565.77, default_y=-670.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=565.77, default_y=-660.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=630.69, default_y=-675.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=630.69, default_y=-665.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=649.86):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.9)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-535.9):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.58, default_y=-525.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=130.72, default_y=-530.9):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=130.72, default_y=-520.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=153.98, default_y=-525.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.98, default_y=-515.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=204.81, default_y=-530.9):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=204.81, default_y=-520.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=228.07, default_y=-535.9):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.07, default_y=-525.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=266.21, default_y=-540.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=266.21, default_y=-530.9):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=294.48, default_y=-545.9):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.48, default_y=-535.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=345.3, default_y=-550.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=345.3, default_y=-540.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=377.37, default_y=-555.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=377.37, default_y=-545.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=438.77, default_y=-555.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=551.0, default_y=-555.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=551.0, default_y=-545.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=574.26, default_y=-550.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=574.26, default_y=-540.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=625.09, default_y=-545.9):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=625.09, default_y=-535.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=92.58, default_y=-680.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=92.58, default_y=-670.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=153.98, default_y=-715.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=153.98, default_y=-680.9):
                Chord()
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
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=266.21, default_y=-680.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=266.21, default_y=-670.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=294.48, default_y=-675.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.48, default_y=-665.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=345.3, default_y=-670.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=345.3, default_y=-660.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=377.37, default_y=-665.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=377.37, default_y=-655.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=415.5, default_y=-660.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=415.5, default_y=-650.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=438.77, default_y=-655.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=438.77, default_y=-645.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=489.6, default_y=-660.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=489.6, default_y=-650.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=512.86, default_y=-665.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=512.86, default_y=-655.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=551.0, default_y=-670.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=551.0, default_y=-660.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=574.26, default_y=-675.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=574.26, default_y=-665.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=625.09, default_y=-680.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=625.09, default_y=-670.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=585.94):
            with Note(default_x=19.31, default_y=-540.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=19.31, default_y=-530.9):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=59.83, default_y=-535.9):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=59.83, default_y=-525.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=83.09, default_y=-530.9):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.09, default_y=-520.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=137.1, default_y=-535.9):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=137.1, default_y=-525.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=160.36, default_y=-540.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.36, default_y=-530.9):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=200.89, default_y=-545.9):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=200.89, default_y=-535.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=221.66, default_y=-550.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.66, default_y=-540.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=275.66, default_y=-555.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=275.66, default_y=-545.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=298.93, default_y=-560.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=298.93, default_y=-550.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=362.72, default_y=-560.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=480.51, default_y=-585.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=480.51, default_y=-550.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=507.17, default_y=-580.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=507.17, default_y=-545.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=561.18, default_y=-575.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=561.18, default_y=-540.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=19.31, default_y=-685.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=19.31, default_y=-675.9):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=83.09, default_y=-720.9):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=83.09, default_y=-685.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=200.89, default_y=-685.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=200.89, default_y=-675.9):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=221.66, default_y=-680.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.66, default_y=-670.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=275.66, default_y=-675.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=275.66, default_y=-665.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=298.93, default_y=-670.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.93, default_y=-660.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=339.45, default_y=-665.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=339.45, default_y=-655.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=362.72, default_y=-660.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.72, default_y=-650.9):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=416.72, default_y=-665.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=416.72, default_y=-655.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=439.99, default_y=-670.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=439.99, default_y=-660.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=480.51, default_y=-675.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=480.51, default_y=-665.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=507.17, default_y=-680.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=507.17, default_y=-670.9):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=561.18, default_y=-685.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=561.18, default_y=-675.9):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=676.31):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(106.39)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=97.58, default_y=-581.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=97.58, default_y=-546.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=137.04, default_y=-576.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=137.04, default_y=-541.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=160.31, default_y=-571.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.31, default_y=-536.39):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=212.9, default_y=-576.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=212.9, default_y=-541.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=233.12, default_y=-581.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.12, default_y=-546.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=272.59, default_y=-586.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=272.59, default_y=-551.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=299.25, default_y=-591.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=299.25, default_y=-556.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=351.84, default_y=-596.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=351.84, default_y=-561.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=385.54, default_y=-601.39):
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
            with Note(default_x=385.54, default_y=-591.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=385.54, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=498.81, default_y=-591.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=498.81, default_y=-576.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=498.81, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=539.27, default_y=-586.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=539.27, default_y=-576.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=539.27, default_y=-561.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=631.32, default_y=-586.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=631.32, default_y=-576.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=631.32, default_y=-561.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=97.58, default_y=-701.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=97.58, default_y=-691.39):
                Chord()
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
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=272.59, default_y=-701.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=272.59, default_y=-691.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=299.25, default_y=-696.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=299.25, default_y=-686.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=351.84, default_y=-691.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=351.84, default_y=-681.39):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=385.54, default_y=-721.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=385.54, default_y=-686.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=446.22, default_y=-721.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=446.22, default_y=-686.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=466.45, default_y=-756.39):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=466.45, default_y=-721.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=519.04, default_y=-721.39):
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
            with Note(default_x=519.04, default_y=-686.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=539.27, default_y=-731.39):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=539.27, default_y=-696.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=578.73, default_y=-721.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=578.73, default_y=-686.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=598.96, default_y=-731.39):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=598.96, default_y=-696.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=651.55, default_y=-741.39):
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
            with Note(default_x=651.55, default_y=-706.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=559.49):
            with Note(default_x=17.19, default_y=-586.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=17.19, default_y=-576.39):
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
            with Note(default_x=17.19, default_y=-561.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=58.47, default_y=-576.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=97.17, default_y=-591.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.17, default_y=-576.39):
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
            with Note(default_x=97.17, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=138.46, default_y=-556.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=159.62, default_y=-576.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.62, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=159.62, default_y=-556.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=159.62, default_y=-541.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=222.07, default_y=-591.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.07, default_y=-576.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=222.07, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=296.46, default_y=-586.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.46, default_y=-576.39):
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
            with Note(default_x=296.46, default_y=-561.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=337.75, default_y=-576.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=358.91, default_y=-591.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.91, default_y=-576.39):
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
            with Note(default_x=358.91, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=400.2, default_y=-556.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=421.36, default_y=-576.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=421.36, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=421.36, default_y=-556.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=421.36, default_y=-541.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=483.81, default_y=-576.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=483.81, default_y=-566.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=483.81, default_y=-556.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=17.19, default_y=-721.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=17.19, default_y=-686.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=97.17, default_y=-756.39):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=97.17, default_y=-721.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=200.91, default_y=-721.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=222.07, default_y=-756.39):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.36, default_y=-721.39):
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
            with Note(default_x=296.46, default_y=-741.39):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=296.46, default_y=-706.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=358.91, default_y=-756.39):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=358.91, default_y=-721.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=462.65, default_y=-721.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=483.81, default_y=-756.39):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=525.1, default_y=-721.39):
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
        with Measure(number='17', width=666.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.58, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=92.58, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=138.36, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=177.05, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.05, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=177.05, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=222.83, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-78.3)
                Staff(1)
            with Note(default_x=246.3, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.3, default_y=-530.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=292.07, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=315.54, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.32, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=384.78, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=430.56, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=454.02, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=499.8, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=523.27, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=569.05, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=595.71, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=641.49, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=92.58, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=92.58, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=177.05, default_y=-745.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=177.05, default_y=-710.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=292.07, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=292.07, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=315.54, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.54, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=361.32, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=361.32, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=384.78, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=384.78, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=454.02, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=454.02, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=523.27, default_y=-720.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=523.27, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=595.71, default_y=-725.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=595.71, default_y=-690.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=569.24):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=16.72, default_y=-585.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Note(default_x=165.3, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=189.66, default_y=-530.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.16, default_y=-535.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=261.51, default_y=-540.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=309.02, default_y=-535.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=335.69, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.2, default_y=-540.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=407.55, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=455.05, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=495.79, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=543.29, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(32.0)
            with Note(default_x=16.72, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=16.72, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=189.66, default_y=-665.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=189.66, default_y=-655.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=261.51, default_y=-660.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=261.51, default_y=-650.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=335.69, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=335.69, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=407.55, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=407.55, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=483.92, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=495.79, default_y=-575.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=335.69, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=335.69, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=407.55, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=407.55, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=495.79, default_y=-745.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=495.79, default_y=-710.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='19', width=498.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.0)
                with StaffLayout(number=2):
                    StaffDistance(95.0)
            with Note(default_x=92.58, default_y=-585.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=92.58, default_y=-575.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=92.58, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=199.36, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=216.86, default_y=-540.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.0, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=268.5, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.64, default_y=-545.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=320.14, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=354.28, default_y=-550.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=371.78, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=405.93, default_y=-555.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=439.62, default_y=-565.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=473.76, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=92.58, default_y=-740.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=92.58, default_y=-705.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=216.86, default_y=-675.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=216.86, default_y=-665.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=268.5, default_y=-670.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=268.5, default_y=-660.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=320.14, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=320.14, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=371.78, default_y=-585.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=371.78, default_y=-570.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=439.62, default_y=-590.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=439.62, default_y=-575.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=320.14, default_y=-735.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=320.14, default_y=-700.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=371.78, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=371.78, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=439.62, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=439.62, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=283.0):
            with Note(default_x=22.27, default_y=-595.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=22.27, default_y=-570.0):
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
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=-31.11, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=84.93, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=84.93, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=84.93, default_y=-535.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=187.41, default_y=-560.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=187.41, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=187.41, default_y=-540.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=218.74, default_y=-570.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=218.74, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=218.74, default_y=-545.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=250.07, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=250.07, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=250.07, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-17.41, relative_y=-28.22):
                        Pp()
                Staff(2)
                Sound(dynamics=27.78)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=22.27, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=22.27, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=53.6, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=53.6, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=84.93, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=84.93, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=116.26, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=116.26, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=147.59, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=147.59, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=187.41, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.41, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=218.74, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=218.74, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=250.07, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=250.07, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='21', width=249.77):
            with Note(default_x=26.03, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=26.03, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=37.9, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=53.8, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.8, default_y=-560.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=65.66, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=81.57, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.57, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=81.57, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=109.33, default_y=-575.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.33, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=109.33, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.1, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.1, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.1, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=164.87, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.87, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=164.87, default_y=-550.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=192.63, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=192.63, default_y=-570.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=192.63, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=220.4, default_y=-580.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=220.4, default_y=-570.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=220.4, default_y=-555.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=26.03, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=26.03, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=53.8, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=53.8, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=81.57, default_y=-720.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.57, default_y=-685.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=109.33, default_y=-715.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=109.33, default_y=-680.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=137.1, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=137.1, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=164.87, default_y=-710.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.87, default_y=-675.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=192.63, default_y=-745.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.63, default_y=-710.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=220.4, default_y=-745.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=220.4, default_y=-710.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='22', width=204.5):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=40.61, default_y=-585.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=40.61, default_y=-575.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=40.61, default_y=-550.0):
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
            with Note(default_x=90.23, default_y=-585.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=90.23, default_y=-575.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=90.23, default_y=-565.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=115.51, default_y=-610.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=1.5, relative_y=10.0)
            with Note(default_x=115.51, default_y=-600.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=115.51, default_y=-585.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=115.51, default_y=-575.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=15.8, default_y=-730.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
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
            with Note(default_x=65.42, default_y=-730.0):
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
                        Accent()
            with Note(default_x=65.42, default_y=-695.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
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
            with Note(default_x=115.51, default_y=-765.0):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=115.51, default_y=-730.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')