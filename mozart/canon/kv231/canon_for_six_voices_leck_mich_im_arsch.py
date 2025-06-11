with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('"Leck mich im Arsch!"')
    with Identification():
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://imslp.org/wiki/Special:ImagefromIndex/110254')
    with Defaults():
        with Scaling():
            Millimeters(7.112)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1670.0)
            PageWidth(1181.43)
            with PageMargins(type='even'):
                LeftMargin(56.243)
                RightMargin(56.243)
                TopMargin(56.243)
                BottomMargin(112.486)
            with PageMargins(type='odd'):
                LeftMargin(56.243)
                RightMargin(56.243)
                TopMargin(56.243)
                BottomMargin(112.486)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('KV 231: Kanon für sechs Stimmen', default_x=590.714, default_y=1613.76, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Ursprünglichen Text', default_x=590.714, default_y=1557.51, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('WOLFGANG AMADEUS MOZART', default_x=1125.19, default_y=1513.76, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('"Leck mich im Arsch!"', default_x=56.243, default_y=1513.76, justify='left', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Stimme')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Part_1')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(54)
                Volume(77.9528)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=152.27):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(82.22)
                        RightMargin(-0.0)
                    TopSystemDistance(173.62)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(1)
            with Direction(placement='above'):
                DirectionType()
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1.', enclosure='rectangle', default_y=13.8, font_weight='bold', font_family='Times New Roman', font_size='14')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Prestissimo ', default_x=-32.63, default_y=50.61, font_weight='bold', font_family='Times New Roman', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='yes', default_x=-32.63, default_y=50.61):
                        BeatUnit('quarter')
                        PerMinute('200')
                Sound(tempo=200.0)
            with Note(default_x=100.51, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Leck', font_family='Times New Roman')
        with Measure(number='2', width=75.06):
            with Note(default_x=23.53, default_y=-5.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich', font_family='Times New Roman')
        with Measure(number='3', width=55.09):
            with Note(default_x=15.32, default_y=-15.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('im', font_family='Times New Roman')
        with Measure(number='4', width=90.7):
            with Note(default_x=28.15, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=12.42, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Arsch!', font_family='Times New Roman')
        with Measure(number='5', width=80.48):
            with Direction(placement='above'):
                with DirectionType():
                    Words('2.', enclosure='rectangle', default_y=13.8, font_weight='bold', font_family='Times New Roman', font_size='14')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=42.09, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Laßt', font_family='Times New Roman')
        with Measure(number='6', width=74.09):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=40.47, default_y=-15.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman')
        with Measure(number='7', width=78.21):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=41.81, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh', font_family='Times New Roman')
        with Measure(number='8', width=82.56):
            with Note(default_x=12.36, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.51, default_y=0.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.81, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein!', font_family='Times New Roman')
        with Measure(number='9', width=104.44):
            with Direction(placement='above'):
                with DirectionType():
                    Words('3.', enclosure='rectangle', default_y=18.85, font_weight='bold', font_family='Times New Roman', font_size='14')
            with Note(default_x=23.71, default_y=0.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mur', font_family='Times New Roman')
            with Note(default_x=63.09, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ren', font_family='Times New Roman')
        with Measure(number='10', width=86.66):
            with Note(default_x=14.98, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman')
            with Note(default_x=49.84, default_y=-5.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver', font_family='Times New Roman')
        with Measure(number='11', width=107.16):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=60.5, default_y=-25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.84, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('bens!', font_family='Times New Roman')
        with Measure(number='12', width=195.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=124.59, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kur', font_family='Times New Roman')
            with Note(default_x=159.0, default_y=-15.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=4.92, default_y=-47.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('ren,', font_family='Times New Roman')
        with Measure(number='13', width=195.65):
            with Direction(placement='above'):
                with DirectionType():
                    Words('4.', enclosure='rectangle', default_y=13.8, font_weight='bold', font_family='Times New Roman', font_size='14')
            with Note(default_x=30.02, default_y=-20.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Brum', font_family='Times New Roman')
            with Note(default_x=77.08, default_y=-25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=2.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('men', font_family='Times New Roman')
            with Note(default_x=116.07, default_y=-30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman')
            with Note(default_x=155.06, default_y=-35.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver', font_family='Times New Roman')
        with Measure(number='14', width=172.85):
            with Note(default_x=15.14, default_y=-40.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=54.17, default_y=-40.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.81, default_y=-47.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('bens,', font_family='Times New Roman')
            with Note(default_x=93.2, default_y=-25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman')
            with Note(default_x=132.22, default_y=-20.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('das', font_family='Times New Roman')
        with Measure(number='15', width=185.71):
            with Note(default_x=23.47, default_y=-25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wah', font_family='Times New Roman')
            with Note(default_x=63.63, default_y=-30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=103.79, default_y=-35.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kreuz', font_family='Times New Roman')
            with Note(default_x=143.95, default_y=-40.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('de', font_family='Times New Roman')
        with Measure(number='16', width=319.34):
            with Note(default_x=16.53, default_y=-45.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le', font_family='Times New Roman')
            with Note(default_x=75.29, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.81, default_y=-47.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('bens,', font_family='Times New Roman')
            with Note(default_x=117.82, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('das', font_family='Times New Roman')
            with Note(default_x=160.51, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Brum', font_family='Times New Roman')
            with Note(default_x=207.57, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('men', font_family='Times New Roman')
            with Note(default_x=244.29, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman')
            with Note(default_x=281.01, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver', font_family='Times New Roman')
        with Measure(number='17', width=178.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5.', enclosure='rectangle', default_y=33.86, font_weight='bold', font_family='Times New Roman', font_size='14')
            with Note(default_x=86.21, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=111.09, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=135.61, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.17, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('bens,', font_family='Times New Roman')
        with Measure(number='18', width=287.74):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=62.96, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kur', font_family='Times New Roman')
            with Note(default_x=97.36, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=4.92, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('ren,', font_family='Times New Roman')
            with Note(default_x=144.18, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Brum', font_family='Times New Roman')
            with Note(default_x=191.23, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('men', font_family='Times New Roman')
            with Note(default_x=223.61, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman')
            with Note(default_x=254.87, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver', font_family='Times New Roman')
        with Measure(number='19', width=104.39):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=36.88, default_y=-15.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=61.4, default_y=-15.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.17, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('bens,', font_family='Times New Roman')
        with Measure(number='20', width=168.45):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=44.63, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver', font_family='Times New Roman')
            with Note(default_x=64.44, default_y=-5.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.25, default_y=0.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge', font_family='Times New Roman')
            with Note(default_x=104.06, default_y=5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.03, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.2, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('bens!', font_family='Times New Roman')
        with Measure(number='21', width=329.77):
            with Direction(placement='above'):
                with DirectionType():
                    Words('6.', enclosure='rectangle', relative_y=30.0, font_weight='bold', font_family='Times New Roman', font_size='14')
            with Note(default_x=30.62, default_y=-20.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('Drum', font_family='Times New Roman')
            with Note(default_x=93.26, default_y=15.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('laßt', font_family='Times New Roman')
            with Note(default_x=132.41, default_y=15.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman')
            with Note(default_x=171.56, default_y=15.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh', font_family='Times New Roman')
            with Note(default_x=210.71, default_y=15.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman')
            with Note(default_x=249.86, default_y=15.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('frö', font_family='Times New Roman')
            with Note(default_x=289.01, default_y=15.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.88, default_y=-46.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich,', font_family='Times New Roman')
        with Measure(number='22', width=333.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=86.21, default_y=15.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh', font_family='Times New Roman')
            with Note(default_x=154.57, default_y=-5.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=222.58, default_y=-5.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.81, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein!', font_family='Times New Roman')
        with Measure(number='23', width=455.01):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=105.67, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Laßt', font_family='Times New Roman')
            with Note(default_x=163.63, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman')
            with Note(default_x=221.58, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh', font_family='Times New Roman')
            with Note(default_x=279.54, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman')
            with Note(default_x=337.5, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fröh', font_family='Times New Roman')
            with Note(default_x=395.45, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.88, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich,', font_family='Times New Roman')
        with Measure(number='24', width=280.0):
            with Note(default_x=23.27, default_y=10.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh', font_family='Times New Roman')
            with Note(default_x=91.64, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=159.65, default_y=-10.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.81, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein!', font_family='Times New Roman')
            with Barline(location='right'):
                BarStyle('light-heavy')