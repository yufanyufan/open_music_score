with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Das ist des Vaters Wille')
    with Identification():
        Creator('Johann Sebastian Bach', type='arranger')
        Creator('Johann Sebastian Bach (1685 - 1750)', type='composer')
        Creator('Ludwig Helmbold (1532 - 1598)', type='lyricist')
        Rights('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.\n')
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
            Millimeters(5.90304)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2012.02)
            PageWidth(1423.39)
            with PageMargins(type='even'):
                LeftMargin(67.7617)
                RightMargin(67.7617)
                TopMargin(67.7617)
                BottomMargin(135.523)
            with PageMargins(type='odd'):
                LeftMargin(67.7617)
                RightMargin(67.7617)
                TopMargin(67.7617)
                BottomMargin(135.523)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Times New Roman', font_size='9.6688')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685 - 1750)', default_x=1355.63, default_y=1811.26, justify='right', valign='bottom', font_family='Times New Roman', font_size='9.2768')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Ludwig Helmbold (1532 - 1598)', default_x=67.7617, default_y=1811.26, justify='left', valign='bottom', font_family='Times New Roman', font_size='9.2768')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Das ist des Vaters Wille', default_x=711.694, default_y=1944.26, justify='center', valign='top', font_family='Times New Roman', font_size='18.5536')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.\n', default_x=711.694, default_y=1876.5, justify='center', valign='top', font_family='Times New Roman', font_size='8.4929')
        CreditWords(None)
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords("Final chorale of cantata Herr, wie du willt, so schick's mit mir (BWV 73)\n", default_x=711.694, default_y=1876.5, justify='center', valign='top', font_family='Times New Roman', font_size='11.7594')
        CreditWords(None)
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.\n', default_x=711.694, default_y=135.523, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.\n', default_x=711.694, default_y=135.523, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.\n', default_x=711.694, default_y=135.523, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano. Corno, Oboe I. Violino I. col Soprano.')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto. Oboe II. Violino II. coll´ Alto.')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenore. Viola col Tenore.')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Basso.')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass (2)')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P5'):
            PartName('Continuo.')
            PartAbbreviation('Ped.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Pedals')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=151.11):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(472.84)
                        RightMargin(-0.0)
                    TopSystemDistance(203.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=112.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Das')
        with Measure(number='2', width=171.03):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=52.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=91.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
            with Note(default_x=130.52, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ters')
        with Measure(number='3', width=161.88):
            with Note(default_x=17.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wil')
            with Note(default_x=93.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.53, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('le,')
            with Note(default_x=126.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Der')
        with Measure(number='4', width=216.13):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=59.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=102.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schaf')
            with Note(default_x=158.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('fen')
        with Measure(number='5', width=114.87):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Edited by Niels Brandt (2015)', relative_y=20.0, font_family='Times New Roman', font_size='9.2768')
            with Note(default_x=14.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.41, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat;')
            with Note(default_x=80.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sein')
        with Measure(number='6', width=1230.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(57.38)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=90.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sohn')
            with Note(default_x=375.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=659.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('Guts')
            with Note(default_x=944.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='7', width=216.82):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(57.38)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=90.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fül')
            with Note(default_x=156.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=185.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
        with Measure(number='8', width=208.61):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wor')
            with Note(default_x=57.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=99.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
        with Measure(number='9', width=125.21):
            with Note(default_x=16.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.43, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('nad;')
            with Note(default_x=86.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Auch')
        with Measure(number='10', width=173.41):
            with Note(default_x=16.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=55.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=94.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heil')
            with Note(default_x=132.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=108.46):
            with Note(default_x=23.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Geist')
            with Note(default_x=78.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
        with Measure(number='12', width=212.89):
            with Note(default_x=21.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glau')
            with Note(default_x=61.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=111.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=161.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
        with Measure(number='13', width=185.09):
            with Note(default_x=14.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gie')
            with Note(default_x=108.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.45, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret,')
            with Note(default_x=145.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zum')
        with Measure(number='14', width=402.21):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(57.38)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Das ist des Vaters Wille,Der uns erschaffen hat;Sein Sohn hat Guts die FülleErworben und Genad;Auch Gott der Heilge GeistIm Glauben uns regieret,Zum Reich des Himmels führet.Ihm sei Lob, Ehr und Preis!(Ludwig Helmbold, 1563)', default_y=15.97, relative_y=20.0, font_family='Times New Roman', font_size='12.9353')
            with Note(default_x=90.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Reich')
            with Note(default_x=163.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=236.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=327.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('mels')
        with Measure(number='15', width=314.12):
            with Note(default_x=16.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=103.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.45, default_y=-45.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret.')
            with Note(default_x=242.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ihm')
        with Measure(number='16', width=346.75):
            with Note(default_x=13.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=73.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.63, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lob,')
            with Note(default_x=160.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ehr')
            with Note(default_x=258.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='17', width=167.41):
            with Note(default_x=14.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.34, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Preis!')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=151.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(68.03)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=112.68, default_y=-148.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Das')
        with Measure(number='2', width=171.03):
            with Note(default_x=13.8, default_y=-138.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=52.71, default_y=-138.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=91.61, default_y=-138.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
            with Note(default_x=130.52, default_y=-143.03):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ters')
        with Measure(number='3', width=161.88):
            with Note(default_x=17.76, default_y=-143.03):
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
                with Lyric(number='1', default_y=-42.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wil')
            with Note(default_x=38.72, default_y=-138.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=59.68, default_y=-133.03):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.21, default_y=-138.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.53, default_y=-42.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('le,')
            with Note(default_x=126.75, default_y=-138.03):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Der')
        with Measure(number='4', width=216.13):
            with Note(default_x=16.2, default_y=-148.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=59.56, default_y=-143.03):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=102.93, default_y=-143.03):
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
                with Lyric(number='1', default_y=-42.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schaf')
            with Note(default_x=131.79, default_y=-133.03):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=158.9, default_y=-138.03):
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
            with Note(default_x=186.0, default_y=-143.03):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('fen')
        with Measure(number='5', width=114.87):
            with Note(default_x=14.74, default_y=-148.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.41, default_y=-42.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat;')
            with Note(default_x=80.0, default_y=-148.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sein')
        with Measure(number='6', width=1230.49):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=90.38, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sohn')
            with Note(default_x=375.01, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=659.63, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Guts')
            with Note(default_x=944.26, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='7', width=216.82):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(69.74)
            with Note(default_x=90.74, default_y=-144.74):
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
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fül')
            with Note(default_x=109.05, default_y=-139.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=127.35, default_y=-134.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.64, default_y=-139.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=185.93, default_y=-139.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
        with Measure(number='8', width=208.61):
            with Note(default_x=16.2, default_y=-149.74):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wor')
            with Note(default_x=57.99, default_y=-144.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=99.78, default_y=-144.74):
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
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=128.65, default_y=-134.74):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.77, default_y=-139.74):
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
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
            with Note(default_x=180.89, default_y=-144.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=125.21):
            with Note(default_x=16.86, default_y=-149.74):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.43, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('nad;')
            with Note(default_x=86.23, default_y=-124.74):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Auch')
        with Measure(number='10', width=173.41):
            with Note(default_x=16.2, default_y=-124.74):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=55.1, default_y=-124.74):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=94.0, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heil')
            with Note(default_x=132.91, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=108.46):
            with Note(default_x=23.14, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Geist')
            with Note(default_x=78.61, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
        with Measure(number='12', width=212.89):
            with Note(default_x=21.82, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glau')
            with Note(default_x=61.71, default_y=-134.74):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=111.57, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=161.43, default_y=-124.74):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=186.36, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=185.09):
            with Note(default_x=14.65, default_y=-134.74):
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
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gie')
            with Note(default_x=38.1, default_y=-139.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=61.55, default_y=-134.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=108.45, default_y=-144.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.45, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret,')
            with Note(default_x=145.97, default_y=-129.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zum')
        with Measure(number='14', width=402.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.0)
            with Note(default_x=90.38, default_y=-146.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Reich')
            with Note(default_x=163.37, default_y=-156.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=236.37, default_y=-166.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-49.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=327.61, default_y=-151.0):
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
                    Slur(type='start', placement='below', number=1)
        with Measure(number='15', width=314.12):
            with Note(default_x=16.2, default_y=-151.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.78, default_y=-156.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('mels')
            with Note(default_x=103.35, default_y=-151.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=173.08, default_y=-156.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.45, default_y=-49.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret.')
            with Note(default_x=242.8, default_y=-161.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ihm')
        with Measure(number='16', width=346.75):
            with Note(default_x=13.94, default_y=-166.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=73.66, default_y=-161.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.63, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lob,')
            with Note(default_x=160.54, default_y=-156.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ehr')
            with Note(default_x=258.27, default_y=-156.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='17', width=167.41):
            with Note(default_x=14.69, default_y=-156.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.62, default_y=-49.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Preis!')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=151.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(66.14)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Note(default_x=112.68, default_y=-229.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Das')
        with Measure(number='2', width=171.03):
            with Note(default_x=13.8, default_y=-219.18):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=52.71, default_y=-224.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=91.61, default_y=-229.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
            with Note(default_x=130.52, default_y=-229.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ters')
        with Measure(number='3', width=161.88):
            with Note(default_x=17.76, default_y=-234.18):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wil')
            with Note(default_x=59.68, default_y=-239.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.21, default_y=-224.18):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.53, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('le,')
            with Note(default_x=126.75, default_y=-219.18):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Der')
        with Measure(number='4', width=216.13):
            with Note(default_x=16.2, default_y=-229.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=59.56, default_y=-239.18):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=102.93, default_y=-244.18):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schaf')
            with Note(default_x=158.9, default_y=-244.18):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('fen')
        with Measure(number='5', width=114.87):
            with Note(default_x=14.74, default_y=-229.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.13, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat;')
            with Note(default_x=80.0, default_y=-229.18):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sein')
        with Measure(number='6', width=1230.49):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=90.38, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sohn')
            with Note(default_x=375.01, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=659.63, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('Guts')
            with Note(default_x=944.26, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='7', width=216.82):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.71)
            with Note(default_x=90.74, default_y=-245.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fül')
            with Note(default_x=127.35, default_y=-250.45):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.64, default_y=-235.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=185.93, default_y=-230.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
        with Measure(number='8', width=208.61):
            with Note(default_x=16.2, default_y=-240.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wor')
            with Note(default_x=57.99, default_y=-250.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=99.78, default_y=-255.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.77, default_y=-255.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
        with Measure(number='9', width=125.21):
            with Note(default_x=16.86, default_y=-240.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.15, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('nad;')
            with Note(default_x=86.23, default_y=-230.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Auch')
        with Measure(number='10', width=173.41):
            with Note(default_x=16.2, default_y=-225.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=55.1, default_y=-215.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=94.0, default_y=-220.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heil')
            with Note(default_x=132.91, default_y=-225.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=108.46):
            with Note(default_x=23.14, default_y=-220.45):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Geist')
            with Note(default_x=78.61, default_y=-225.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
        with Measure(number='12', width=212.89):
            with Note(default_x=21.82, default_y=-230.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glau')
            with Note(default_x=86.64, default_y=-235.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=111.57, default_y=-235.45):
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
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
                    Extend()
            with Note(default_x=136.5, default_y=-245.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=161.43, default_y=-230.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
        with Measure(number='13', width=185.09):
            with Note(default_x=14.65, default_y=-230.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gie')
            with Note(default_x=61.55, default_y=-235.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=85.0, default_y=-240.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.45, default_y=-245.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.45, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret,')
            with Note(default_x=145.97, default_y=-225.45):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zum')
        with Measure(number='14', width=402.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.14)
            with Note(default_x=90.38, default_y=-265.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Reich')
            with Note(default_x=163.37, default_y=-280.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=236.37, default_y=-275.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=281.99, default_y=-270.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=327.61, default_y=-265.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('mels')
        with Measure(number='15', width=314.12):
            with Note(default_x=16.2, default_y=-260.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.76, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=103.35, default_y=-265.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.08, default_y=-270.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.45, default_y=-45.76, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret.')
            with Note(default_x=242.8, default_y=-280.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ihm')
        with Measure(number='16', width=346.75):
            with Note(default_x=13.94, default_y=-280.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=73.66, default_y=-275.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=0.48, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lob,')
                    Extend()
            with Note(default_x=117.1, default_y=-270.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=160.54, default_y=-265.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ehr')
                    Extend()
            with Note(default_x=203.98, default_y=-270.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.12, default_y=-275.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=258.27, default_y=-270.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=301.71, default_y=-270.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='17', width=167.41):
            with Note(default_x=14.69, default_y=-265.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', default_y=4.12, relative_y=10.0)
                with Lyric(number='1', default_x=9.34, default_y=-45.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('Preis!')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=151.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(80.41)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=112.68, default_y=-359.58):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Das')
        with Measure(number='2', width=171.03):
            with Note(default_x=13.8, default_y=-324.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=52.71, default_y=-329.58):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=91.61, default_y=-324.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
            with Note(default_x=130.52, default_y=-334.58):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('ters')
        with Measure(number='3', width=161.88):
            with Note(default_x=17.76, default_y=-329.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wil')
            with Note(default_x=59.68, default_y=-344.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.21, default_y=-339.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.53, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('le,')
            with Note(default_x=126.75, default_y=-349.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Der')
        with Measure(number='4', width=216.13):
            with Note(default_x=16.2, default_y=-334.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=59.56, default_y=-344.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=102.93, default_y=-364.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schaf')
            with Note(default_x=158.9, default_y=-364.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('fen')
        with Measure(number='5', width=114.87):
            with Note(default_x=14.74, default_y=-359.58):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.41, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat;')
            with Note(default_x=80.0, default_y=-359.58):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sein')
        with Measure(number='6', width=1230.49):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(77.13)
            with Note(default_x=90.38, default_y=-317.13):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sohn')
            with Note(default_x=375.01, default_y=-322.13):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat')
            with Note(default_x=659.63, default_y=-317.13):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Guts')
            with Note(default_x=944.26, default_y=-327.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
        with Measure(number='7', width=216.82):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.69)
            with Note(default_x=90.74, default_y=-339.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fül')
            with Note(default_x=127.35, default_y=-354.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.64, default_y=-349.13):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('le')
            with Note(default_x=185.93, default_y=-359.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Er')
        with Measure(number='8', width=208.61):
            with Note(default_x=16.2, default_y=-344.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wor')
            with Note(default_x=57.99, default_y=-354.13):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=99.78, default_y=-374.13):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=154.77, default_y=-374.13):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
        with Measure(number='9', width=125.21):
            with Note(default_x=16.86, default_y=-369.13):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.43, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('nad;')
            with Note(default_x=86.23, default_y=-334.13):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Auch')
        with Measure(number='10', width=173.41):
            with Note(default_x=16.2, default_y=-344.13):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=55.1, default_y=-354.13):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=94.0, default_y=-339.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Heil')
            with Note(default_x=132.91, default_y=-374.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=108.46):
            with Note(default_x=23.14, default_y=-359.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Geist')
            with Note(default_x=78.61, default_y=-339.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Im')
        with Measure(number='12', width=212.89):
            with Note(default_x=21.82, default_y=-349.13):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Glau')
            with Note(default_x=61.71, default_y=-354.13):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
            with Note(default_x=111.57, default_y=-359.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=161.43, default_y=-369.13):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
        with Measure(number='13', width=185.09):
            with Note(default_x=14.29, default_y=-354.13):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-40.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gie')
            with Note(default_x=108.45, default_y=-374.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.45, default_y=-40.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret,')
            with Note(default_x=145.97, default_y=-339.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zum')
        with Measure(number='14', width=402.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.15)
            with Note(default_x=90.38, default_y=-393.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Reich')
            with Note(default_x=163.37, default_y=-403.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('des')
            with Note(default_x=236.37, default_y=-388.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=327.61, default_y=-393.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('mels')
        with Measure(number='15', width=314.12):
            with Note(default_x=16.2, default_y=-398.29):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.29, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=103.35, default_y=-398.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.08, default_y=-393.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.45, default_y=-45.29, relative_y=-30.0):
                    Syllabic('end')
                    Text('ret.')
            with Note(default_x=242.8, default_y=-408.29):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ihm')
        with Measure(number='16', width=346.75):
            with Note(default_x=13.94, default_y=-403.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=73.66, default_y=-388.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=8.63, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lob,')
            with Note(default_x=160.54, default_y=-393.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ehr')
            with Note(default_x=258.27, default_y=-428.29):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='17', width=167.41):
            with Note(default_x=14.69, default_y=-413.29):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=8.62, default_y=-45.29, relative_y=-30.0):
                    Syllabic('single')
                    Text('Preis!')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=151.11):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(88.01)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=112.68, default_y=-487.59):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=171.03):
            with Note(default_x=13.8, default_y=-452.59):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=52.71, default_y=-457.59):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=91.61, default_y=-452.59):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=130.52, default_y=-462.59):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=161.88):
            with Note(default_x=17.76, default_y=-457.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('65', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=59.68, default_y=-472.59):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=93.21, default_y=-467.59):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.75, default_y=-477.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=216.13):
            with Note(default_x=16.2, default_y=-462.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=59.56, default_y=-472.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('65', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=102.93, default_y=-492.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=158.9, default_y=-492.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=114.87):
            with Note(default_x=14.74, default_y=-487.59):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=80.0, default_y=-487.59):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=1230.49):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.43)
            with Note(default_x=90.38, default_y=-444.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=375.01, default_y=-449.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=659.63, default_y=-444.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=944.26, default_y=-454.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=216.82):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(92.31)
            with Note(default_x=90.74, default_y=-471.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('65', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=127.35, default_y=-486.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.64, default_y=-481.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=185.93, default_y=-491.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=208.61):
            with Note(default_x=16.2, default_y=-476.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=57.99, default_y=-486.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('65', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=99.78, default_y=-506.45):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=154.77, default_y=-506.45):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=125.21):
            with Note(default_x=16.86, default_y=-501.45):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=86.23, default_y=-466.45):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=173.41):
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=16.2, default_y=-476.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('75', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=55.1, default_y=-486.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('64', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=94.0, default_y=-471.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('53', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=132.91, default_y=-506.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=108.46):
            with Note(default_x=23.14, default_y=-491.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=78.61, default_y=-471.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=212.89):
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=21.82, default_y=-481.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=61.71, default_y=-486.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.57, default_y=-491.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=161.43, default_y=-501.45):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=185.09):
            with Direction(placement='above'):
                with DirectionType():
                    Words('7', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=14.29, default_y=-486.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6 5  ', relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=108.45, default_y=-506.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=145.97, default_y=-471.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=402.21):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(134.48)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Editorial note:Bach in January 1724 wrote the cantata "Herr, wie du willt, so schick\'s mit mir" (BWV 73), of which this chorale is the fifth and final movement. This edition is based on Bach-Gesellschaft Ausgabe, Band 18, Breitkopf & Härtel, Leipzig, 1870 (Wilhelm Rust).The old clefs of the SAT voices have been changed to modern clefs.All fermatas except on the last note have been removed, to avoid misconceptions. For composers of the Baroque, fermatas simply indicate the end of a phrase, and the corresponding notes should not necessarily be prolonged.Please also note the copyright notice on page 1.This pdf file contains both the full score and the 5 individual parts.It is available at www.cpdl.org, and here the chorale is also available as a music notation file (Sibelius 7), an mp3 file and a midi file.', default_y=17.17, relative_y=20.0, font_family='Times New Roman', font_size='10.9754')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=90.38, default_y=-567.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('75', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=163.37, default_y=-577.77):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=236.37, default_y=-562.77):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('64x', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=327.61, default_y=-567.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=314.12):
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=16.2, default_y=-572.77):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('m5', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=103.35, default_y=-572.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.08, default_y=-567.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6b', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=242.8, default_y=-582.77):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=346.75):
            with Note(default_x=13.94, default_y=-577.77):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('6', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=73.66, default_y=-562.77):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('64', default_y=38.42, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=160.54, default_y=-567.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('5§', default_y=39.85, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=258.27, default_y=-602.77):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=167.41):
            with Direction(placement='above'):
                with DirectionType():
                    Words('§', default_y=39.85, relative_y=20.0, font_family='Opus Figured Bass Std', font_size='8.4929')
            with Note(default_x=14.69, default_y=-587.77):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')