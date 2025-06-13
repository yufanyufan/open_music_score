with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Five Minutes More')
    with Identification():
        Creator('Sammy Cahn', type='composer')
        Creator('Jule Styne', type='lyricist')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.4)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1510.27)
            PageWidth(1167.03)
            with PageMargins(type='even'):
                LeftMargin(54.054)
                RightMargin(54.054)
                TopMargin(54.054)
                BottomMargin(108.108)
            with PageMargins(type='odd'):
                LeftMargin(54.054)
                RightMargin(54.054)
                TopMargin(97.2971)
                BottomMargin(108.108)
        WordFont(font_family='MuseJazz Text', font_size='11')
        LyricFont(font_family='MuseJazz Text', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Five Minutes More', default_x=583.514, default_y=1412.97, justify='center', valign='top', font_size='28')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('arr. by Emma Nelson', default_x=583.514, default_y=1358.92, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('lyrics by Sammy Cahn', default_x=1112.97, default_y=1342.97, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('composed by Jule Styne', default_x=54.054, default_y=1342.97, justify='left', valign='bottom', font_size='12')
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
    with Part(id='P1'):
        with Measure(number='1', width=300.06):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(146.67)
            with Attributes():
                Divisions(6.0)
                with Key():
                    Fifths(-4)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=126.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.53, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dear,')
            with Note(default_x=169.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('this')
            with Note(default_x=212.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.26, default_y=-67.76, relative_x=-0.32, relative_y=-42.87):
                    Syllabic('begin')
                    Text('eve')
            with Note(default_x=255.51, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-44.78):
                    Syllabic('end')
                    Text('ning')
        with Measure(number='2', width=163.59):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('G')
                Kind('major')
            with Note(default_x=37.85, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.67, default_y=-67.76, relative_x=-1.91, relative_y=-46.05):
                    Syllabic('single')
                    Text('seemed')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=70.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.49, default_y=-67.76, relative_x=1.91, relative_y=-45.73):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=100.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('go')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=131.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
        with Measure(number='3', width=150.14):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=22.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-67.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('awf')
            with Note(default_x=74.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.59, default_y=-67.76, relative_y=-30.0):
                    Syllabic('end')
                    Text("'ly")
            with Note(default_x=107.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.44, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('fast.')
        with Measure(number='4', width=72.74):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=171.95):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=18.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('We')
            with Note(default_x=56.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('had')
            with Note(default_x=94.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
            with Note(default_x=132.5, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('much')
        with Measure(number='6', width=200.44):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('G')
                Kind('major')
            with Note(default_x=25.26, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=3.71, default_y=-67.76, relative_x=-2.87, relative_y=-44.78):
                    Syllabic('single')
                    Text('fun')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=68.62, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=5.31, default_y=-67.76, relative_x=-1.28, relative_y=-43.82):
                    Syllabic('single')
                    Text('and')
            with Note(default_x=111.98, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('now')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=155.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-67.76, relative_y=-30.0):
                    Syllabic('single')
                    Text("you're")
        with Measure(number='7', width=296.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(152.77)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=105.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('home')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('dominant-ninth', text='9')
            with Note(default_x=189.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('at')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Note(default_x=242.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.98, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('last.')
        with Measure(number='8', width=239.0):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
                Offset(6.0)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
                Offset(12.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=288.45):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('D')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=14.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('I')
            with Note(default_x=73.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('looked')
            with Note(default_x=133.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for')
            with Note(default_x=175.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ward')
            with Note(default_x=212.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=249.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
        with Measure(number='10', width=235.02):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=21.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('kiss')
            with Note(default_x=71.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('or')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('minor', text='m')
            with Note(default_x=121.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('two')
            with Note(default_x=171.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('at')
            with Note(default_x=202.28, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='11', width=1058.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Note(default_x=105.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-63.56, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gar')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=788.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.56, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=923.04, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.6, default_y=-63.56, relative_y=-30.0):
                    Syllabic('single')
                    Text('gate.')
        with Measure(number='12', width=254.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(282.54)
            with Note(default_x=109.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('diminished', text='dim')
            with Note(default_x=187.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('But')
            with Note(default_x=222.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('you')
        with Measure(number='13', width=202.49):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=23.91, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('gave')
            with Note(default_x=68.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('diminished', text='dim')
            with Note(default_x=112.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('just')
            with Note(default_x=156.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('one')
        with Measure(number='14', width=228.21):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=24.68, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('peck')
            with Note(default_x=61.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
            with Note(default_x=89.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('minor', text='m')
            with Note(default_x=135.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sis')
            with Note(default_x=180.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ted')
        with Measure(number='15', width=201.4):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('minor-seventh', text='m7')
            with Note(default_x=14.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('it')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=97.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=148.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.88, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('late.')
        with Measure(number='16', width=65.22):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='17', width=107.21):
            with Note(default_x=29.02, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=3.93, default_y=-63.52, relative_x=-2.65, relative_y=-43.97):
                    Syllabic('single')
                    Text('Give')
            with Note(default_x=67.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.02, default_y=-63.52, relative_x=3.43, relative_y=-42.94):
                    Syllabic('single')
                    Text('me')
        with Measure(number='18', width=332.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=133.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.83, default_y=-63.14, relative_x=0.61, relative_y=-41.96):
                    Syllabic('single')
                    Text('five')
            with Note(default_x=198.4, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=5.6, default_y=-63.14, relative_x=-0.98, relative_y=-45.89):
                    Syllabic('begin')
                    Text('min')
            with Note(default_x=227.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=14.93, default_y=-63.14, relative_x=8.34, relative_y=-46.87):
                    Syllabic('end')
                    Text('utes')
            with Note(default_x=274.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=16.53, default_y=-63.14, relative_x=7.8, relative_y=-45.4):
                    Syllabic('single')
                    Text('more,')
        with Measure(number='19', width=120.36):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=48.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('on')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('dominant', text='7')
            with Note(default_x=95.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
        with Measure(number='20', width=216.25):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('D')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=21.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('five')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=83.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('min')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('dominant', text='7')
            with Note(default_x=127.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('utes')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor', text='m')
            with Note(default_x=173.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.73, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('more.')
        with Measure(number='21', width=178.84):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=76.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
            with Note(default_x=104.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
            with Note(default_x=137.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.8, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('stay,')
        with Measure(number='22', width=210.54):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=14.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('let')
            with Note(default_x=135.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
            with Note(default_x=168.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.8, default_y=-63.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('stay,')
        with Measure(number='23', width=314.02):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(16.76)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=105.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant-ninth', text='9')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=198.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=226.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Note(default_x=269.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.73, default_y=-63.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('arms.')
        with Measure(number='24', width=66.91):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='25', width=135.27):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=74.73, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.13, default_y=-63.91, relative_x=-2.45, relative_y=-43.44):
                    Syllabic('single')
                    Text('Here')
            with Note(default_x=104.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('am')
        with Measure(number='26', width=176.16):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-63.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('I')
            with Note(default_x=69.37, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=4.62, default_y=-63.91, relative_x=-1.96, relative_y=-42.45):
                    Syllabic('begin')
                    Text('beg')
            with Note(default_x=98.28, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.53, default_y=-63.91, relative_x=2.94, relative_y=-41.96):
                    Syllabic('end')
                    Text('ging')
            with Note(default_x=139.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.55, default_y=-63.91, relative_x=1.96, relative_y=-43.44):
                    Syllabic('single')
                    Text('for')
        with Measure(number='27', width=128.47):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=53.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('on')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('dominant', text='7')
            with Note(default_x=100.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
        with Measure(number='28', width=238.09):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('D')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=21.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-63.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('five')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=94.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=4.68, default_y=-63.91, relative_x=-1.91, relative_y=-45.72):
                    Syllabic('begin')
                    Text('min')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('dominant', text='7')
            with Note(default_x=138.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.4, default_y=-63.91, relative_x=3.81, relative_y=-44.77):
                    Syllabic('end')
                    Text('utes')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor', text='m')
            with Note(default_x=191.26, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.64, default_y=-63.91, relative_x=1.91, relative_y=-45.87):
                    Syllabic('single')
                    Text('more,')
        with Measure(number='29', width=273.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(147.73)
            with Note(default_x=109.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=180.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('on')
            with Note(default_x=202.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
            with Note(default_x=238.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('five')
        with Measure(number='30', width=257.36):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=14.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=138.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('min')
            with Note(default_x=176.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('utes')
            with Note(default_x=217.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('more')
        with Measure(number='31', width=280.02):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=14.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant-ninth', text='9')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=136.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('of')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=174.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Note(default_x=226.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.67, default_y=-47.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('charms.')
        with Measure(number='32', width=117.04):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
                Offset(12.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='33', width=131.47):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('power', text='5', use_symbols='yes')
                Offset(12.0)
            with Note(default_x=14.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
        with Measure(number='34', width=270.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(147.73)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('D')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=105.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('All')
            with Note(default_x=146.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('week')
            with Note(default_x=187.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('long')
            with Note(default_x=228.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('I')
        with Measure(number='35', width=230.22):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('D')
                    RootAlter(-1.0)
                Kind('minor', text='m')
            with Note(default_x=40.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('dreamed')
            with Note(default_x=89.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
            with Note(default_x=120.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('end')
                    Text('bout')
            with Note(default_x=179.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('our')
        with Measure(number='36', width=219.77):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=58.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sat')
            with Note(default_x=112.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ur')
            with Note(default_x=142.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('end')
                    Text('day')
            with Note(default_x=178.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.59, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('date.')
        with Measure(number='37', width=103.52):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('half')
        with Measure(number='38', width=234.49):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('D')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=26.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text("Don't")
            with Note(default_x=78.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('you')
            with Note(default_x=129.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('know')
            with Note(default_x=181.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.09, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
        with Measure(number='39', width=293.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(147.73)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=105.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sun')
            with Note(default_x=152.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('day')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('dominant', text='7')
            with Note(default_x=198.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('morn')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('minor', text='m')
            with Note(default_x=245.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing')
        with Measure(number='40', width=266.47):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='tacet')
            with Note(default_x=72.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('you')
            with Note(default_x=143.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('can')
            with Note(default_x=180.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('sleep')
            with Note(default_x=219.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.88, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('late?')
        with Measure(number='41', width=138.94):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=14.5, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=73.91, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=3.64, default_y=-63.52, relative_x=-2.95, relative_y=-45.89):
                    Syllabic('single')
                    Text('Give')
            with Note(default_x=103.62, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.53, default_y=-63.52, relative_x=2.94, relative_y=-44.91):
                    Syllabic('single')
                    Text('me')
        with Measure(number='42', width=226.25):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=21.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('five')
            with Note(default_x=95.59, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=3.64, default_y=-63.52, relative_x=-2.95, relative_y=-44.42):
                    Syllabic('begin')
                    Text('min')
            with Note(default_x=129.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.51, default_y=-63.52, relative_x=3.93, relative_y=-43.44):
                    Syllabic('end')
                    Text('utes')
            with Note(default_x=183.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.73, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('more,')
        with Measure(number='43', width=133.78):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=57.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('on')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C')
                Kind('dominant', text='7')
            with Note(default_x=104.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
        with Measure(number='44', width=335.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(153.45)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('D')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=105.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('five')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('power', text='5', use_symbols='yes')
            with Note(default_x=187.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('begin')
                    Text('min')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('dominant', text='7')
            with Note(default_x=231.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('end')
                    Text('utes')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor', text='m')
            with Note(default_x=290.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.66, default_y=-62.23, relative_x=0.92, relative_y=-41.96):
                    Syllabic('single')
                    Text('more.')
        with Measure(number='45', width=213.42):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Note(default_x=101.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('Let')
            with Note(default_x=128.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
            with Note(default_x=171.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.8, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('stay,')
        with Measure(number='46', width=245.12):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=14.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=130.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('let')
            with Note(default_x=167.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
            with Note(default_x=203.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=8.8, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('stay,')
        with Measure(number='47', width=265.03):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=59.62)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=14.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant-ninth', text='9')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=138.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=177.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Note(default_x=220.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.73, default_y=-62.23, relative_y=-30.0):
                    Syllabic('single')
                    Text('arms.')
        with Measure(number='48', width=322.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(150.65)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
                Offset(6.0)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                Kind('minor-seventh', text='m7')
                Offset(12.0)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('G')
                Kind('major', parentheses_degrees='yes')
                with Degree():
                    DegreeValue(9)
                    DegreeAlter(-1.0)
                    DegreeType('add')
                Offset(18.0)
            with Note(default_x=105.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='49', width=122.14):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('half')
            with Note(default_x=48.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.13, default_y=-106.1, relative_x=-2.45, relative_y=-45.89):
                    Syllabic('single')
                    Text('Give')
            with Note(default_x=76.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-106.1, relative_y=-47.63):
                    Syllabic('single')
                    Text('me')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='50', width=165.41):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=60.58)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=98.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                with Lyric(number='1', default_x=1.18, default_y=-106.1, relative_x=-5.4, relative_y=-46.87):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=127.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                with Notations():
                    Tuplet(type='stop')
                with Lyric(number='1', default_x=7.07, default_y=-106.1, relative_x=0.49, relative_y=-45.89):
                    Syllabic('single')
                    Text('your')
        with Measure(number='51', width=223.47):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
                Offset(6.0)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
                Offset(12.0)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('F')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
                Offset(18.0)
            with Note(default_x=27.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=1.42, default_y=-106.1, relative_x=-1.85, relative_y=-43.93):
                    Syllabic('single')
                    Text('arms')
        with Measure(number='52', width=225.1):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('B')
                    RootAlter(-1.0)
                Kind('minor-seventh', text='m7')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant-ninth', text='9')
                Offset(6.0)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
                Offset(12.0)
            with Note(default_x=14.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=190.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-106.1, relative_y=-30.0):
                    Syllabic('single')
                    Text('five')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='53', width=619.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(184.92)
            with Note(default_x=105.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=169.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=233.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('min')
            with Note(default_x=297.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('utes')
            with Note(default_x=361.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('more')
            with Note(default_x=425.95, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
            with Note(default_x=490.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=9.93, default_y=-53.52, relative_x=3.34, relative_y=-42.01):
                    Syllabic('single')
                    Text('let')
            with Note(default_x=554.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('me')
        with Measure(number='54', width=439.16):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('E')
                    RootAlter(-1.0)
                Kind('dominant', text='7')
            with Note(default_x=24.49, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('stay')
            with Note(default_x=86.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=148.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('A')
                    RootAlter(-1.0)
                Kind('major')
            with Note(default_x=209.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('arms')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')