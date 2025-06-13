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
            Millimeters(6.4)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1855.79)
            PageWidth(1312.86)
            with PageMargins(type='even'):
                LeftMargin(62.5)
                RightMargin(62.5)
                TopMargin(62.5)
                BottomMargin(125.0)
            with PageMargins(type='odd'):
                LeftMargin(62.5)
                RightMargin(62.5)
                TopMargin(62.5)
                BottomMargin(125.0)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('James Gibb editions', default_x=62.5, default_y=1693.29, justify='left', valign='bottom', font_family='Times New Roman', font_size='7')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Dona nobis pacem - Beethoven', default_x=1250.36, default_y=1693.29, justify='right', valign='bottom', font_family='Times New Roman', font_size='7')
    with Credit(page=1):
        CreditType('title')
        CreditWords('#', default_x=656.431, default_y=1793.29, justify='center', valign='top', font_family='Times New Roman', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano')
            PartAbbreviation('S')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            PartAbbreviation('A')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            PartAbbreviation('B')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Midi_74')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=262.83):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(93.9)
                        RightMargin(0.0)
                    TopSystemDistance(321.83)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=85.41, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Sound(tempo=76.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Dona nobis pacem', relative_y=20.0, font_family='Times New Roman', font_size='19')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Ludwig van Beethoven\n', default_y=61.89, relative_y=20.0, font_family='Times New Roman', font_size='11')
                    Words('(1770-1827)')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=116.42, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Sound(tempo=76.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=147.44, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Sound(tempo=76.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=178.46, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Sound(tempo=76.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='2', width=256.78):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='3', width=311.06):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='4', width=263.3):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='5', width=269.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=181.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=241.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='6', width=303.21):
            with Note(default_x=21.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=80.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=186.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=204.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=223.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=309.87):
            with Note(default_x=21.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=56.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=75.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=167.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=233.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        TrillMark()
        with Measure(number='8', width=271.51):
            with Note(default_x=21.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=92.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=122.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=190.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=269.23):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=61.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=325.86):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='11', width=337.35):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=221.93):
            with Note(default_x=21.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=86.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=112.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=162.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='13', width=440.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=110.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-47.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=133.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=157.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=258.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-47.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=343.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.0, default_y=-47.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
        with Measure(number='14', width=404.42):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=107.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=302.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.89, default_y=-47.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
        with Measure(number='15', width=309.83):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=55.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=91.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=163.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-47.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='16', width=376.56):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=244.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=336.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='17', width=333.3):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=86.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=195.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=217.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=240.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=444.51):
            with Note(default_x=21.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=65.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=93.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=230.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=275.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=302.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=330.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=360.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=387.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=415.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=360.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=61.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-47.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=100.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-47.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=136.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=172.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=207.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=368.71):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=98.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=195.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.25, default_y=-47.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
        with Measure(number='21', width=424.81):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=112.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=317.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-47.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
        with Measure(number='22', width=458.73):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=61.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=155.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=259.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=300.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=326.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=352.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=379.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=431.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=405.62):
            with Note(default_x=21.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=252.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=278.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=303.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=328.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=290.02):
            with Note(default_x=16.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=65.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=367.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=226.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=331.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='26', width=359.19):
            with Note(default_x=21.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=96.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=217.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-42.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=240.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=264.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=287.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=427.37):
            with Note(default_x=21.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-42.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=63.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-42.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=90.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=143.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=224.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-42.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=267.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-42.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=293.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=319.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=346.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=372.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=381.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=61.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-51.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=157.04, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-51.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=263.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=321.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='29', width=389.85):
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=109.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=218.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-51.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=382.67):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='31', width=408.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=270.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=300.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=321.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=342.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=379.75):
            with Note(default_x=17.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=201.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=238.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=261.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=285.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=308.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=354.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=366.07):
            with Note(default_x=20.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=192.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=228.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=251.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=273.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=413.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=61.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=105.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=192.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=236.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=280.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=323.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=367.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=302.39):
            with Note(default_x=21.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='36', width=438.96):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='37', width=349.9):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=212.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=310.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='38', width=367.13):
            with Note(default_x=14.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=97.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=226.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=249.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=296.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=342.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='39', width=437.34):
            with Note(default_x=21.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=119.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.0, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=227.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=271.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=381.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.89, default_y=-43.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
        with Measure(number='40', width=445.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=61.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=105.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=214.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.95, default_y=-42.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=268.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=312.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.94, default_y=-42.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=356.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-42.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=400.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='41', width=302.11):
            with Note(default_x=21.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-42.13, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='42', width=406.91):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='43', width=421.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=61.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=180.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=220.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=320.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='44', width=350.52):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=48.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=70.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=215.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=237.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=259.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=281.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='45', width=381.88):
            with Note(default_x=21.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=59.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=82.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=200.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=238.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=262.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=285.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=309.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=356.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='46', width=410.13):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(33.49)
                        RightMargin(0.0)
                    TopSystemDistance(240.21)
            with Note(default_x=64.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=101.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=125.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=148.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=194.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=241.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=278.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=362.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='47', width=282.37):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('75')
                Sound(tempo=75.0)
            with Note(default_x=10.72, default_y=-10.0):
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=31.02, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('74')
                Sound(tempo=74.0)
            with Note(default_x=45.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.73, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('74')
                Sound(tempo=74.0)
            with Note(default_x=115.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=41.75, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('73')
                Sound(tempo=73.0)
            with Note(default_x=150.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem.')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=72.77, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Sound(tempo=72.0)
            with Note(default_x=206.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=103.78, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Sound(tempo=72.0)
            with Note(default_x=241.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.66, default_y=-43.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
        with Measure(number='48', width=194.02):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=134.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('71')
                Sound(tempo=71.0)
            with Note(default_x=11.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=165.82, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=61.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-43.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=196.84, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Sound(tempo=69.0)
            with Note(default_x=111.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.1, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='49', width=138.13):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Sound(tempo=66.0)
            with Note(default_x=18.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=5.34, default_y=-43.1, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.')
        with Measure(number='50', width=129.73):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Sound(tempo=64.0)
            with Note(default_x=13.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=262.83):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='2', width=256.78):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='3', width=311.06):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='4', width=263.3):
            with Note(default_x=16.65, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=103.95, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=133.04, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=191.24, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='5', width=269.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.91)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=86.65, default_y=-147.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=102.44, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=118.24, default_y=-147.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.03, default_y=-157.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.83, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.63, default_y=-147.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=181.42, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=216.17, default_y=-162.91):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
        with Measure(number='6', width=303.21):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=50.85, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=80.35, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.86, default_y=-147.91):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=138.3, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.74, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=223.13, default_y=-147.91):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='7', width=309.87):
            with Note(default_x=21.35, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=93.63, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note(default_x=167.33, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=185.75, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=204.17, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=263.13, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=271.51):
            with Note(default_x=21.35, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='9', width=269.23):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=123.49, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=149.65, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=201.96, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='10', width=325.86):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.65, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-56.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=71.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.94, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.09, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.24, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.38, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.53, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=253.39, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-56.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
        with Measure(number='11', width=337.35):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=221.93):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=112.06, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=187.56, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-56.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='13', width=440.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.02)
            with Note(default_x=72.35, default_y=-168.02):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.89, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
            with Note(default_x=110.24, default_y=-163.02):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=157.6, default_y=-158.02):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=258.55, default_y=-163.02):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=296.44, default_y=-143.02):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=320.12, default_y=-148.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=343.8, default_y=-143.02):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=367.48, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.16, default_y=-138.02):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=414.84, default_y=-143.02):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=404.42):
            with Note(default_x=17.23, default_y=-148.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=57.31, default_y=-148.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=82.36, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.41, default_y=-148.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.3, default_y=-158.02):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.35, default_y=-143.02):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.4, default_y=-148.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=212.45, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=252.53, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=277.58, default_y=-158.02):
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
            with Note(default_x=302.63, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=327.67, default_y=-163.02):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.72, default_y=-148.02):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=377.77, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=309.83):
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=17.23, default_y=-158.02):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-52.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=55.6, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=127.78, default_y=-158.02):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=163.51, default_y=-153.02):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-52.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
        with Measure(number='16', width=376.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.98)
            with Note(default_x=61.49, default_y=-139.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=148.3, default_y=-144.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=244.75, default_y=-139.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note(default_x=297.8, default_y=-129.98):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-46.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=336.38, default_y=-134.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='17', width=333.3):
            with Note(default_x=14.0, default_y=-139.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=50.25, default_y=-144.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=86.5, default_y=-139.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=122.75, default_y=-149.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=159.0, default_y=-134.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=195.25, default_y=-139.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=240.57, default_y=-144.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
        with Measure(number='18', width=444.51):
            with Note(default_x=21.35, default_y=-139.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.89, default_y=-46.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
            with Note(default_x=65.48, default_y=-144.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.64, default_y=-149.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=230.97, default_y=-144.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=275.1, default_y=-149.98):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=330.26, default_y=-154.98):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=360.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.69)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=61.37, default_y=-168.69):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-56.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=100.88, default_y=-173.69):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-56.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=136.52, default_y=-168.69):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.15, default_y=-163.69):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=207.79, default_y=-158.69):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=243.43, default_y=-153.69):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.7, default_y=-148.69):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=287.97, default_y=-153.69):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=323.61, default_y=-158.69):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=368.71):
            with Note(default_x=16.87, default_y=-163.69):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=195.18, default_y=-158.69):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='21', width=424.81):
            with Note(default_x=16.87, default_y=-163.69):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-56.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=221.48, default_y=-168.69):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.58, default_y=-56.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
        with Measure(number='22', width=458.73):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.15)
            with Note(default_x=61.37, default_y=-151.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=207.18, default_y=-151.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=259.25, default_y=-146.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.89, default_y=-48.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
            with Note(default_x=352.99, default_y=-141.15):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=405.62):
            with Note(default_x=21.35, default_y=-136.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=61.63, default_y=-141.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-48.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=86.8, default_y=-146.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.98, default_y=-141.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.16, default_y=-151.15):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.33, default_y=-136.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.51, default_y=-141.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=212.68, default_y=-146.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-48.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=290.02):
            with Note(default_x=16.65, default_y=-141.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=100.99, default_y=-141.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=136.51, default_y=-146.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=207.54, default_y=-131.15):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='25', width=367.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=96.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-53.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=117.99, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.76, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.53, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.31, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.08, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=226.86, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=296.54, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-53.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
        with Measure(number='26', width=359.19):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.71, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-53.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=96.07, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=133.43, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=156.78, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.13, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=264.19, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='27', width=427.37):
            with Note(default_x=21.35, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=116.56, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-53.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note(default_x=224.77, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-53.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=319.98, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=381.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.06)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=61.37, default_y=-178.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=103.89, default_y=-178.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=130.46, default_y=-173.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=157.04, default_y=-168.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.61, default_y=-173.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.18, default_y=-168.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.76, default_y=-163.06):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=263.33, default_y=-158.06):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=321.79, default_y=-183.06):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
        with Measure(number='29', width=389.85):
            with Note(default_x=13.8, default_y=-188.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=218.25, default_y=-193.06):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=261.56, default_y=-183.06):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=303.79, default_y=-178.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=346.02, default_y=-173.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
        with Measure(number='30', width=382.67):
            with Note(default_x=14.22, default_y=-168.06):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.89, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
            with Note(default_x=54.98, default_y=-173.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.74, default_y=-178.06):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='31', width=408.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.77)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=95.08, default_y=-136.77):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-49.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=115.91, default_y=-141.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=136.75, default_y=-136.77):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.59, default_y=-146.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.46, default_y=-131.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.3, default_y=-136.77):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=236.83, default_y=-141.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='32', width=379.75):
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=17.95, default_y=-141.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-49.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=55.17, default_y=-141.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-49.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=85.07, default_y=-146.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.33, default_y=-141.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.59, default_y=-151.77):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.85, default_y=-136.77):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.11, default_y=-141.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.01, default_y=-146.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=366.07):
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=21.35, default_y=-146.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-49.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=57.4, default_y=-146.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-49.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=79.93, default_y=-151.77):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=102.46, default_y=-146.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.99, default_y=-156.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.53, default_y=-141.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.06, default_y=-146.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.23, default_y=-151.77):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=413.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.85)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=61.37, default_y=-162.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=105.13, default_y=-157.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=148.88, default_y=-152.85):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=192.64, default_y=-157.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=236.4, default_y=-157.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=302.39):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='36', width=438.96):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='37', width=349.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.85)
            with Note(default_x=61.37, default_y=-154.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=174.63, default_y=-154.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=212.39, default_y=-174.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=272.8, default_y=-149.85):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='38', width=367.13):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=51.0, default_y=-159.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=74.12, default_y=-164.85):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.25, default_y=-159.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.37, default_y=-169.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.49, default_y=-154.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.62, default_y=-159.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=189.38, default_y=-164.85):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='39', width=437.34):
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=21.35, default_y=-154.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=64.79, default_y=-144.85):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=91.94, default_y=-149.85):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.09, default_y=-144.85):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.24, default_y=-154.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.39, default_y=-139.85):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.54, default_y=-144.85):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=227.69, default_y=-149.85):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=271.13, default_y=-149.85):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=298.28, default_y=-154.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=325.43, default_y=-149.85):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.58, default_y=-159.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.44, default_y=-144.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.59, default_y=-149.85):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='40', width=445.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-44.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=105.07, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-44.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=132.38, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=159.7, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.01, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.32, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.64, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.95, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=312.65, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=356.35, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='41', width=302.11):
            with Note(default_x=21.35, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-44.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=160.93, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=261.74, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='42', width=406.91):
            with Note(default_x=14.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=106.68, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=250.85, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-44.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=276.59, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=302.33, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=328.08, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.82, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=379.57, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='43', width=421.98):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.76)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=61.37, default_y=-164.76):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-58.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=101.15, default_y=-174.76):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-58.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=140.92, default_y=-164.76):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.69, default_y=-159.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=220.46, default_y=-154.76):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=320.94, default_y=-144.76):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='44', width=350.52):
            with Note(default_x=13.72, default_y=-164.76):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-58.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=92.74, default_y=-159.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.55, default_y=-154.76):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-58.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=259.9, default_y=-144.76):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=303.8, default_y=-144.76):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-58.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='45', width=381.88):
            with Note(default_x=20.98, default_y=-149.76):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-58.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=200.45, default_y=-154.76):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-58.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='46', width=410.13):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.63)
            with Note(default_x=64.69, default_y=-156.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-44.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=148.33, default_y=-156.63):
                with Pitch():
                    Step('F')
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
            with Note(default_x=171.56, default_y=-151.63):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.79, default_y=-146.63):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.02, default_y=-156.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=241.26, default_y=-151.63):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=324.89, default_y=-156.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='47', width=282.37):
            with Note(default_x=10.72, default_y=-161.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=45.64, default_y=-151.63):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=80.55, default_y=-151.63):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=150.38, default_y=-151.63):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-44.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem.')
            with Note(default_x=206.24, default_y=-161.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=241.16, default_y=-161.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.66, default_y=-44.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
        with Measure(number='48', width=194.02):
            with Note(default_x=11.35, default_y=-156.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=61.65, default_y=-151.63):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-44.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
            with Note(default_x=111.59, default_y=-156.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-44.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='49', width=138.13):
            with Note(default_x=18.96, default_y=-161.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=5.34, default_y=-44.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.')
        with Measure(number='50', width=129.73):
            with Note(default_x=13.32, default_y=-161.63):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=262.83):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(67.34)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='2', width=256.78):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=153.38, default_y=-227.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=225.02, default_y=-227.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='3', width=311.06):
            with Note(default_x=14.0, default_y=-232.34):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=79.03, default_y=-217.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=184.69, default_y=-227.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-45.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=205.01, default_y=-232.34):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=225.33, default_y=-227.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=245.65, default_y=-237.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.98, default_y=-222.34):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.3, default_y=-227.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=263.3):
            with Note(default_x=16.65, default_y=-232.34):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.85, default_y=-242.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-45.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=162.14, default_y=-227.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-45.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=191.24, default_y=-237.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=220.34, default_y=-232.34):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=238.53, default_y=-227.34):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=269.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.41)
            with Note(default_x=61.37, default_y=-241.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=118.24, default_y=-251.32):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=181.42, default_y=-246.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=216.17, default_y=-251.32):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=241.45, default_y=-256.32):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=303.21):
            with Note(default_x=21.35, default_y=-261.32):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='7', width=309.87):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='8', width=271.51):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=62.67, default_y=-246.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=92.72, default_y=-246.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=122.42, default_y=-251.32):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-46.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
        with Measure(number='9', width=269.23):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.43)
            with Note(default_x=61.37, default_y=-236.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='10', width=325.86):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=182.53, default_y=-246.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=288.83, default_y=-246.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='11', width=337.35):
            with Note(default_x=14.0, default_y=-251.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=86.85, default_y=-236.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=201.74, default_y=-246.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-45.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=221.98, default_y=-251.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=242.21, default_y=-246.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=272.11, default_y=-256.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.35, default_y=-241.43):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.58, default_y=-246.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=221.93):
            with Note(default_x=21.35, default_y=-251.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=61.61, default_y=-261.43):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-45.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=137.22, default_y=-261.43):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-45.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=162.39, default_y=-246.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=187.56, default_y=-251.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
        with Measure(number='13', width=440.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.74)
            with Note(default_x=72.35, default_y=-270.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=110.24, default_y=-275.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=157.6, default_y=-280.77):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=258.55, default_y=-275.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-57.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=404.42):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='15', width=309.83):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=91.69, default_y=-245.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=199.96, default_y=-245.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=236.05, default_y=-255.77):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=272.14, default_y=-265.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='16', width=376.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.31)
            with Note(default_x=61.13, default_y=-245.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=244.75, default_y=-250.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=333.3):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='18', width=444.51):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
            with Note(default_x=330.26, default_y=-240.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.0, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
        with Measure(number='19', width=360.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.41)
            with Note(default_x=61.37, default_y=-276.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=136.52, default_y=-276.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=207.79, default_y=-286.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=287.97, default_y=-271.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='20', width=368.71):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=53.21, default_y=-281.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=75.7, default_y=-286.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.18, default_y=-281.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.08, default_y=-291.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.56, default_y=-276.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.05, default_y=-281.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=195.54, default_y=-286.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=276.49, default_y=-296.1):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
        with Measure(number='21', width=424.81):
            with Note(default_x=17.23, default_y=-271.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=112.17, default_y=-276.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=317.33, default_y=-281.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='22', width=458.73):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.4)
            with Note(default_x=61.37, default_y=-243.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=155.1, default_y=-248.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.2, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=259.25, default_y=-248.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-45.2, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=405.62):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='24', width=290.02):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=172.02, default_y=-233.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-45.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=207.54, default_y=-243.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.05, default_y=-238.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.2, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=265.25, default_y=-233.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=367.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.19)
            with Note(default_x=61.37, default_y=-243.19):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=139.76, default_y=-253.19):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=226.86, default_y=-248.19):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=261.7, default_y=-253.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=296.54, default_y=-258.19):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=331.37, default_y=-263.19):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='26', width=359.19):
            with Note(default_x=21.35, default_y=-268.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='27', width=427.37):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='28', width=381.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.91)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='29', width=389.85):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=218.25, default_y=-286.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=346.02, default_y=-286.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='30', width=382.67):
            with Note(default_x=14.22, default_y=-296.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=95.74, default_y=-281.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=228.22, default_y=-291.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=253.69, default_y=-296.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=279.17, default_y=-291.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=304.64, default_y=-301.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.12, default_y=-286.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.6, default_y=-291.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=408.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.48)
            with Note(default_x=61.73, default_y=-264.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=321.27, default_y=-234.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.0, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
        with Measure(number='32', width=379.75):
            with Note(default_x=17.95, default_y=-234.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=108.33, default_y=-254.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=285.11, default_y=-239.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.89, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
        with Measure(number='33', width=366.07):
            with Note(default_x=21.35, default_y=-239.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.46, default_y=-259.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=273.71, default_y=-244.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
        with Measure(number='34', width=413.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.17)
            with Note(default_x=61.37, default_y=-258.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=105.13, default_y=-248.02):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=148.88, default_y=-243.02):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-45.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=236.4, default_y=-248.02):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-45.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=280.15, default_y=-258.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=323.91, default_y=-263.02):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=367.66, default_y=-268.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=302.39):
            with Note(default_x=21.35, default_y=-273.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=161.07, default_y=-258.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=261.98, default_y=-258.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='36', width=438.96):
            with Note(default_x=13.78, default_y=-268.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.64, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=114.1, default_y=-253.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-45.64, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=270.16, default_y=-258.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-45.64, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=298.02, default_y=-263.02):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=325.89, default_y=-258.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=353.76, default_y=-268.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.63, default_y=-253.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=409.49, default_y=-258.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='37', width=349.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.43)
            with Note(default_x=61.37, default_y=-251.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=99.13, default_y=-241.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=136.88, default_y=-246.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=174.63, default_y=-251.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=212.39, default_y=-236.29):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-46.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='38', width=367.13):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='39', width=437.34):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='40', width=445.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.07)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='41', width=302.11):
            with Note(default_x=21.35, default_y=-231.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=122.16, default_y=-231.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=160.93, default_y=-236.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=222.97, default_y=-221.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='42', width=406.91):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=55.19, default_y=-231.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=80.94, default_y=-236.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.68, default_y=-231.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.42, default_y=-241.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.17, default_y=-226.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.91, default_y=-231.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=209.66, default_y=-236.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=302.33, default_y=-246.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem')
        with Measure(number='43', width=421.98):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.71)
            with Note(default_x=61.37, default_y=-277.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.95, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=140.92, default_y=-287.47):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=220.46, default_y=-292.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=260.24, default_y=-292.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=296.09, default_y=-297.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural', parentheses='yes')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=320.94, default_y=-292.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=345.8, default_y=-302.47):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.66, default_y=-297.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=395.52, default_y=-292.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='44', width=350.52):
            with Note(default_x=13.36, default_y=-287.47):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.55, default_y=-292.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=259.9, default_y=-257.47):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.0, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
        with Measure(number='45', width=381.88):
            with Note(default_x=21.35, default_y=-257.47):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=105.99, default_y=-262.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=285.82, default_y=-267.47):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.89, default_y=-51.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
        with Measure(number='46', width=410.13):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.18)
            with Note(default_x=64.69, default_y=-249.81):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=148.33, default_y=-254.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=194.79, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=241.26, default_y=-264.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=278.43, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=301.66, default_y=-264.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=324.89, default_y=-269.81):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=362.06, default_y=-264.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=385.29, default_y=-269.81):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=282.37):
            with Note(default_x=10.72, default_y=-274.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.64, default_y=-249.81):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=80.55, default_y=-254.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=150.38, default_y=-249.81):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem.')
            with Note(default_x=206.24, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=241.16, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.66, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
        with Measure(number='48', width=194.02):
            with Note(default_x=11.35, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=61.65, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
            with Note(default_x=111.59, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='49', width=138.13):
            with Note(default_x=18.96, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=11.98, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.')
        with Measure(number='50', width=129.73):
            with Note(default_x=13.32, default_y=-259.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=262.83):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(75.34)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=83.68, default_y=-332.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=139.99, default_y=-332.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=168.86, default_y=-342.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=215.04, default_y=-327.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='2', width=256.78):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.28, default_y=-337.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=59.13, default_y=-342.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=77.98, default_y=-337.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=96.83, default_y=-347.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.68, default_y=-332.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.53, default_y=-337.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.38, default_y=-342.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=194.85, default_y=-352.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
        with Measure(number='3', width=311.06):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=46.51, default_y=-332.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-43.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=79.03, default_y=-342.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.54, default_y=-337.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=131.86, default_y=-332.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=152.18, default_y=-327.68):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=225.33, default_y=-337.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='4', width=263.3):
            with Note(default_x=16.65, default_y=-332.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=45.75, default_y=-337.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=74.85, default_y=-342.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.95, default_y=-347.68):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=133.04, default_y=-352.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=269.77):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.14)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='6', width=303.21):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='7', width=309.87):
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
            with Note(default_x=233.65, default_y=-353.46):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=281.55, default_y=-353.46):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='8', width=271.51):
            with Note(default_x=21.35, default_y=-363.46):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=62.67, default_y=-348.46):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=152.83, default_y=-358.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=171.61, default_y=-363.46):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=190.4, default_y=-358.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.18, default_y=-368.46):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.96, default_y=-353.46):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.75, default_y=-358.46):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=269.23):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.36)
            with Note(default_x=61.37, default_y=-362.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.34, default_y=-372.79):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=175.8, default_y=-337.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=10.0, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=201.96, default_y=-347.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=228.11, default_y=-342.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=244.46, default_y=-337.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=325.86):
            with Note(default_x=14.22, default_y=-332.79):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.89, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
            with Note(default_x=49.65, default_y=-337.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.94, default_y=-342.79):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=182.53, default_y=-337.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=217.96, default_y=-342.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=253.39, default_y=-347.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.94, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
        with Measure(number='11', width=337.35):
            with Note(default_x=14.0, default_y=-347.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=46.38, default_y=-352.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=66.62, default_y=-357.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.85, default_y=-352.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.23, default_y=-337.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.47, default_y=-342.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=169.36, default_y=-347.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=201.74, default_y=-352.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=242.21, default_y=-357.79):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=221.93):
            with Note(default_x=21.35, default_y=-352.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-60.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='13', width=440.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.01)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=258.55, default_y=-368.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=343.8, default_y=-358.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
        with Measure(number='14', width=404.42):
            with Note(default_x=17.23, default_y=-363.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=107.41, default_y=-348.77):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=212.45, default_y=-368.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
            with Note(default_x=302.63, default_y=-353.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
        with Measure(number='15', width=309.83):
            with Note(default_x=17.23, default_y=-373.77):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=127.78, default_y=-373.77):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=163.87, default_y=-383.77):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=236.05, default_y=-368.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='16', width=376.56):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.03)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=100.07, default_y=-356.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=124.18, default_y=-361.32):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=148.3, default_y=-356.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.41, default_y=-366.32):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.52, default_y=-351.32):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.64, default_y=-356.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=244.75, default_y=-361.32):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=333.3):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='18', width=444.51):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='19', width=360.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.75)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='20', width=368.71):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=231.51, default_y=-379.85):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=254.0, default_y=-384.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=276.49, default_y=-379.85):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.97, default_y=-389.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.46, default_y=-374.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.94, default_y=-379.85):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=424.81):
            with Note(default_x=17.23, default_y=-384.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=59.59, default_y=-384.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=86.06, default_y=-389.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.53, default_y=-384.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.42, default_y=-394.85):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.9, default_y=-379.85):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.37, default_y=-384.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=221.84, default_y=-389.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=264.19, default_y=-389.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=290.86, default_y=-394.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=317.33, default_y=-389.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=343.8, default_y=-399.85):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.27, default_y=-384.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=396.74, default_y=-389.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=458.73):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.17)
            with Note(default_x=61.37, default_y=-349.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=103.03, default_y=-349.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=129.07, default_y=-354.72):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.1, default_y=-349.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.14, default_y=-359.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.18, default_y=-344.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.22, default_y=-349.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=259.25, default_y=-354.72):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=352.99, default_y=-339.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
        with Measure(number='23', width=405.62):
            with Note(default_x=20.98, default_y=-344.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.3, default_y=-43.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note(default_x=212.32, default_y=-364.72):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.59, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
        with Measure(number='24', width=290.02):
            with Note(default_x=16.29, default_y=-359.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.51, default_y=-364.72):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='1', default_x=8.94, default_y=-43.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=367.81):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.14)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='26', width=359.19):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='27', width=427.37):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='28', width=381.85):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.53)
            with Note(default_x=61.37, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=210.18, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=263.33, default_y=-405.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=321.79, default_y=-390.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='29', width=389.85):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=56.39, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=82.78, default_y=-405.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.18, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.57, default_y=-410.5):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.96, default_y=-395.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.36, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=218.25, default_y=-405.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-46.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=261.56, default_y=-415.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-46.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=303.79, default_y=-410.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=346.02, default_y=-405.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
        with Measure(number='30', width=382.67):
            with Note(default_x=14.22, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.89, default_y=-46.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('no-')
            with Note(default_x=54.98, default_y=-405.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.74, default_y=-410.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('bis')
            with Note(default_x=136.5, default_y=-405.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-46.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=161.98, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=187.45, default_y=-395.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=228.22, default_y=-400.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=279.17, default_y=-405.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=408.55):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-354.25):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.3, default_y=-42.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=236.83, default_y=-349.25):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
        with Measure(number='32', width=379.75):
            with Note(default_x=17.59, default_y=-334.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=201.01, default_y=-354.25):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
        with Measure(number='33', width=366.07):
            with Note(default_x=20.98, default_y=-339.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-42.7, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=192.23, default_y=-359.25):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-42.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pa')
        with Measure(number='34', width=413.02):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.0)
            with Note(default_x=61.37, default_y=-376.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('cem,')
            with Note(default_x=105.13, default_y=-381.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=148.88, default_y=-386.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=192.64, default_y=-371.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=236.4, default_y=-391.01):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=302.39):
            with Note(default_x=21.35, default_y=-371.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=122.26, default_y=-371.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=161.07, default_y=-381.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=223.17, default_y=-366.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='36', width=438.96):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.37, default_y=-376.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=86.23, default_y=-381.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.1, default_y=-376.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.97, default_y=-386.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.84, default_y=-371.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.7, default_y=-376.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.57, default_y=-381.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=270.16, default_y=-366.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.0, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('Do-')
            with Note(default_x=325.89, default_y=-371.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=381.63, default_y=-376.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
        with Measure(number='37', width=349.9):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.18)
            with Note(default_x=61.37, default_y=-356.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=99.13, default_y=-346.47):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('bis')
            with Note(default_x=136.88, default_y=-351.47):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=174.63, default_y=-356.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=212.39, default_y=-341.47):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='38', width=367.13):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='39', width=437.34):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=64.79, default_y=-356.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=91.94, default_y=-361.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.09, default_y=-356.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.24, default_y=-366.47):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.39, default_y=-351.47):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.54, default_y=-356.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=227.69, default_y=-361.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=271.13, default_y=-361.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=298.28, default_y=-366.47):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=325.43, default_y=-361.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=352.58, default_y=-371.47):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.44, default_y=-356.47):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.59, default_y=-361.47):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='40', width=445.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.81)
            with Note(default_x=61.37, default_y=-337.88):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.94, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note(default_x=105.07, default_y=-337.88):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.95, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
            with Note(default_x=132.38, default_y=-342.88):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=159.7, default_y=-337.88):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.01, default_y=-347.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.32, default_y=-332.88):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.64, default_y=-337.88):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=268.95, default_y=-332.88):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=312.65, default_y=-337.88):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=356.35, default_y=-342.88):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='41', width=302.11):
            with Note(default_x=21.35, default_y=-347.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-43.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem,')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
        with Measure(number='42', width=406.91):
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='43', width=421.98):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.18)
            with Note():
                Rest()
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='44', width=350.52):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Note(default_x=180.19, default_y=-387.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.31, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('pa-')
        with Measure(number='45', width=381.88):
            with Note(default_x=18.03, default_y=-387.65):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='46', width=410.13):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.67)
            with Note(default_x=61.37, default_y=-371.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='47', width=282.37):
            with Note(default_x=10.36, default_y=-371.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words(',', relative_y=20.0, font_family='Times New Roman', font_size='14')
            with Note(default_x=150.38, default_y=-391.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('cem.')
            with Note(default_x=206.24, default_y=-391.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=241.16, default_y=-391.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.66, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
        with Measure(number='48', width=194.02):
            with Note(default_x=11.35, default_y=-376.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=61.65, default_y=-381.48):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
            with Note(default_x=111.59, default_y=-376.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='49', width=138.13):
            with Note(default_x=18.96, default_y=-391.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=5.34, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.')
        with Measure(number='50', width=129.73):
            with Note(default_x=13.32, default_y=-391.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')