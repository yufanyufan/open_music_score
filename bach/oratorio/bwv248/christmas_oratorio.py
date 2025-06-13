with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('BACH_CHRISTMAS_ORATORIO_12_B03')
    with Identification():
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
            Millimeters(6.0014)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1979.04)
            PageWidth(1400.06)
            with PageMargins(type='even'):
                LeftMargin(66.6512)
                RightMargin(66.6512)
                TopMargin(66.6512)
                BottomMargin(133.302)
            with PageMargins(type='odd'):
                LeftMargin(66.6512)
                RightMargin(66.6512)
                TopMargin(66.6512)
                BottomMargin(133.302)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Times New Roman', font_size='9.8327')
    with Credit(page=1):
        CreditType('title')
        CreditWords('BACH_CHRISTMAS_ORATORIO_12_B03', default_x=700.03, default_y=1912.39, justify='center', valign='top', font_size='24')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano (2)')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Piano (2)')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Piano (2) (2)')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Piano (2)')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=178.41):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(94.24)
                        RightMargin(0.0)
                    TopSystemDistance(193.49)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(1)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Editor:  John Henry Fowler', relative_y=20.0, font_weight='bold', font_style='italic', font_family='Times New Roman', font_size='12.2244')
            with Direction(placement='above'):
                with DirectionType():
                    Words('( Revision:  11 - 6 - 2008 )', default_y=25.22, relative_y=20.0, font_weight='bold', font_style='italic', font_family='Times New Roman', font_size='6.2451')
            with Note(default_x=107.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
        with Measure(number='2', width=268.85):
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-46.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
            with Note(default_x=77.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Christmas Oratorio', default_y=22.87, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='20.064')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cantata No 2 - No 12 - Choral', default_y=56.09, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='12.2244')
            with Note(default_x=140.52, default_y=-20.0):
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
                with Lyric(number='1', default_y=-46.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schö')
            with Note(default_x=172.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=203.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
        with Measure(number='3', width=266.03):
            with Note(default_x=20.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=87.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
            with Note(default_x=142.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-46.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
            with Note(default_x=196.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='4', width=276.86):
            with Note(default_x=18.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
            with Note(default_x=82.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Johann Sebastian Bach', relative_y=20.0, font_weight='bold', font_style='italic', font_family='Times New Roman', font_size='12.2244')
            with Note(default_x=146.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Direction(placement='above'):
                with DirectionType():
                    Words('( 1685 - 1750 )', default_y=26.16, relative_y=20.0, font_weight='bold', font_style='italic', font_family='Times New Roman', font_size='8.2382')
            with Note(default_x=210.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
        with Measure(number='5', width=182.37):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=14.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.62, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
            with Note(default_x=114.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.84, default_y=-46.62, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen !')
        with Measure(number='6', width=166.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.17)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=107.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
        with Measure(number='7', width=298.31):
            with Attributes():
                with Time(print_object='no'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hir')
            with Note(default_x=85.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=155.86, default_y=-20.0):
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
                with Lyric(number='1', default_y=-48.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('volk,')
                    Extend()
            with Note(default_x=191.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=226.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='8', width=317.12):
            with Note(default_x=23.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schre')
            with Note(default_x=104.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('cken')
            with Note(default_x=169.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.71, default_y=-48.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=234.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil')
        with Measure(number='9', width=278.78):
            with Note(default_x=14.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Note(default_x=79.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
            with Note(default_x=145.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=211.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('gel')
        with Measure(number='10', width=200.05):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=14.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-48.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=122.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-48.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=166.57):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.17)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=103.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
        with Measure(number='12', width=279.9):
            with Note(default_x=15.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=84.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
            with Note(default_x=153.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=222.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='13', width=266.68):
            with Note(default_x=19.64, default_y=-20.0):
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
                with Lyric(number='1', default_y=-49.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=51.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=148.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=200.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
        with Measure(number='14', width=293.2):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=83.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note(default_x=152.7, default_y=-15.0):
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
                with Lyric(number='1', default_y=-49.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
                    Extend()
            with Note(default_x=187.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=222.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='15', width=254.23):
            with Note(default_x=21.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=85.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=136.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.78, default_y=-49.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein.')
            with Note(default_x=188.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='16', width=371.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.17)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=81.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=153.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=225.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=297.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
        with Measure(number='17', width=308.09):
            with Note(default_x=16.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=169.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=230.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='18', width=333.84):
            with Note(default_x=20.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=98.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=176.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=254.38, default_y=-20.0):
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
                with Lyric(number='1', default_y=-46.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                    Extend()
            with Note(default_x=293.31, default_y=-15.0):
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
        with Measure(number='19', width=247.32):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=14.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-46.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=175.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-46.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=178.41):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(70.25)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(1)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=107.32, default_y=-155.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
        with Measure(number='2', width=268.85):
            with Note(default_x=13.8, default_y=-150.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-53.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
            with Note(default_x=77.16, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Note(default_x=140.52, default_y=-155.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schö')
            with Note(default_x=172.21, default_y=-150.25):
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
            with Note(default_x=203.89, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
        with Measure(number='3', width=266.03):
            with Note(default_x=20.11, default_y=-150.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=54.04, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=87.98, default_y=-140.25):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
            with Note(default_x=142.27, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.79, default_y=-53.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
            with Note(default_x=196.56, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='4', width=276.86):
            with Note(default_x=18.0, default_y=-150.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
            with Note(default_x=82.31, default_y=-155.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=114.47, default_y=-150.25):
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
            with Note(default_x=146.63, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=210.94, default_y=-140.25):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
        with Measure(number='5', width=182.37):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-140.25):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
            with Note(default_x=59.14, default_y=-145.25):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.32, default_y=-155.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.84, default_y=-53.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen !')
        with Measure(number='6', width=166.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.45)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=107.32, default_y=-157.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
        with Measure(number='7', width=298.31):
            with Attributes():
                with Time(print_object='no'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-152.45):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hir')
            with Note(default_x=85.43, default_y=-147.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=155.86, default_y=-157.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('volk,')
                    Extend()
            with Note(default_x=191.07, default_y=-152.45):
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
            with Note(default_x=226.29, default_y=-147.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='8', width=317.12):
            with Note(default_x=23.87, default_y=-152.45):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schre')
            with Note(default_x=64.38, default_y=-147.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=104.89, default_y=-142.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('cken')
            with Note(default_x=169.7, default_y=-147.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-54.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=234.51, default_y=-147.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil')
        with Measure(number='9', width=278.78):
            with Note(default_x=14.23, default_y=-152.45):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Note(default_x=79.97, default_y=-157.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                    Extend()
            with Note(default_x=112.84, default_y=-152.45):
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
            with Note(default_x=145.7, default_y=-147.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=211.44, default_y=-142.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('gel')
        with Measure(number='10', width=200.05):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-142.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=62.86, default_y=-147.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.68, default_y=-157.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-54.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=166.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(72.91)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=103.52, default_y=-147.91):
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
                with Lyric(number='1', default_y=-54.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                    Extend()
            with Note(default_x=134.25, default_y=-142.91):
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
        with Measure(number='12', width=279.9):
            with Note(default_x=15.17, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=119.04, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
            with Note(default_x=153.66, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.31, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=188.28, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=222.9, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='13', width=266.68):
            with Note(default_x=19.64, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=84.23, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=148.82, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=200.49, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
                    Extend()
            with Note(default_x=232.79, default_y=-157.91):
                with Pitch():
                    Step('D')
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
        with Measure(number='14', width=293.2):
            with Note(default_x=13.8, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=83.25, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note(default_x=152.7, default_y=-152.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
                    Extend()
            with Note(default_x=187.43, default_y=-147.91):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=222.15, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-54.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=256.88, default_y=-147.91):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=254.23):
            with Note(default_x=21.29, default_y=-147.91):
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
                with Lyric(number='1', default_y=-54.31, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=53.42, default_y=-142.91):
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
            with Note(default_x=85.55, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=136.96, default_y=-142.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-54.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein.')
            with Note(default_x=188.37, default_y=-137.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-54.31, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='16', width=371.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.74)
            with Note(default_x=81.21, default_y=-146.74):
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
                with Lyric(number='1', default_y=-57.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                    Extend()
            with Note(default_x=117.28, default_y=-141.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=153.34, default_y=-136.74):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=225.48, default_y=-136.74):
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
                with Lyric(number='1', default_y=-57.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=261.54, default_y=-141.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=297.61, default_y=-141.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-57.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=333.68, default_y=-146.74):
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
        with Measure(number='17', width=308.09):
            with Note(default_x=16.87, default_y=-146.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-57.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=169.47, default_y=-151.74):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=230.37, default_y=-146.74):
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
                with Lyric(number='1', default_y=-57.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=268.43, default_y=-151.74):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=333.84):
            with Note(default_x=20.82, default_y=-156.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=98.67, default_y=-151.74):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=176.53, default_y=-146.74):
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
                with Lyric(number='1', default_y=-57.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=215.45, default_y=-141.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.38, default_y=-161.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='19', width=247.32):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-156.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-57.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=114.77, default_y=-161.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=175.74, default_y=-161.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-57.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=178.41):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(73.56)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(1)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=107.32, default_y=-278.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
        with Measure(number='2', width=268.85):
            with Note(default_x=13.8, default_y=-278.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.47, default_y=-73.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
                    Extend()
            with Note(default_x=45.48, default_y=-273.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=108.84, default_y=-268.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Note(default_x=140.52, default_y=-278.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-73.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schö')
            with Note(default_x=172.21, default_y=-283.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=203.89, default_y=-283.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
        with Measure(number='3', width=266.03):
            with Note(default_x=20.11, default_y=-283.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=87.98, default_y=-283.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.93, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
            with Note(default_x=142.27, default_y=-283.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.79, default_y=-73.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
            with Note(default_x=196.56, default_y=-278.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-73.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=230.5, default_y=-283.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=276.86):
            with Note(default_x=18.0, default_y=-288.81):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-73.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
                    Extend()
            with Note(default_x=50.15, default_y=-283.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=82.31, default_y=-278.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-73.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=114.47, default_y=-273.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.63, default_y=-268.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=210.94, default_y=-268.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-73.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
        with Measure(number='5', width=182.37):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-268.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-73.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
            with Note(default_x=86.73, default_y=-273.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.32, default_y=-278.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=11.84, default_y=-73.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen !')
        with Measure(number='6', width=166.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.12)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=107.32, default_y=-281.57):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-74.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
        with Measure(number='7', width=298.31):
            with Attributes():
                with Time(print_object='no'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-281.57):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-74.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hir')
            with Note(default_x=50.21, default_y=-276.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=85.43, default_y=-276.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.64, default_y=-271.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-74.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=155.86, default_y=-281.57):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-74.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('volk,')
                    Extend()
            with Note(default_x=191.07, default_y=-286.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=226.29, default_y=-286.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-74.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='8', width=317.12):
            with Note(default_x=23.87, default_y=-286.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-74.06, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schre')
            with Note(default_x=104.89, default_y=-286.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-74.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('cken')
            with Note(default_x=169.7, default_y=-286.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-74.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=234.51, default_y=-281.57):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-74.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil')
                    Extend()
            with Note(default_x=275.01, default_y=-286.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=278.78):
            with Note(default_x=14.23, default_y=-291.57):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-74.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
                    Extend()
            with Note(default_x=47.1, default_y=-286.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=79.97, default_y=-281.57):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-74.06, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                    Extend()
            with Note(default_x=112.84, default_y=-276.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.7, default_y=-271.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-74.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=211.44, default_y=-271.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-74.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('gel')
        with Measure(number='10', width=200.05):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-271.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-74.06, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=92.77, default_y=-276.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.68, default_y=-281.57):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.02, default_y=-74.06, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=166.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.96)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=103.52, default_y=-267.87):
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
                with Lyric(number='1', default_y=-64.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                    Extend()
            with Note(default_x=134.25, default_y=-262.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=279.9):
            with Note(default_x=15.17, default_y=-257.87):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-64.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=49.8, default_y=-262.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.42, default_y=-267.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
            with Note(default_x=153.66, default_y=-262.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=222.9, default_y=-257.87):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='13', width=266.68):
            with Note(default_x=19.64, default_y=-277.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=84.23, default_y=-262.87):
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
                with Lyric(number='1', default_y=-64.71, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=116.53, default_y=-267.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=148.82, default_y=-272.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=200.49, default_y=-287.87):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-64.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
                    Extend()
            with Note(default_x=232.79, default_y=-282.87):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=293.2):
            with Note(default_x=13.8, default_y=-277.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-64.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=48.53, default_y=-272.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.25, default_y=-267.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-64.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
                    Extend()
            with Note(default_x=117.98, default_y=-262.87):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=152.7, default_y=-272.87):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
            with Note(default_x=222.15, default_y=-272.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='15', width=254.23):
            with Note(default_x=21.29, default_y=-277.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=85.55, default_y=-277.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=136.96, default_y=-277.87):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-64.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein.')
            with Note(default_x=188.37, default_y=-267.87):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-64.71, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='16', width=371.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.17)
            with Note(default_x=81.21, default_y=-278.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=153.34, default_y=-263.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=225.48, default_y=-298.91):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-82.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=261.54, default_y=-293.91):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=297.61, default_y=-288.91):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
        with Measure(number='17', width=308.09):
            with Note(default_x=17.23, default_y=-273.91):
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
                with Lyric(number='1', default_y=-82.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=55.29, default_y=-278.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=93.35, default_y=-273.91):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=131.41, default_y=-283.91):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=169.47, default_y=-278.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=230.37, default_y=-278.91):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='18', width=333.84):
            with Note(default_x=20.82, default_y=-278.91):
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
                with Lyric(number='1', default_y=-82.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=59.74, default_y=-283.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=98.67, default_y=-283.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-82.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
                    Extend()
            with Note(default_x=137.6, default_y=-288.91):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=176.53, default_y=-288.91):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-82.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=215.45, default_y=-293.91):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.38, default_y=-298.91):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-82.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='19', width=247.32):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-298.91):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-82.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=59.34, default_y=-303.91):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.06, default_y=-308.91):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.77, default_y=-303.91):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=175.74, default_y=-288.91):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-82.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=178.41):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(114.29)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(1)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=107.32, default_y=-383.1):
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
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
                    Extend()
            with Note(default_x=142.07, default_y=-388.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=268.85):
            with Note(default_x=13.8, default_y=-393.1):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.78, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
            with Note(default_x=77.16, default_y=-398.1):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Note(default_x=140.52, default_y=-383.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schö')
            with Note(default_x=203.89, default_y=-388.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
                    Extend()
            with Note(default_x=235.57, default_y=-383.1):
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
        with Measure(number='3', width=266.03):
            with Note(default_x=20.11, default_y=-378.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=87.98, default_y=-413.1):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
            with Note(default_x=142.27, default_y=-398.1):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-49.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
            with Note(default_x=196.56, default_y=-398.1):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='4', width=276.86):
            with Note(default_x=18.0, default_y=-393.1):
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
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
                    Extend()
            with Note(default_x=50.15, default_y=-388.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=82.31, default_y=-383.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=114.47, default_y=-403.1):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.63, default_y=-368.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=178.78, default_y=-373.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=210.94, default_y=-378.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=243.1, default_y=-383.1):
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
                with Lyric(number='1', default_x=6.58, default_y=-49.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
        with Measure(number='5', width=182.37):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-363.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
            with Note(default_x=59.14, default_y=-398.1):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=114.32, default_y=-383.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=11.84, default_y=-49.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen !')
        with Measure(number='6', width=166.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(114.56)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=107.32, default_y=-386.13):
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
                with Lyric(number='1', default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
                    Extend()
            with Note(default_x=136.02, default_y=-391.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=298.31):
            with Attributes():
                with Time(print_object='no'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-396.13):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hir')
            with Note(default_x=85.43, default_y=-401.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=155.86, default_y=-386.13):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.54, default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('volk,')
            with Note(default_x=226.29, default_y=-391.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=261.5, default_y=-386.13):
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
        with Measure(number='8', width=317.12):
            with Note(default_x=23.87, default_y=-381.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.67, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schre')
            with Note(default_x=104.89, default_y=-416.13):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('cken')
            with Note(default_x=169.7, default_y=-401.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.71, default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=234.51, default_y=-401.13):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil')
        with Measure(number='9', width=278.78):
            with Note(default_x=14.23, default_y=-396.13):
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
                with Lyric(number='1', default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
                    Extend()
            with Note(default_x=47.1, default_y=-391.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=79.97, default_y=-386.13):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                    Extend()
            with Note(default_x=112.84, default_y=-406.13):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.7, default_y=-371.13):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('En')
                    Extend()
            with Note(default_x=178.57, default_y=-376.13):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=211.44, default_y=-381.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('gel')
                    Extend()
            with Note(default_x=244.31, default_y=-386.13):
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
        with Measure(number='10', width=200.05):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-366.13):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=62.86, default_y=-401.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.68, default_y=-386.13):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.02, default_y=-48.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen:')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='11', width=166.57):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(109.98)
            with Attributes():
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
            with Note(default_x=103.52, default_y=-392.84):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
        with Measure(number='12', width=279.9):
            with Note(default_x=15.17, default_y=-357.84):
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
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=49.8, default_y=-362.84):
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
            with Note(default_x=84.42, default_y=-367.84):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
            with Note(default_x=153.66, default_y=-372.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=222.9, default_y=-392.84):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='13', width=266.68):
            with Note(default_x=19.64, default_y=-387.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=84.23, default_y=-387.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=148.82, default_y=-407.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=200.49, default_y=-387.84):
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
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
                    Extend()
            with Note(default_x=232.79, default_y=-382.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=293.2):
            with Note(default_x=13.8, default_y=-377.84):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=83.25, default_y=-377.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note(default_x=152.7, default_y=-372.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
            with Note(default_x=222.15, default_y=-367.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='15', width=254.23):
            with Note(default_x=21.29, default_y=-367.84):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=85.55, default_y=-402.84):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=136.96, default_y=-387.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.78, default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein.')
            with Note(default_x=188.37, default_y=-357.84):
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
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
                    Extend()
            with Note(default_x=220.5, default_y=-362.84):
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
        with Measure(number='16', width=371.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(117.43)
            with Note(default_x=81.21, default_y=-386.34):
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
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                    Extend()
            with Note(default_x=117.28, default_y=-391.34):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=153.34, default_y=-396.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=189.41, default_y=-401.34):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.48, default_y=-406.34):
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
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=261.54, default_y=-401.34):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=297.61, default_y=-396.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
            with Note(default_x=333.68, default_y=-406.34):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=308.09):
            with Note(default_x=17.23, default_y=-416.34):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=55.29, default_y=-421.34):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=93.35, default_y=-416.34):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=131.41, default_y=-426.34):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=169.47, default_y=-411.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=230.37, default_y=-421.34):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='18', width=333.84):
            with Note(default_x=20.82, default_y=-416.34):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=98.67, default_y=-411.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=176.53, default_y=-406.34):
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
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=215.45, default_y=-401.34):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.38, default_y=-396.34):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='19', width=247.32):
            with Attributes():
                with Time(print_object='no'):
                    Beats('3')
                    BeatType('4')
            with Note(default_x=15.0, default_y=-416.34):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=114.77, default_y=-411.34):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=175.74, default_y=-431.34):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.78, default_y=-46.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')