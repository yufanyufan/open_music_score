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
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.25)
            PageWidth(1190.8)
            with PageMargins(type='even'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
            with PageMargins(type='odd'):
                LeftMargin(56.6894)
                RightMargin(56.6894)
                TopMargin(56.6894)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Là ci darem la mano', default_x=595.402, default_y=1626.56, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Wolfgang Amadeus Mozart', default_x=1134.12, default_y=1526.56, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Lorenzo da Ponte', default_x=56.6894, default_y=1526.56, justify='left', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Don Giovanni / Zerlina', default_x=595.402, default_y=1569.88, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with PartList():
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
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=359.84):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(108.59)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(3)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', default_x=-36.12, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12')
                Sound(tempo=54.0)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='2', width=171.23):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='3', width=285.06):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='4', width=152.71):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='5', width=270.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(94.03)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='6', width=133.88):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='7', width=183.71):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='8', width=116.31):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vor', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.53, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ach,', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='9', width=170.68):
            with Note(default_x=19.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.84, default_y=-44.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('rei,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=63.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('e', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=99.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=136.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vor', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='10', width=130.12):
            with Note(default_x=17.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.7, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wa', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=46.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-44.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('i,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=7.15, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen?', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=91.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.7, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mein', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='11', width=275.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(94.03)
            with Note(default_x=98.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.76, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=159.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma un', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('o', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=200.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('po', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('sag', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=237.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('co il', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='12', width=152.34):
            with Note(default_x=18.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('cor', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.3, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir!', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=45.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
            with Note(default_x=117.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fe', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='13', width=182.83):
            with Note(default_x=18.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('li', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=71.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ce, è', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('le', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=110.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ver', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('froh', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=147.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='14', width=159.17):
            with Note(default_x=25.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('rei', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schla', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=63.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='2', default_x=2.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=124.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='15', width=234.9):
            with Note(default_x=21.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('steh', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=45.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=70.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('può', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=106.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bur', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=134.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zit', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=173.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.6, relative_y=-30.0):
                    Syllabic('single')
                    Text('ternd', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=207.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='16', width=245.51):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    TopSystemDistance(31.6)
            with Note(default_x=98.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=8.82, default_y=-51.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('cor,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.64, default_y=-77.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('hier,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=119.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=141.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma', font_family='Times New Roman', font_size='9.99937')
                    Extend()
            with Note(default_x=209.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='2', default_x=6.58, default_y=-77.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='17', width=213.61):
            with Note(default_x=21.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('può', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('steh', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=44.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=67.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bur', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=91.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zit', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=152.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-51.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('ternd', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=186.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-51.15, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='18', width=132.94):
            with Note(default_x=20.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.22, default_y=-51.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('cor!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.64, default_y=-77.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('hier.', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='19', width=263.63):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='20', width=149.14):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.15, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ma', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='21', width=271.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(96.6)
            with Note(default_x=110.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('fà', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('set', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=128.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=164.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('tà', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_y=-77.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wür', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=200.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=228.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ma', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('de', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=246.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=167.63):
            with Note(default_x=19.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('set', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ster', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=51.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-51.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('to!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=4.95, default_y=-77.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=232.4):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='24', width=134.92):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=92.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Pre', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kaum', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='25', width=198.28):
            with Note(default_x=17.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=40.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-51.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('kann', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=78.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-51.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=110.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('son', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=128.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('più', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-77.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=173.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='26', width=345.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(96.6)
            with Note(default_x=102.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stre', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=127.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=153.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=8.57, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.55, default_y=-79.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=198.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('kaum', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=237.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('son', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=263.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=292.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('più', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=317.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=262.68):
            with Note(default_x=19.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stre', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=45.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=8.57, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.55, default_y=-79.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=115.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('kaum', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=155.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('son', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=181.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=209.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('più', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=235.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=177.73):
            with Note(default_x=19.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-53.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-79.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stre', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=57.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.57, default_y=-53.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('te.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.55, default_y=-79.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben.', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=218.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='30', width=308.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    TopSystemDistance(31.2)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='31', width=141.2):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=102.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vor', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.53, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ach,', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='32', width=172.34):
            with Note(default_x=19.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.84, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rei,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=64.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('e', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=100.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('wohl', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=137.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vor', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='33', width=128.52):
            with Note(default_x=17.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wa', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=46.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.8, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('i,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=7.15, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen?', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='34', width=254.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='35', width=186.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(92.41)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=147.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mein', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='36', width=198.71):
            with Note(default_x=24.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tre', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.76, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herz,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=63.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('ma', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=95.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('un', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('o', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=122.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('po', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('sag', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=154.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('co', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=173.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('il', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='37', width=243.61):
            with Note(default_x=18.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('cor;', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.3, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='38', width=114.48):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=43.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('mà', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ich', font_family='Times New Roman', font_size='9.99937')
                    Extend()
        with Measure(number='39', width=261.3):
            with Note(default_x=16.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('può', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ste', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=96.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('bur', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('he', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=123.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=2.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zit', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=140.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=158.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=175.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=200.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=2.58, default_y=-82.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('ternd', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=233.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-56.8, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='40', width=333.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(92.41)
            with Note(default_x=102.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.82, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('cor.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.64, default_y=-71.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('hier.', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=273.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ma', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='41', width=198.49):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('fà', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('set', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=38.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=60.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('to', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=81.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('tà', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wür', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=124.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=152.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ma', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('de', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=173.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='42', width=247.0):
            with Note(default_x=29.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('set', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ster', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=73.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.8, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('to;', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.95, default_y=-71.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=190.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('pre', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_y=-71.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kaum', font_family='Times New Roman', font_size='9.99937')
                    Extend()
        with Measure(number='43', width=225.58):
            with Note(default_x=17.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=54.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('kann', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=93.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=125.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('son', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=148.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=176.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('più', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=200.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='44', width=324.99):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    TopSystemDistance(31.2)
            with Note(default_x=98.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stre', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=119.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=141.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=8.57, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.55, default_y=-80.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=186.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('kaum', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=225.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('son', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=256.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=278.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('più', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=300.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='45', width=243.19):
            with Note(default_x=19.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stre', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=40.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=62.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=8.57, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('te,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.55, default_y=-80.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=107.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('kaum', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=146.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('son', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=168.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=196.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('più', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=218.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='46', width=145.42):
            with Note(default_x=19.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('stre', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=37.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=56.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.77, default_y=-54.3, relative_y=-30.0):
                    Syllabic('single')
                    Text('te;', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.95, default_y=-80.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='47', width=143.37):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='48', width=147.86):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=107.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-54.3, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-80.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wohl', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='49', width=187.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(-0.0)
                    SystemDistance(94.48)
            with Note(default_x=102.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.19, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-75.96):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=123.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        BreathMark(None)
            with Note(default_x=152.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('middle')
                    Text('An', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('So', font_family='Times New Roman')
        with Measure(number='50', width=188.34):
            with Attributes():
                with Time():
                    Beats('6')
                    BeatType('8')
            with Direction(placement='above'):
                with DirectionType():
                    Words('.', default_x=-27.3, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12')
                Sound(tempo=108.0)
            with Note(default_x=32.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-50.05, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=74.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=113.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('end')
                    Text('diam', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-75.96):
                    Syllabic('begin')
                    Text('oh', font_family='Times New Roman')
            with Note(default_x=154.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='51', width=172.18):
            with Note(default_x=21.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=54.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.0, default_y=-50.05):
                    Syllabic('end')
                    Text('ne,', font_family='Times New Roman')
                with Lyric(number='2', default_x=2.58, default_y=-75.96):
                    Syllabic('single')
                    Text('len', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=102.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='52', width=157.51):
            with Note(default_x=23.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ri', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=60.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ent', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=87.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=1.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('rar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=125.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('le', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gen', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='53', width=161.78):
            with Note(default_x=14.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pe', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=39.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.0, default_y=-50.05):
                    Syllabic('end')
                    Text('ne,', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-75.96):
                    Syllabic('single')
                    Text('len', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=88.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'un", font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='54', width=137.86):
            with Note(default_x=13.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=71.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.05):
                    Syllabic('middle')
                    Text('no', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96):
                    Syllabic('single')
                    Text('lig', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=92.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=113.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='55', width=236.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(94.48)
            with Note(default_x=98.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cen', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=166.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te  a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='56', width=185.99):
            with Note(default_x=21.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.88, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('mor.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='57', width=186.89):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=156.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('So', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='58', width=200.47):
            with Note(default_x=25.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=77.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=114.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('oh', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=167.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='59', width=194.6):
            with Note(default_x=21.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=55.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=6.58, default_y=-50.05):
                    Syllabic('end')
                    Text('ne', font_family='Times New Roman')
                with Lyric(number='2', default_x=2.58, default_y=-75.96):
                    Syllabic('end')
                    Text('len', font_family='Times New Roman')
            with Note(default_x=110.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=163.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='60', width=233.92):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    TopSystemDistance(31.6)
            with Note(default_x=98.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ri', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=136.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ent', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=163.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=1.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('rar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=201.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('le', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gen', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='61', width=174.02):
            with Note(default_x=14.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pe', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=40.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.0, default_y=-50.05):
                    Syllabic('end')
                    Text('ne,', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-75.96):
                    Syllabic('end')
                    Text('len', font_family='Times New Roman')
            with Note(default_x=90.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=139.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'un", font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='62', width=138.72):
            with Note(default_x=13.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=72.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-50.05):
                    Syllabic('middle')
                    Text('no', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96):
                    Syllabic('end')
                    Text('lig', font_family='Times New Roman')
            with Note(default_x=92.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=113.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='63', width=139.12):
            with Note(default_x=21.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cen', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=77.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.05, relative_y=-30.0):
                    Syllabic('middle')
                    Text('te  a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-75.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='64', width=144.89):
            with Note(default_x=21.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.88, default_y=-50.05, relative_y=-30.0):
                    Syllabic('end')
                    Text('mor.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-75.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='65', width=174.16):
            with Note():
                Rest()
                Duration(72.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='66', width=237.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(96.57)
            with Note():
                Rest()
                Duration(72.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='67', width=143.33):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=76.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wohl', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='68', width=158.49):
            with Note(default_x=25.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.19, default_y=-45.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-70.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='69', width=157.19):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=88.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.05, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wohl', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='70', width=164.65):
            with Note(default_x=25.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.19, default_y=-45.05, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-70.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='71', width=143.33):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='72', width=252.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    SystemDistance(96.57)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=221.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('So', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='73', width=184.6):
            with Note(default_x=25.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=68.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=106.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.51, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('bene,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=150.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.77, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('len,', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='74', width=182.45):
            with Note(default_x=25.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=8.79, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=61.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('len', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=149.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('le', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='75', width=170.15):
            with Note(default_x=14.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pe', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=58.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('lig', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=93.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ri', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=137.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='76', width=215.39):
            with Note(default_x=16.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('rar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.75, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=119.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.25, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'un", font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-73.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='77', width=268.37):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(72.6)
                        RightMargin(0.0)
                    TopSystemDistance(30.8)
            with Note(default_x=98.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_y=-74.97, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=130.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-74.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('lig', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=178.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ce', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-74.97):
                    Syllabic('end')
                    Text('sein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=210.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.06, relative_y=-30.0):
                    Syllabic('middle')
                    Text('te', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=235.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-74.97, relative_y=-30.0):
                    Syllabic('end')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='78', width=133.12):
            with Note(default_x=21.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.28, default_y=-49.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('mor!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-74.97, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='79', width=149.08):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='80', width=124.0):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='81', width=169.92):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='82', width=160.35):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=359.84):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(44.4)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(3)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=119.39, default_y=-84.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('Là', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Reich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=175.06, default_y=-84.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('ci', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=209.85, default_y=-79.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('die', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=246.9, default_y=-74.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('rem', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.73, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Hand,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=302.57, default_y=-84.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('la', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='2', width=171.23):
            with Note(default_x=17.42, default_y=-94.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=55.47, default_y=-79.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.78, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('no,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.55, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben,', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='3', width=285.06):
            with Note(default_x=31.02, default_y=-89.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('là', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=85.92, default_y=-89.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=120.24, default_y=-89.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=173.64, default_y=-84.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55):
                    Syllabic('single')
                    Text('rai', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schloss', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=228.55, default_y=-79.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('di', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='4', width=152.71):
            with Note(default_x=18.9, default_y=-99.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('sì;', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.3, default_y=-68.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=270.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.4)
            with Note(default_x=98.21, default_y=-130.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ve', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kannst', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=140.01, default_y=-130.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=8.8, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('di,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('du', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=175.03, default_y=-125.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('non', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('noch', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=208.03, default_y=-120.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('è', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wi', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=235.76, default_y=-130.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lon', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='6', width=133.88):
            with Note(default_x=20.42, default_y=-140.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ta', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.46):
                    Syllabic('middle')
                    Text('stre', font_family='Times New Roman')
            with Note(default_x=55.3, default_y=-125.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman')
                with Lyric(number='2', default_x=7.3, default_y=-70.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben?', font_family='Times New Roman')
            with Note(default_x=99.5, default_y=-130.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='7', width=183.71):
            with Note(default_x=23.19, default_y=-130.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=8.61, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('tiam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=44.0, default_y=-135.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.81, default_y=-140.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=83.31, default_y=-145.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.81, default_y=-145.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.83, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('weit', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=140.45, default_y=-140.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('da', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('von', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=158.95, default_y=-135.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=116.31):
            with Note(default_x=20.96, default_y=-130.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.8, default_y=-44.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.64, default_y=-70.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('hier.', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=170.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='10', width=130.12):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='11', width=275.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.4)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='12', width=152.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='13', width=182.83):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='14', width=159.17):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='15', width=234.9):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='16', width=245.51):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.06)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='17', width=213.61):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='18', width=132.94):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='19', width=263.63):
            with Note(default_x=23.22, default_y=-131.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=72.64, default_y=-141.06):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=8.8, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=111.63, default_y=-151.06):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('um', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=150.83, default_y=-126.06):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('bel', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('sonst', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=200.25, default_y=-116.06):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=231.14, default_y=-126.06):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=149.14):
            with Note(default_x=20.42, default_y=-131.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.81, relative_y=-30.0):
                    Syllabic('middle')
                    Text('let', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wer', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=69.02, default_y=-141.06):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.72, default_y=-131.06):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-45.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('to!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=4.89, default_y=-71.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
        with Measure(number='21', width=271.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(103.1)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='22', width=167.63):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='23', width=232.4):
            with Note(default_x=29.42, default_y=-138.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('Io', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('Glück', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=71.21, default_y=-148.1):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=106.01, default_y=-158.1):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=144.01, default_y=-133.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('rò', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('stets', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=182.18, default_y=-123.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tu', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('um', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=206.95, default_y=-133.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='24', width=134.92):
            with Note(default_x=17.22, default_y=-138.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.84, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sor', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=54.14, default_y=-148.1):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.78, default_y=-138.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.57, default_y=-45.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('te.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=4.95, default_y=-71.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
        with Measure(number='25', width=198.28):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='26', width=345.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(98.69)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='27', width=262.68):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='28', width=177.73):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=95.03, default_y=-133.69):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.81, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=138.23, default_y=-143.69):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.8, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('o', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='29', width=218.94):
            with Note(default_x=31.02, default_y=-123.69):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('vie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=119.06, default_y=-133.69):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.2, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('doch!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
        with Measure(number='30', width=308.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.71)
            with Note(default_x=102.01, default_y=-125.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Là', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Reich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=146.25, default_y=-125.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ci', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=175.85, default_y=-120.71):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('die', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=212.91, default_y=-115.71):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rem', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.73, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Hand,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=262.25, default_y=-125.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('la', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='31', width=141.2):
            with Note(default_x=17.42, default_y=-135.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ma', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=47.85, default_y=-120.71):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.78, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('no,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.95, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='32', width=172.34):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='33', width=128.52):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='34', width=254.68):
            with Note(default_x=33.02, default_y=-125.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('là', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=75.95, default_y=-125.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mi', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=109.95, default_y=-120.71):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=163.35, default_y=-115.71):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rai', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Schloss', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=210.15, default_y=-125.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('di', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='35', width=186.74):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(103.53)
            with Note(default_x=99.15, default_y=-128.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('sì;', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.1, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir;', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='36', width=198.71):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='37', width=243.61):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
            with Note(default_x=43.17, default_y=-143.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=77.74, default_y=-143.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Lyric(number='1', default_x=4.61, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('tiam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=123.36, default_y=-138.53):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=164.36, default_y=-133.53):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=8.83, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('weit', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=203.19, default_y=-143.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('da', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('von', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='38', width=114.48):
            with Note(default_x=20.96, default_y=-128.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.2, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('qui!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.64, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('hier.', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='39', width=261.3):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='40', width=333.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(102.53)
            with Note(default_x=102.01, default_y=-132.53):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Vie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=149.48, default_y=-142.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=8.8, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('ni,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=188.48, default_y=-157.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('um', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=227.68, default_y=-127.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('bel', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('sonst', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=295.78, default_y=-147.53):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='41', width=198.49):
            with Note(default_x=17.23, default_y=-142.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('begin')
                    Text('let', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wer', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=60.01, default_y=-142.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=9.0, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('to!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.95, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='42', width=247.0):
            with Note(default_x=29.42, default_y=-132.53):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('io', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('Glück', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=73.57, default_y=-142.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('begin')
                    Text('can', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=108.37, default_y=-157.53):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gie', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=146.37, default_y=-127.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('rò', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('stets', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=212.6, default_y=-147.53):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('tua', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('um', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='43', width=225.58):
            with Note(default_x=17.22, default_y=-142.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.83, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sor', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-71.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=54.85, default_y=-142.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=8.57, default_y=-45.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('te.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.95, default_y=-71.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='44', width=324.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(99.21)
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='45', width=243.19):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
        with Measure(number='46', width=145.42):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=114.59, default_y=-124.21):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('O', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='47', width=143.37):
            with Note(default_x=30.97, default_y=-124.21):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.63, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=58.67, default_y=-144.21):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=114.07, default_y=-119.21):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('o', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='48', width=147.86):
            with Note(default_x=30.97, default_y=-119.21):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=9.19, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.03, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm!', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=55.94, default_y=-139.21):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='49', width=187.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.31)
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=152.78, default_y=-180.31):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('An', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('So', font_family='Times New Roman')
        with Measure(number='50', width=188.34):
            with Attributes():
                with Time():
                    Beats('6')
                    BeatType('8')
            with Note(default_x=32.3, default_y=-150.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=74.03, default_y=-155.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=113.23, default_y=-150.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('oh', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=154.96, default_y=-145.31):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='51', width=172.18):
            with Note(default_x=21.82, default_y=-155.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=54.21, default_y=-165.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.4, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne,', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('len', font_family='Times New Roman', font_size='9.99937')
                    Extend()
            with Note(default_x=102.63, default_y=-165.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.4, default_y=-155.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='52', width=157.51):
            with Note(default_x=23.02, default_y=-150.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ri', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=60.67, default_y=-155.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ent', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=87.67, default_y=-150.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=1.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=125.33, default_y=-145.31):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('le', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gen', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='53', width=161.78):
            with Note(default_x=14.62, default_y=-155.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pe', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=39.82, default_y=-165.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('len', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=88.23, default_y=-165.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.0, default_y=-155.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'un", font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='54', width=137.86):
            with Note(default_x=13.02, default_y=-150.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=71.17, default_y=-145.31):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lig', font_family='Times New Roman', font_size='9.99937')
                    Extend()
            with Note(default_x=92.13, default_y=-135.31):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=113.1, default_y=-145.31):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='55', width=236.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(101.78)
            with Note(default_x=98.21, default_y=-141.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cen', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=166.56, default_y=-146.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('te  a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='56', width=185.99):
            with Note(default_x=21.12, default_y=-141.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.88, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mor.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='57', width=186.89):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=156.51, default_y=-146.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('So', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='58', width=200.47):
            with Note(default_x=25.01, default_y=-141.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=77.45, default_y=-146.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=114.64, default_y=-141.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('oh', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=167.09, default_y=-136.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='59', width=194.6):
            with Note(default_x=21.82, default_y=-146.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=55.21, default_y=-156.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.4, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne,', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('len', font_family='Times New Roman', font_size='9.99937')
                    Extend()
            with Note(default_x=110.77, default_y=-156.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=163.82, default_y=-146.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='60', width=233.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(105.78)
            with Note(default_x=98.57, default_y=-145.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ri', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lust', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=136.66, default_y=-150.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ent', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=163.66, default_y=-145.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=1.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=201.74, default_y=-140.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('le', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gen', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='61', width=174.02):
            with Note(default_x=14.62, default_y=-150.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pe', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=40.82, default_y=-160.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=9.0, default_y=-40.0):
                    Syllabic('end')
                    Text('ne,', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-65.91):
                    Syllabic('end')
                    Text('len', font_family='Times New Roman')
            with Note(default_x=90.77, default_y=-160.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=139.24, default_y=-150.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'un", font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='62', width=138.72):
            with Note(default_x=13.02, default_y=-145.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=72.02, default_y=-140.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('no', font_family='Times New Roman', font_size='9.99937')
                    Extend()
                with Lyric(number='2', default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lig', font_family='Times New Roman', font_size='9.99937')
                    Extend()
            with Note(default_x=92.99, default_y=-130.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=113.95, default_y=-140.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='63', width=139.12):
            with Note(default_x=21.02, default_y=-145.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cen', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=77.02, default_y=-150.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('to  a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='64', width=144.89):
            with Note(default_x=21.12, default_y=-145.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.88, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mor.', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='65', width=174.16):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=92.08, default_y=-145.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('O', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='66', width=237.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.76)
            with Note(default_x=98.21, default_y=-111.76):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.19, default_y=-41.35, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.03, default_y=-67.26, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='67', width=143.33):
            with Note():
                Rest()
                Duration(72.0)
                Voice('1')
                Type('half')
                Dot()
        with Measure(number='68', width=158.49):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='69', width=157.19):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='70', width=164.65):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='71', width=143.33):
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=76.11, default_y=-141.76):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.35, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-67.26, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wohl', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='72', width=252.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.98)
            with Note(default_x=99.15, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.19, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=221.86, default_y=-137.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('An', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('So', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='73', width=184.6):
            with Note(default_x=25.01, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=68.59, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mio', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=106.66, default_y=-152.98):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.51, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('bene,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=150.24, default_y=-152.98):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.77, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('len,', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='74', width=182.45):
            with Note(default_x=25.01, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=8.79, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('diam,', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=61.01, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('len', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=149.27, default_y=-137.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('le', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='75', width=170.15):
            with Note(default_x=14.62, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pe', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=58.19, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lig', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=93.99, default_y=-152.98):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ri', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=137.57, default_y=-152.98):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sto', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='76', width=215.39):
            with Note(default_x=16.42, default_y=-147.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('rar', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=8.75, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=119.53, default_y=-137.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text("d'un", font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ja', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='77', width=268.37):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(108.08)
            with Note(default_x=98.21, default_y=-148.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_y=-65.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('se', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=130.02, default_y=-143.08):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.19, default_y=-148.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('no', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lig', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=178.58, default_y=-153.08):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cen', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91):
                    Syllabic('single')
                    Text('sein', font_family='Times New Roman')
            with Note(default_x=210.39, default_y=-158.08):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('te', font_family='Times New Roman', font_size='9.99937')
            with Note(default_x=235.79, default_y=-153.08):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=6.58, default_y=-65.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('fort', font_family='Times New Roman', font_size='9.99937')
        with Measure(number='78', width=133.12):
            with Note(default_x=21.12, default_y=-148.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.28, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mor!', font_family='Times New Roman', font_size='9.99937')
                with Lyric(number='2', default_x=9.15, default_y=-65.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('an!', font_family='Times New Roman', font_size='9.99937')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
        with Measure(number='79', width=149.08):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='80', width=124.0):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='81', width=169.92):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
        with Measure(number='82', width=160.35):
            with Note():
                Rest(measure='yes')
                Duration(72.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=359.84):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(103.67)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(3)
                with Time():
                    Beats('2')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=175.06, default_y=-278.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=175.06, default_y=-268.07):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=175.06, default_y=-253.07):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=302.57, default_y=-278.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=302.57, default_y=-268.07):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=302.57, default_y=-253.07):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=119.39, default_y=-363.07):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=246.9, default_y=-363.07):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='2', width=171.23):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.47, default_y=-273.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.47, default_y=-263.07):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.47, default_y=-248.07):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=131.58, default_y=-283.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=131.58, default_y=-263.07):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=131.58, default_y=-253.07):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.42, default_y=-348.07):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=93.52, default_y=-348.07):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='3', width=285.06):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=85.92, default_y=-283.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=85.92, default_y=-268.07):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=85.92, default_y=-258.07):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=228.55, default_y=-288.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=228.55, default_y=-273.07):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=228.55, default_y=-263.07):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=31.02, default_y=-343.07):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=173.64, default_y=-358.07):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='4', width=152.71):
            with Note(default_x=18.9, default_y=-293.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=18.9, default_y=-268.07):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.95, default_y=-248.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=51.95, default_y=-238.07):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=63.82, default_y=-233.07):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=85.0, default_y=-253.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.0, default_y=-243.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.0, default_y=-233.07):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=118.06, default_y=-258.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.06, default_y=-248.07):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=118.06, default_y=-233.07):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.9, default_y=-378.07):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.95, default_y=-333.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=85.0, default_y=-328.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=118.06, default_y=-323.07):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=270.13):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(111.25)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=98.21, default_y=-306.66):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.21, default_y=-296.66):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=98.21, default_y=-286.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=140.01, default_y=-331.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=140.01, default_y=-321.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=140.01, default_y=-306.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=235.76, default_y=-331.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=235.76, default_y=-321.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=235.76, default_y=-306.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.21, default_y=-381.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=208.03, default_y=-416.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='6', width=133.88):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.3, default_y=-326.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.3, default_y=-316.66):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.3, default_y=-301.66):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=99.5, default_y=-326.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=99.5, default_y=-316.66):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=99.5, default_y=-306.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.42, default_y=-401.66):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=80.89, default_y=-396.66):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='7', width=183.71):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=64.81, default_y=-336.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=64.81, default_y=-326.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=76.68, default_y=-321.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=64.81, default_y=-311.66):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=140.45, default_y=-336.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=140.45, default_y=-326.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=152.32, default_y=-321.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=140.45, default_y=-311.66):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=23.19, default_y=-396.66):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=101.81, default_y=-396.66):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='8', width=116.31):
            with Note(default_x=20.96, default_y=-341.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=20.96, default_y=-331.66):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=20.96, default_y=-321.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=20.96, default_y=-306.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=38.79, default_y=-321.66):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=38.79, default_y=-286.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=59.76, default_y=-316.66):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=59.76, default_y=-291.66):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.59, default_y=-311.66):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=77.59, default_y=-301.66):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.96, default_y=-416.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.79, default_y=-371.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=59.76, default_y=-376.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=77.59, default_y=-396.66):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=170.68):
            with Note(default_x=19.22, default_y=-306.66):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=19.22, default_y=-296.66):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=46.14, default_y=-331.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=46.14, default_y=-321.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=46.14, default_y=-306.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=136.3, default_y=-331.66):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=136.3, default_y=-321.66):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=136.3, default_y=-306.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.22, default_y=-416.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=99.1, default_y=-416.66):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='10', width=130.12):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=46.25, default_y=-336.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=46.25, default_y=-316.66):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=46.25, default_y=-301.66):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=91.14, default_y=-336.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=91.14, default_y=-316.66):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=91.14, default_y=-306.66):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.02, default_y=-401.66):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=72.41, default_y=-401.66):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='11', width=275.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(35.0)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=135.11, default_y=-260.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=135.11, default_y=-245.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=135.11, default_y=-235.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=237.21, default_y=-265.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=237.21, default_y=-250.4):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=237.21, default_y=-240.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.33, default_y=-320.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=200.44, default_y=-335.4):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='12', width=152.34):
            with Note(default_x=18.9, default_y=-245.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.32, default_y=-225.4):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=45.32, default_y=-215.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=57.19, default_y=-210.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=74.35, default_y=-230.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=74.35, default_y=-220.4):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=74.35, default_y=-210.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=100.77, default_y=-235.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=100.77, default_y=-225.4):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=100.77, default_y=-210.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.9, default_y=-355.4):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.32, default_y=-310.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=74.35, default_y=-305.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=100.77, default_y=-300.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=182.83):
            with Note(default_x=18.62, default_y=-230.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=18.62, default_y=-220.4):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=18.62, default_y=-210.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.13, default_y=-255.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=51.13, default_y=-245.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.13, default_y=-230.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=147.65, default_y=-255.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=147.65, default_y=-245.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=147.65, default_y=-230.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.62, default_y=-305.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=110.05, default_y=-340.4):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='14', width=159.17):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=63.41, default_y=-260.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=63.41, default_y=-240.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=63.41, default_y=-225.4):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=124.8, default_y=-260.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=124.8, default_y=-240.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=124.8, default_y=-230.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=25.42, default_y=-325.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=94.11, default_y=-325.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='15', width=234.9):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=70.07, default_y=-260.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=70.07, default_y=-250.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=70.07, default_y=-235.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=173.72, default_y=-260.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=173.72, default_y=-250.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=173.72, default_y=-235.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=21.02, default_y=-320.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=134.47, default_y=-320.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='16', width=245.51):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(102.33)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=141.15, default_y=-338.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=141.15, default_y=-318.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=141.15, default_y=-303.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=209.66, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=209.66, default_y=-298.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=209.66, default_y=-288.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.33, default_y=-403.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=175.4, default_y=-418.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='17', width=213.61):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=67.95, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=67.95, default_y=-303.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=67.95, default_y=-293.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=152.43, default_y=-323.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=164.3, default_y=-318.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=152.43, default_y=-308.39):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=21.02, default_y=-413.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=114.88, default_y=-393.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='18', width=132.94):
            with Note(default_x=20.96, default_y=-328.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=20.96, default_y=-318.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=20.96, default_y=-303.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=48.55, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=48.55, default_y=-303.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=48.55, default_y=-293.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=76.15, default_y=-328.39):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=76.15, default_y=-318.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=76.15, default_y=-303.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.96, default_y=-413.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=48.55, default_y=-378.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=76.15, default_y=-413.39):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='19', width=263.63):
            with Note(default_x=23.22, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=23.22, default_y=-308.39):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=23.22, default_y=-298.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=72.64, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=150.83, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=150.83, default_y=-303.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=150.83, default_y=-293.39):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=200.25, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=23.22, default_y=-393.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=150.83, default_y=-393.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='20', width=149.14):
            with Note(default_x=20.42, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=20.42, default_y=-308.39):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=20.42, default_y=-298.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=50.33, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=87.72, default_y=-318.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=87.72, default_y=-308.39):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=117.63, default_y=-308.39):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=117.63, default_y=-298.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.42, default_y=-393.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.33, default_y=-393.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=87.72, default_y=-393.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='21', width=271.6):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(104.5)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=110.61, default_y=-342.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=110.61, default_y=-322.6):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=110.61, default_y=-307.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=228.83, default_y=-342.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=228.83, default_y=-322.6):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=228.83, default_y=-312.6):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=110.25, default_y=-407.6):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=167.63):
            with Note(default_x=19.42, default_y=-342.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=19.42, default_y=-327.6):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=19.42, default_y=-317.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.85, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=51.85, default_y=-317.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=69.02, default_y=-322.6):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=69.02, default_y=-312.6):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=86.18, default_y=-317.6):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=86.18, default_y=-307.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=103.35, default_y=-322.6):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=103.35, default_y=-312.6):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=120.51, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.51, default_y=-317.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=142.86, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.42, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.85, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=120.51, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='23', width=232.4):
            with Note(default_x=29.42, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.42, default_y=-317.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=29.42, default_y=-307.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=71.21, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=144.01, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=144.01, default_y=-312.6):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=144.01, default_y=-302.6):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=182.18, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=29.42, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=144.01, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='24', width=134.92):
            with Note(default_x=17.22, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=17.22, default_y=-317.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=17.22, default_y=-307.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=36.97, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.78, default_y=-327.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=72.78, default_y=-317.6):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=92.53, default_y=-317.6):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=92.53, default_y=-307.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.22, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.97, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=72.78, default_y=-402.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='25', width=198.28):
            with Note(default_x=17.95, default_y=-342.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.95, default_y=-322.6):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.95, default_y=-307.6):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=156.35, default_y=-342.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=156.35, default_y=-322.6):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=156.35, default_y=-312.6):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.59, default_y=-407.6):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=345.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(103.71)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=102.01, default_y=-337.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.01, default_y=-322.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.01, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=237.99, default_y=-337.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=237.99, default_y=-317.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=237.99, default_y=-307.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=102.01, default_y=-397.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=237.99, default_y=-402.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=262.68):
            with Note(default_x=19.22, default_y=-337.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=19.22, default_y=-322.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=19.22, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=155.19, default_y=-337.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=155.19, default_y=-317.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=155.19, default_y=-307.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.22, default_y=-397.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=155.19, default_y=-402.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=177.73):
            with Note(default_x=19.22, default_y=-337.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=19.22, default_y=-322.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=19.22, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=57.12, default_y=-337.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=57.12, default_y=-322.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=57.12, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=95.03, default_y=-322.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.03, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=138.23, default_y=-312.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=138.23, default_y=-302.4):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.22, default_y=-397.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=95.03, default_y=-397.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='29', width=218.94):
            with Note(default_x=31.02, default_y=-302.4):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=31.02, default_y=-292.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=67.56, default_y=-297.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=67.56, default_y=-287.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=84.73, default_y=-302.4):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=84.73, default_y=-292.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=101.89, default_y=-307.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=101.89, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=119.06, default_y=-312.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.06, default_y=-302.4):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=143.63, default_y=-317.4):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.63, default_y=-292.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=168.2, default_y=-322.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.2, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=192.77, default_y=-327.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.77, default_y=-302.4):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=31.02, default_y=-397.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=119.06, default_y=-397.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='30', width=308.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(106.69)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=102.01, default_y=-322.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.01, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.25, default_y=-322.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=146.25, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.25, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=262.25, default_y=-322.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=262.25, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=262.25, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=102.01, default_y=-407.4):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=212.91, default_y=-407.4):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='31', width=141.2):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=47.85, default_y=-327.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=47.85, default_y=-307.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=47.85, default_y=-292.4):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=102.48, default_y=-327.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=102.48, default_y=-307.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=102.48, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.42, default_y=-392.4):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=75.17, default_y=-392.4):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='32', width=172.34):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=47.37, default_y=-327.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=47.37, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=47.37, default_y=-302.4):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=137.96, default_y=-332.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.96, default_y=-317.4):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=137.96, default_y=-307.4):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.22, default_y=-387.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=100.77, default_y=-402.4):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='33', width=128.52):
            with Note(default_x=17.02, default_y=-312.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.25, default_y=-292.4):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=46.25, default_y=-282.4):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=58.12, default_y=-277.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=75.28, default_y=-297.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=75.28, default_y=-287.4):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=75.28, default_y=-277.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=101.1, default_y=-302.4):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=101.1, default_y=-292.4):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=101.1, default_y=-277.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.02, default_y=-422.4):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='34', width=254.68):
            with Note(default_x=33.02, default_y=-297.4):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.02, default_y=-287.4):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=33.02, default_y=-277.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=75.95, default_y=-322.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.95, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=75.95, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=210.15, default_y=-322.4):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=210.15, default_y=-312.4):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=210.15, default_y=-297.4):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=33.02, default_y=-407.4):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=163.35, default_y=-372.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='35', width=186.74):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(103.91)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=99.15, default_y=-332.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=99.15, default_y=-312.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=99.15, default_y=-297.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=99.15, default_y=-397.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='36', width=198.71):
            with Note(default_x=24.44, default_y=-342.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=24.44, default_y=-332.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=24.44, default_y=-317.44):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=122.36, default_y=-342.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=122.36, default_y=-332.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=122.36, default_y=-317.44):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(48.0)
            with Note(default_x=24.44, default_y=-402.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=122.36, default_y=-402.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='37', width=243.61):
            with Note(default_x=18.9, default_y=-337.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=18.9, default_y=-327.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=18.9, default_y=-312.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.74, default_y=-337.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=77.74, default_y=-327.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.74, default_y=-312.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=203.19, default_y=-337.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=203.19, default_y=-327.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=203.19, default_y=-312.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.9, default_y=-422.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=164.36, default_y=-387.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='38', width=114.48):
            with Note(default_x=20.96, default_y=-332.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=20.96, default_y=-312.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=20.96, default_y=-297.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=66.79, default_y=-332.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=66.79, default_y=-307.44):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=89.71, default_y=-337.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=89.71, default_y=-312.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.96, default_y=-397.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='39', width=261.3):
            with Note(default_x=15.8, default_y=-342.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-332.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-317.44):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.8, default_y=-402.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='40', width=333.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(112.11)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=102.01, default_y=-344.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.01, default_y=-319.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=126.78, default_y=-344.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.78, default_y=-334.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=126.78, default_y=-319.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=188.48, default_y=-334.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=188.48, default_y=-319.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=227.68, default_y=-339.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.68, default_y=-324.64):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=250.38, default_y=-339.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=250.38, default_y=-324.64):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=295.78, default_y=-334.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=295.78, default_y=-324.64):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=295.78, default_y=-314.64):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=102.01, default_y=-394.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.78, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.48, default_y=-384.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.48, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=227.68, default_y=-389.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=250.38, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.08, default_y=-379.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.78, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=198.49):
            with Note(default_x=17.23, default_y=-334.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-319.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=60.01, default_y=-319.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=60.01, default_y=-299.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=152.34, default_y=-314.64):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=152.34, default_y=-304.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.23, default_y=-384.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=102.78, default_y=-399.64):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='42', width=247.0):
            with Note(default_x=29.42, default_y=-319.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.42, default_y=-309.64):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=51.49, default_y=-319.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=51.49, default_y=-309.64):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=108.37, default_y=-334.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=108.37, default_y=-319.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=146.37, default_y=-339.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.37, default_y=-324.64):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=168.44, default_y=-339.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=168.44, default_y=-324.64):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=212.6, default_y=-334.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=212.6, default_y=-324.64):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=212.6, default_y=-314.64):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=29.42, default_y=-394.64):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.49, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.57, default_y=-384.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.37, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.37, default_y=-389.64):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.44, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.52, default_y=-379.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.6, default_y=-409.64):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=225.58):
            with Note(default_x=17.22, default_y=-334.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=17.22, default_y=-319.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=125.25, default_y=-334.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=125.25, default_y=-314.64):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=125.25, default_y=-304.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.22, default_y=-384.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=125.25, default_y=-399.64):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='44', width=324.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.46)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=98.21, default_y=-308.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=98.21, default_y=-293.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=98.21, default_y=-283.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=225.6, default_y=-318.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=225.6, default_y=-298.67):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=225.6, default_y=-288.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=98.21, default_y=-368.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=225.6, default_y=-378.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='45', width=243.19):
            with Note(default_x=19.22, default_y=-318.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=19.22, default_y=-303.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=19.22, default_y=-293.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=146.82, default_y=-328.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.82, default_y=-308.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.82, default_y=-298.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.22, default_y=-378.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=146.82, default_y=-393.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='46', width=145.42):
            with Note(default_x=19.22, default_y=-328.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=19.22, default_y=-313.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=19.22, default_y=-303.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=56.12, default_y=-328.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=56.12, default_y=-313.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=56.12, default_y=-303.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=85.35, default_y=-303.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=85.35, default_y=-278.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.22, default_y=-388.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=56.12, default_y=-388.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=85.35, default_y=-398.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='47', width=143.37):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=58.67, default_y=-323.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=58.67, default_y=-308.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=58.67, default_y=-298.67):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=86.37, default_y=-298.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=86.37, default_y=-273.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=58.67, default_y=-383.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=86.37, default_y=-393.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='48', width=147.86):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.94, default_y=-318.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.94, default_y=-303.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.94, default_y=-293.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=82.71, default_y=-293.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=82.71, default_y=-268.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=55.94, default_y=-378.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=82.71, default_y=-388.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='49', width=187.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.71)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=102.01, default_y=-353.03):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=102.01, default_y=-343.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=152.78, default_y=-328.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=102.01, default_y=-438.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=102.01, default_y=-413.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='50', width=188.34):
            with Attributes():
                with Time():
                    Beats('6')
                    BeatType('8')
            with Note(default_x=32.3, default_y=-323.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.3, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=53.17, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=74.03, default_y=-328.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=74.03, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=113.23, default_y=-323.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.23, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=134.1, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=154.96, default_y=-318.03):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=154.96, default_y=-308.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=31.94, default_y=-433.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='51', width=172.18):
            with Note(default_x=21.82, default_y=-328.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=21.82, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=54.21, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=54.21, default_y=-328.03):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=73.6, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.46, default_y=-333.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=73.6, default_y=-323.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=102.63, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.63, default_y=-328.03):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=102.63, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=122.01, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=122.01, default_y=-323.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=122.01, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=141.4, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.4, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=141.4, default_y=-308.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.46, default_y=-433.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='52', width=157.51):
            with Note(default_x=23.02, default_y=-323.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=23.02, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=41.85, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.67, default_y=-328.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=60.67, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=87.67, default_y=-323.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=87.67, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=106.5, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.33, default_y=-318.03):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=125.33, default_y=-308.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=22.66, default_y=-433.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='53', width=161.78):
            with Note(default_x=14.62, default_y=-328.03):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=14.62, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=39.82, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=39.82, default_y=-328.03):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=59.2, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=71.06, default_y=-333.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=59.2, default_y=-323.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=88.23, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=88.23, default_y=-328.03):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=88.23, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=107.61, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.61, default_y=-323.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=107.61, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=127.0, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.0, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=127.0, default_y=-308.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.26, default_y=-433.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='54', width=137.86):
            with Note(default_x=13.02, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=13.02, default_y=-323.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=13.02, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=32.4, default_y=-313.03):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=32.4, default_y=-303.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.78, default_y=-338.03):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=51.78, default_y=-323.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.78, default_y=-313.03):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=71.17, default_y=-333.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=71.17, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=71.17, default_y=-308.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=92.13, default_y=-308.03):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.13, default_y=-298.03):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.1, default_y=-333.03):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=113.1, default_y=-318.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.1, default_y=-308.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.02, default_y=-433.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=71.17, default_y=-418.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='55', width=236.88):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(104.57)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=98.21, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.21, default_y=-311.34):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=98.21, default_y=-301.34):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=120.99, default_y=-301.34):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.99, default_y=-291.34):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=143.77, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=143.77, default_y=-311.34):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=143.77, default_y=-301.34):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=166.56, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=166.56, default_y=-316.34):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=166.56, default_y=-306.34):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=189.34, default_y=-306.34):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=189.34, default_y=-296.34):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=212.12, default_y=-331.34):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=212.12, default_y=-316.34):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=212.12, default_y=-306.34):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=98.21, default_y=-401.34):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=166.56, default_y=-436.34):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='56', width=185.99):
            with Note(default_x=21.12, default_y=-336.34):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=21.12, default_y=-326.34):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=21.12, default_y=-311.34):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=48.14, default_y=-301.34):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=48.14, default_y=-276.34):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=75.16, default_y=-301.34):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=75.16, default_y=-276.34):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=102.19, default_y=-291.34):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=102.19, default_y=-281.34):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=129.21, default_y=-306.34):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.21, default_y=-291.34):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=157.37, default_y=-301.34):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=157.37, default_y=-281.34):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=20.76, default_y=-421.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='57', width=186.89):
            with Note(default_x=12.94, default_y=-296.34):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.94, default_y=-286.34):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=44.33, default_y=-311.34):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=44.33, default_y=-296.34):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=76.93, default_y=-311.34):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=76.93, default_y=-286.34):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=103.46, default_y=-316.34):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.46, default_y=-291.34):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=129.98, default_y=-316.34):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.98, default_y=-306.34):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=156.51, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=156.51, default_y=-296.34):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.58, default_y=-421.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='58', width=200.47):
            with Note(default_x=25.01, default_y=-311.34):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=25.01, default_y=-301.34):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.23, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=77.45, default_y=-316.34):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=77.45, default_y=-306.34):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=114.64, default_y=-311.34):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=114.64, default_y=-301.34):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=140.86, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.09, default_y=-306.34):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.09, default_y=-296.34):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=24.65, default_y=-421.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='59', width=194.6):
            with Note(default_x=21.82, default_y=-316.34):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=21.82, default_y=-306.34):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=55.21, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.21, default_y=-316.34):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=81.74, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=93.6, default_y=-321.34):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=81.74, default_y=-311.34):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=110.77, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=110.77, default_y=-316.34):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=110.77, default_y=-306.34):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.29, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.29, default_y=-311.34):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=137.29, default_y=-301.34):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=163.82, default_y=-326.34):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=163.82, default_y=-306.34):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=163.82, default_y=-296.34):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.46, default_y=-421.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='60', width=233.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.71)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=98.57, default_y=-318.49):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.57, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=117.62, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=136.66, default_y=-323.49):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=136.66, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=163.66, default_y=-318.49):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=163.66, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=182.7, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.74, default_y=-313.49):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=201.74, default_y=-303.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=98.21, default_y=-428.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='61', width=174.02):
            with Note(default_x=14.62, default_y=-323.49):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=14.62, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=40.82, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=40.82, default_y=-323.49):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=61.73, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=73.6, default_y=-328.49):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=61.73, default_y=-318.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=90.77, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.77, default_y=-323.49):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=90.77, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=118.32, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=118.32, default_y=-318.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=118.32, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=139.24, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=139.24, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=139.24, default_y=-303.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.62, default_y=-428.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=90.77, default_y=-428.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=118.32, default_y=-428.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='62', width=138.72):
            with Note(default_x=13.02, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=13.02, default_y=-318.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=13.02, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=32.68, default_y=-308.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=32.68, default_y=-298.49):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=52.35, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=52.35, default_y=-318.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=52.35, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=72.02, default_y=-328.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=72.02, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=72.02, default_y=-303.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=92.99, default_y=-303.49):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.99, default_y=-293.49):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.95, default_y=-328.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=113.95, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.95, default_y=-303.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=13.02, default_y=-428.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=72.02, default_y=-413.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='63', width=139.12):
            with Note(default_x=21.02, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=21.02, default_y=-318.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=21.02, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=39.68, default_y=-308.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=39.68, default_y=-298.49):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=58.35, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=58.35, default_y=-318.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=58.35, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.02, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=77.02, default_y=-323.49):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.02, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=95.68, default_y=-313.49):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.68, default_y=-303.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=114.35, default_y=-333.49):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=114.35, default_y=-323.49):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=114.35, default_y=-313.49):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.02, default_y=-408.49):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=77.02, default_y=-443.49):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='64', width=144.89):
            with Note(default_x=21.12, default_y=-343.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=21.12, default_y=-333.49):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=21.12, default_y=-318.49):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=49.57, default_y=-308.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=77.73, default_y=-323.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=77.73, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=102.96, default_y=-313.49):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=120.12, default_y=-323.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=120.12, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.12, default_y=-428.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=77.73, default_y=-393.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.12, default_y=-393.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='65', width=174.16):
            with Note(default_x=15.8, default_y=-328.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-303.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=44.55, default_y=-298.49):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=61.71, default_y=-328.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=61.71, default_y=-303.49):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=92.08, default_y=-318.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.82, default_y=-313.49):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=148.99, default_y=-323.49):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=148.99, default_y=-308.49):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=15.8, default_y=-378.49):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.71, default_y=-378.49):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=92.08, default_y=-393.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=148.99, default_y=-393.49):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='66', width=237.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(103.31)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=98.21, default_y=-305.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=98.21, default_y=-280.07):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=153.56, default_y=-280.07):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.73, default_y=-285.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=187.89, default_y=-290.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=205.06, default_y=-295.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=98.21, default_y=-355.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='67', width=143.33):
            with Note(default_x=12.94, default_y=-295.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.94, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=38.22, default_y=-290.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=38.22, default_y=-280.07):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=55.38, default_y=-295.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=55.38, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=76.11, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=76.11, default_y=-290.07):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=101.39, default_y=-305.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=101.39, default_y=-295.07):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=118.56, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.56, default_y=-290.07):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.58, default_y=-385.07):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='68', width=158.49):
            with Note(default_x=25.01, default_y=-295.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=25.01, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=63.19, default_y=-285.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=91.36, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=91.36, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=116.55, default_y=-290.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=133.72, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=133.72, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=25.01, default_y=-370.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=91.36, default_y=-370.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=133.72, default_y=-370.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='69', width=157.19):
            with Note(default_x=15.8, default_y=-305.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-280.07):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=42.86, default_y=-275.07):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=60.03, default_y=-305.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=60.03, default_y=-280.07):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=88.19, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=88.19, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=115.26, default_y=-290.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=132.42, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=132.42, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=15.8, default_y=-355.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.03, default_y=-355.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=88.19, default_y=-370.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=132.42, default_y=-370.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='70', width=164.65):
            with Note(default_x=25.01, default_y=-305.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=25.01, default_y=-280.07):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(default_x=80.36, default_y=-280.07):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.52, default_y=-285.07):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=114.69, default_y=-290.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=131.85, default_y=-295.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=25.01, default_y=-355.07):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='71', width=143.33):
            with Note(default_x=12.94, default_y=-295.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.94, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=38.22, default_y=-290.07):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=38.22, default_y=-280.07):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=55.38, default_y=-295.07):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=55.38, default_y=-285.07):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=76.11, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=76.11, default_y=-290.07):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=101.39, default_y=-305.07):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=101.39, default_y=-295.07):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=118.56, default_y=-300.07):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.56, default_y=-290.07):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.94, default_y=-385.07):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=76.11, default_y=-385.07):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='72', width=252.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.91)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=99.15, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=99.15, default_y=-299.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(default_x=150.77, default_y=-294.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=167.93, default_y=-299.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=185.1, default_y=-304.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=202.26, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=99.15, default_y=-384.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='73', width=184.6):
            with Note(default_x=25.01, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=25.01, default_y=-299.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=51.42, default_y=-304.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=51.42, default_y=-294.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=68.59, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=68.59, default_y=-299.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=106.66, default_y=-314.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=106.66, default_y=-304.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=133.07, default_y=-319.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=133.07, default_y=-309.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=150.24, default_y=-314.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=150.24, default_y=-304.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=25.01, default_y=-399.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=106.66, default_y=-399.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='74', width=182.45):
            with Note(default_x=25.01, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=25.01, default_y=-299.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=78.18, default_y=-294.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.34, default_y=-299.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=112.51, default_y=-304.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=129.68, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=25.01, default_y=-384.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Staff(2)
        with Measure(number='75', width=170.15):
            with Note(default_x=14.62, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=14.62, default_y=-299.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=41.03, default_y=-304.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=41.03, default_y=-294.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=58.19, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=58.19, default_y=-299.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.99, default_y=-314.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=93.99, default_y=-304.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=120.4, default_y=-319.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=120.4, default_y=-309.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=137.57, default_y=-314.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=137.57, default_y=-304.89):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=14.62, default_y=-399.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=93.99, default_y=-399.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='76', width=215.39):
            with Note(default_x=16.42, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=16.42, default_y=-299.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=68.03, default_y=-294.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.2, default_y=-299.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=102.36, default_y=-304.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=119.53, default_y=-309.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(72.0)
            with Note(default_x=16.42, default_y=-384.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=156.29, default_y=-384.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.45, default_y=-389.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=190.62, default_y=-394.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='77', width=268.37):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.71)
                with StaffLayout(number=2):
                    StaffDistance(60.0)
            with Note(default_x=98.21, default_y=-306.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=98.21, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=130.02, default_y=-301.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=130.02, default_y=-291.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=147.19, default_y=-306.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=147.19, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=178.58, default_y=-311.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=178.58, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=210.39, default_y=-316.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=210.39, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=235.79, default_y=-311.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=235.79, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=98.21, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=147.19, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=178.58, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=235.79, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='78', width=133.12):
            with Note(default_x=21.12, default_y=-306.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.12, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=65.99, default_y=-311.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=65.99, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=91.19, default_y=-316.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=91.19, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=108.35, default_y=-311.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=108.35, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=21.12, default_y=-416.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=65.99, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='79', width=149.08):
            with Note(default_x=12.0, default_y=-306.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=39.65, default_y=-301.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=39.65, default_y=-291.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=56.82, default_y=-306.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=56.82, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=79.49, default_y=-311.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=79.49, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=107.14, default_y=-316.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=107.14, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=124.31, default_y=-311.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=124.31, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-381.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=79.49, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='80', width=124.0):
            with Note(default_x=12.0, default_y=-306.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=56.87, default_y=-321.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=56.87, default_y=-311.78):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=56.87, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=82.07, default_y=-316.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=82.07, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=99.23, default_y=-321.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=99.23, default_y=-311.78):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=99.23, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-416.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=56.87, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=99.23, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='81', width=169.92):
            with Note(default_x=12.0, default_y=-321.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=12.0, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=45.51, default_y=-301.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=45.51, default_y=-291.78):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=62.68, default_y=-321.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=62.68, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=62.68, default_y=-296.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=90.16, default_y=-321.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.16, default_y=-311.78):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=90.16, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=123.67, default_y=-316.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=123.67, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=140.84, default_y=-326.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=140.84, default_y=-311.78):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=140.84, default_y=-301.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=12.0, default_y=-381.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.68, default_y=-381.78):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=90.16, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=140.84, default_y=-396.78):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='82', width=160.35):
            with Note(default_x=15.8, default_y=-331.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-321.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-306.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(72.0)
            with Note(default_x=15.8, default_y=-416.78):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')