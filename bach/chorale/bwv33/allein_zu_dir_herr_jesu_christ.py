with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('I trust O Christ in You alone')
    with Identification():
        Creator('Allein zu dir\nharmonized JSBach', type='composer')
        Rights('Copyright © 2017 by The Choral Public Domain Library. Edition may be freely distributed, duplicated, performed or recorded.')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(8.10132)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1466.06)
            PageWidth(1037.15)
            with PageMargins(type='even'):
                LeftMargin(49.3747)
                RightMargin(49.3747)
                TopMargin(49.3747)
                BottomMargin(98.7494)
            with PageMargins(type='odd'):
                LeftMargin(49.3747)
                RightMargin(49.3747)
                TopMargin(49.3747)
                BottomMargin(98.7494)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Times New Roman', font_size='13.2741')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Allein zu dir\n', default_x=987.78, default_y=1293.69, justify='right', valign='bottom', font_family='Times New Roman', font_size='12.736')
        CreditWords('harmonized JSBach')
    with Credit(page=1):
        CreditType('title')
        CreditWords('I trust O Christ in You alone', default_x=518.577, default_y=1416.69, justify='center', valign='top', font_family='Times New Roman', font_size='25.472')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Copyright © 2017 by The Choral Public Domain Library. Edition may be freely distributed, duplicated, performed or recorded.', default_x=518.577, default_y=1367.31, justify='center', valign='top', font_family='Times New Roman', font_size='11.6597')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Copyright © 2017 by The Choral Public Domain Library. Edition may be freely distributed, duplicated, performed or recorded.', default_x=518.577, default_y=98.7494, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Copyright © 2017 by The Choral Public Domain Library. Edition may be freely distributed, duplicated, performed or recorded.', default_x=518.577, default_y=98.7494, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Copyright © 2017 by The Choral Public Domain Library. Edition may be freely distributed, duplicated, performed or recorded.', default_x=518.577, default_y=98.7494, justify='center', valign='bottom', font_size='8')
    with Credit(page=4):
        CreditType('rights')
        CreditWords('Copyright © 2017 by The Choral Public Domain Library. Edition may be freely distributed, duplicated, performed or recorded.', default_x=518.577, default_y=98.7494, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('line')
        with ScorePart(id='P1'):
            PartName('Choir')
            PartAbbreviation('Choir')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Choir')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=182.75):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    TopSystemDistance(193.0)
                with StaffLayout(number=2):
                    StaffDistance(167.44)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(1)
                    Mode('major')
                with Time():
                    Beats('4')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-39.8, default_y=26.6, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=106.07, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=-37.62, default_y=-63.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.   I')
                with Lyric(number='2', default_x=-38.67, default_y=-93.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.   My')
                with Lyric(number='3', default_x=-32.05, default_y=-123.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('3.  Con')
            with Note(default_x=106.07, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=106.07, default_y=-257.44):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=106.07, default_y=-222.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=322.57):
            with Direction(placement='above'):
                with DirectionType():
                    Words('B‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=26.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('trust')
                with Lyric(number='2', default_x=6.58, default_y=-93.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('sin')
                with Lyric(number='3', default_x=6.58, default_y=-123.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('firm')
            with Note(default_x=26.93, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=100.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                with Lyric(number='2', default_x=6.58, default_y=-93.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='3', default_x=6.58, default_y=-123.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=100.44, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=173.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('Christ')
                with Lyric(number='2', default_x=6.58, default_y=-93.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('guilt')
                with Lyric(number='3', default_x=6.58, default_y=-123.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('us')
            with Note(default_x=173.95, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=247.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-93.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('are')
                with Lyric(number='3', default_x=6.58, default_y=-123.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Note(default_x=247.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.93, default_y=-237.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=26.93, default_y=-217.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=100.44, default_y=-242.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=100.44, default_y=-207.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=173.95, default_y=-247.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=173.95, default_y=-202.44):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=247.46, default_y=-247.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=247.46, default_y=-212.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=226.18):
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=23.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='2', default_y=-93.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pla')
                with Lyric(number='3', default_y=-123.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gos')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', default_y=6.12, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹6', default_y=30.63, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=73.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', default_y=13.69, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=174.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
                with Lyric(number='2', default_x=6.58, default_y=-93.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('guing')
                with Lyric(number='3', default_x=9.4, default_y=-123.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('pel,')
            with Backup():
                Duration(8.0)
            with Note(default_x=23.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-63.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('you')
            with Note(default_x=73.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=123.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=174.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=23.1, default_y=-227.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=23.1, default_y=-217.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=73.11, default_y=-222.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=73.11, default_y=-212.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=174.21, default_y=-227.44):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.21, default_y=-207.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=202.07):
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', default_y=14.75, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=28.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.21, default_y=-63.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('lone;')
                with Lyric(number='2', default_x=9.21, default_y=-93.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('me;')
                with Lyric(number='3', default_x=9.06, default_y=-123.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lord,')
            with Note(default_x=28.09, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=152.69, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('no')
                with Lyric(number='2', default_x=9.74, default_y=-93.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Oh,')
                with Lyric(number='3', default_x=6.58, default_y=-123.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Note(default_x=152.69, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=28.09, default_y=-247.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=28.09, default_y=-202.44):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=152.69, default_y=-247.44):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=152.69, default_y=-212.44):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='5', width=933.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(146.49)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', default_y=3.89, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=81.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('earth')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('grant')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pro')
            with Note(default_x=81.21, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', default_y=19.29, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=293.9, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('mise')
            with Note(default_x=293.9, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B‹', default_y=22.37, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=506.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('hope')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('true')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
            with Note(default_x=506.59, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=719.28, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_y=-59.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('con')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sal')
            with Note(default_x=719.28, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=81.21, default_y=-206.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=81.21, default_y=-196.49):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=293.9, default_y=-201.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=506.59, default_y=-216.49):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=506.59, default_y=-206.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=719.28, default_y=-216.49):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=719.28, default_y=-196.49):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=310.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(175.37)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=85.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_y=-102.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tri')
                with Lyric(number='3', default_y=-133.04, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹6', default_y=1.88, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=127.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', default_y=0.37, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=169.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B7', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=222.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=85.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('vails')
            with Note(default_x=126.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=234.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=275.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=85.01, default_y=-215.37):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.22, default_y=-205.37):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=169.43, default_y=-210.37):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=275.83, default_y=-215.37):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(8.0)
            with Note(default_x=85.01, default_y=-250.37):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.22, default_y=-260.37):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=169.43, default_y=-255.37):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=195.82, default_y=-250.37):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=222.2, default_y=-245.37):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=150.32):
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=16.87, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.86, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('me.')
                with Lyric(number='2', default_x=8.62, default_y=-102.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('tion.')
                with Lyric(number='3', default_x=8.97, default_y=-133.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('tion;')
            with Note(default_x=16.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=109.32, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('You')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
            with Note(default_x=109.32, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=16.87, default_y=-265.37):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=16.87, default_y=-220.37):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=109.32, default_y=-265.37):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=109.32, default_y=-230.37):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=284.97):
            with Direction(placement='above'):
                with DirectionType():
                    Words('B‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=31.63, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('will')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('by')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('make')
            with Note(default_x=31.63, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=94.57, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('not')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('us')
            with Note(default_x=94.57, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=157.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('see')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('death')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('keen')
            with Note(default_x=157.5, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=220.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='2', default_y=-102.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('u')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=220.43, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=31.63, default_y=-245.37):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=31.63, default_y=-225.37):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.57, default_y=-250.37):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.57, default_y=-215.37):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=157.5, default_y=-255.37):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=157.5, default_y=-210.37):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=220.43, default_y=-255.37):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=220.43, default_y=-220.37):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=188.08):
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=22.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-72.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', default_y=6.01, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹6', default_y=30.52, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=63.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', default_y=6.01, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=145.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ver')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('pon')
                with Lyric(number='3', default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('hear')
                    Extend()
            with Note(default_x=63.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=104.7, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=145.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.93, default_y=-235.37):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=22.93, default_y=-225.37):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=63.45, default_y=-230.37):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=63.45, default_y=-220.37):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=145.59, default_y=-235.37):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.59, default_y=-215.37):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=260.7):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(175.29)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=81.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.79, default_y=-72.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('thrown,')
                with Lyric(number='2', default_x=8.86, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('tree,')
                with Lyric(number='3', default_x=6.22, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('Word')
            with Note(default_x=81.21, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=209.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('when')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
            with Note(default_x=209.79, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=81.21, default_y=-255.29):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=81.21, default_y=-210.29):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=209.79, default_y=-255.29):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=209.79, default_y=-220.29):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='11', width=259.56):
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', default_y=14.42, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=20.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fol')
            with Note(default_x=20.14, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', default_y=15.65, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=79.6, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('end')
                    Text("tan's")
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('don')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('low')
            with Note(default_x=79.6, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B‹', default_y=15.65, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=139.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('host')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('our')
            with Note(default_x=139.05, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=198.51, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_y=-72.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('as')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vo')
            with Note(default_x=198.51, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=20.14, default_y=-235.29):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=20.14, default_y=-225.29):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=79.6, default_y=-230.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.05, default_y=-245.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.05, default_y=-235.29):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=198.51, default_y=-245.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=198.51, default_y=-225.29):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=263.65):
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', default_y=11.34, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=26.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_y=-102.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mis')
                with Lyric(number='3', default_y=-133.04, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ca')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹6', default_y=8.96, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=72.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', default_y=2.11, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=118.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B7', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=175.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('sails')
            with Note(default_x=71.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=187.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=229.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.06, default_y=-215.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=72.09, default_y=-205.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=118.11, default_y=-210.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=229.28, default_y=-215.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.06, default_y=-250.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.09, default_y=-260.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=118.11, default_y=-255.29):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=146.88, default_y=-250.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.65, default_y=-245.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='13', width=149.66):
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=17.08, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.86, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('me.')
                with Lyric(number='2', default_x=9.24, default_y=-102.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('sion.')
                with Lyric(number='3', default_x=8.8, default_y=-133.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('tion:')
            with Note(default_x=17.08, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=111.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-72.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('No')
                with Lyric(number='2', default_x=6.58, default_y=-102.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Be')
                with Lyric(number='3', default_x=6.58, default_y=-133.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('To')
            with Note(default_x=111.77, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.08, default_y=-265.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=17.08, default_y=-220.29):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=111.77, default_y=-230.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.77, default_y=-220.29):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=383.32):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(157.74)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', default_y=0.65, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=81.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('hu')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('fore')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('spend')
            with Note(default_x=81.21, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=155.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('man')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('our')
            with Note(default_x=155.34, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=229.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.75, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('strength,')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fa')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('lives')
            with Note(default_x=229.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=307.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('no')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('end')
                    Text("ther's")
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=307.59, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=81.21, default_y=-232.74):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=81.21, default_y=-197.74):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=155.34, default_y=-217.74):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=155.34, default_y=-207.74):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=229.46, default_y=-237.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=229.46, default_y=-202.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=307.59, default_y=-212.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=307.59, default_y=-202.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=272.71):
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=36.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('earth')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('throne')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('love')
            with Note(default_x=36.86, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E7', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=95.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
            with Note(default_x=95.42, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=153.98, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('power')
                with Lyric(number='2', default_x=9.24, default_y=-89.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('bove,')
                with Lyric(number='3', default_x=9.2, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('you,')
            with Note(default_x=153.98, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=212.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('can')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=212.55, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=36.86, default_y=-222.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=36.86, default_y=-212.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=95.42, default_y=-237.74):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=95.42, default_y=-212.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=153.98, default_y=-232.74):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=153.98, default_y=-197.74):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.55, default_y=-212.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.55, default_y=-202.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=277.54):
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', default_y=0.65, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=26.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('see')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('call')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('bear')
            with Note(default_x=26.24, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=88.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('each')
            with Note(default_x=88.66, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=151.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('thru')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('match')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('oth')
            with Note(default_x=151.09, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=213.52, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-59.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-89.15, relative_y=-30.0):
                    Syllabic('end')
                    Text('less')
                with Lyric(number='3', default_x=6.58, default_y=-119.24, relative_y=-30.0):
                    Syllabic('end')
                    Text("er's")
            with Note(default_x=213.52, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.24, default_y=-232.74):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=26.24, default_y=-197.74):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=88.66, default_y=-217.74):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=88.66, default_y=-207.74):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=151.09, default_y=-237.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=151.09, default_y=-202.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=213.52, default_y=-212.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=213.52, default_y=-202.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=933.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(154.84)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=81.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
                with Lyric(number='2', default_x=6.58, default_y=-93.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('deed')
                with Lyric(number='3', default_x=6.58, default_y=-123.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bur')
            with Note(default_x=81.21, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E7', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=317.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-63.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('vil')
                with Lyric(number='2', default_x=6.58, default_y=-93.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='3', default_x=6.58, default_y=-123.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('dens')
            with Note(default_x=317.53, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=553.5, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.78, default_y=-63.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('hour,')
                with Lyric(number='2', default_x=8.86, default_y=-93.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('love.')
                with Lyric(number='3', default_x=8.64, default_y=-123.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('too.')
            with Note(default_x=553.5, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=81.21, default_y=-219.84):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=81.21, default_y=-209.84):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=317.53, default_y=-234.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=317.53, default_y=-209.84):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=553.5, default_y=-229.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=553.5, default_y=-194.84):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=294.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(170.7)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=134.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('That')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
            with Note(default_x=134.87, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=187.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('you')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('he')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('then')
            with Note(default_x=187.58, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=240.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('may')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('at')
            with Note(default_x=240.3, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=134.87, default_y=-250.7):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=134.87, default_y=-205.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.58, default_y=-230.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.58, default_y=-210.7):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=240.3, default_y=-225.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=240.3, default_y=-215.7):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=341.2):
            with Direction(placement='above'):
                with DirectionType():
                    Words('B‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=25.71, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('lone')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('lift')
                with Lyric(number='3', default_x=9.46, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('last,')
            with Note(default_x=25.71, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=104.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('when')
            with Note(default_x=104.18, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=182.66, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('strength')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dread')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('death')
            with Note(default_x=182.66, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹6', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=261.13, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('ful')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('shall')
            with Note(default_x=261.13, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=25.71, default_y=-240.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=25.71, default_y=-220.7):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=104.18, default_y=-250.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=104.18, default_y=-225.7):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=182.66, default_y=-245.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=182.66, default_y=-225.7):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=261.13, default_y=-245.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=261.13, default_y=-225.7):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=132.72):
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=22.92, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.91, default_y=-75.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('new.')
                with Lyric(number='2', default_x=8.86, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('load.')
                with Lyric(number='3', default_x=8.97, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('loom,')
            with Note(default_x=22.92, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=101.17, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('I')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
            with Note(default_x=101.17, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.92, default_y=-260.7):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=22.92, default_y=-225.7):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=101.17, default_y=-235.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.17, default_y=-225.7):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=165.04):
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=22.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='3', default_y=-135.87, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sav')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A‹7', default_y=24.16, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=57.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D7', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=128.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-75.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
                with Lyric(number='3', default_x=6.58, default_y=-135.87, relative_y=-30.0):
                    Syllabic('end')
                    Text('ior')
            with Backup():
                Duration(8.0)
            with Note(default_x=22.93, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_y=-75.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('cry')
                    Extend()
                with Lyric(number='2', default_x=6.58, default_y=-105.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('Son')
            with Note(default_x=58.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=93.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=128.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.93, default_y=-235.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=22.93, default_y=-220.7):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.05, default_y=-240.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.05, default_y=-215.7):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=93.18, default_y=-245.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.18, default_y=-225.7):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.31, default_y=-245.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.31, default_y=-230.7):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='22', width=231.51):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(4.83)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(180.16)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=85.01, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.36, default_y=-64.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('you!')
                with Lyric(number='2', default_x=9.9, default_y=-94.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('God!')
                with Lyric(number='3', default_x=9.78, default_y=-124.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('come!')
            with Note(default_x=85.01, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=189.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-64.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('I')
                with Lyric(number='2', default_x=6.58, default_y=-94.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('I')
                with Lyric(number='3', default_x=6.58, default_y=-124.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
            with Backup():
                Duration(8.0)
            with Note(default_x=85.01, default_y=-260.16):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=85.01, default_y=-240.16):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=189.76, default_y=-225.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=189.76, default_y=-215.16):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=313.59):
            with Direction(placement='above'):
                with DirectionType():
                    Words('A7', default_y=12.4, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=24.98, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-64.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('trust')
                with Lyric(number='2', default_x=6.58, default_y=-94.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('plead')
                with Lyric(number='3', default_x=6.58, default_y=-124.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('bear')
            with Note(default_x=24.98, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B7', default_y=13.0, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=96.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-64.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                with Lyric(number='2', default_x=6.58, default_y=-94.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='3', default_x=6.58, default_y=-124.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Note(default_x=96.73, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', default_y=12.4, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=168.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-64.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lord')
                with Lyric(number='2', default_x=6.58, default_y=-94.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('grace')
                with Lyric(number='3', default_x=6.58, default_y=-124.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('loved')
            with Note(default_x=168.48, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', default_y=10.7, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=240.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-64.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='2', default_x=6.58, default_y=-94.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='3', default_x=6.58, default_y=-124.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('ones')
            with Note(default_x=240.23, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=13.12, default_y=-225.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=24.98, default_y=-220.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=96.73, default_y=-230.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=96.73, default_y=-220.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=168.48, default_y=-235.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=168.48, default_y=-215.16):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=240.23, default_y=-250.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=240.23, default_y=-225.16):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=260.39):
            with Direction(placement='above'):
                with DirectionType():
                    Words('A7', default_y=2.0, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_y=-64.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pro')
                with Lyric(number='2', default_y=-94.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('death')
                    Extend()
                with Lyric(number='3', default_y=-124.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('safe')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E‹', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=84.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F©7', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B7', default_y=23.81, relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=137.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='2', default_x=6.22, default_y=-94.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Backup():
                Duration(8.0)
            with Note(default_x=16.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=149.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=-5.64, default_y=-64.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('mise')
                with Lyric(number='3', default_x=-5.64, default_y=-124.84, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
            with Note(default_x=191.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.23, default_y=-225.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.66, default_y=-220.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=84.09, default_y=-215.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=137.58, default_y=-210.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=191.93, default_y=-215.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=225.36, default_y=-220.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.23, default_y=-245.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=84.09, default_y=-250.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=137.58, default_y=-255.16):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=191.93, default_y=-250.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=128.09):
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=20.0, font_family='Opus Chords Std', font_size='12.736')
                Staff(1)
            with Note(default_x=32.51, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.64, default_y=-64.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('true.')
                with Lyric(number='2', default_x=9.31, default_y=-94.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('stowed.')
                with Lyric(number='3', default_x=8.69, default_y=-124.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('home.')
            with Note(default_x=32.51, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=32.51, default_y=-270.16):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=32.51, default_y=-225.16):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')