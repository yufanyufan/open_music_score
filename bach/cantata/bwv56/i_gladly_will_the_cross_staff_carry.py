with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Komm, o Tod, du Schlafes Bruder')
    with Identification():
        Creator('Johann Sebastian Bach', type='arranger')
        Creator('Johann Sebastian Bach (1685 - 1750)', type='composer')
        Creator('Johann Franck (1618 - 1677)', type='lyricist')
        Rights('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.')
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
            Millimeters(5.6)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2120.9)
            PageWidth(1500.41)
            with PageMargins(type='even'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
            with PageMargins(type='odd'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Times New Roman', font_size='9.1772')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Full Score', default_x=71.4286, default_y=1949.47, justify='left', valign='bottom', font_family='Times New Roman', font_size='11.1614')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.', default_x=750.207, default_y=142.857, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.', default_x=750.207, default_y=142.857, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Copyright © 2015 by CPDL. This edition can be fully distributed, duplicated, performed, and recorded.', default_x=750.207, default_y=142.857, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano. Oboe I.  II. Violino I. col Soprano.')
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
            PartName('Alto. Violino II. coll´ Alto.')
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
            PartName('Tenore. Taille, Viola col Tenore.')
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
        with Measure(number='1', width=205.58):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(437.36)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=138.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.96, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,')
            with Note(default_x=178.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='2', width=220.09):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod')
            with Note(default_x=66.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=119.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schla')
            with Note(default_x=169.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-44.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('fes')
                    Extend()
            with Note(default_x=193.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='3', width=145.42):
            with Note(default_x=16.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-44.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bru')
            with Note(default_x=97.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-44.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='4', width=128.03):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm')
            with Note(default_x=94.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='5', width=221.08):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Edited by Niels Brandt (2015)', relative_y=20.0, font_family='Times New Roman', font_size='9.3012')
            with Note(default_x=16.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=72.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-44.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
                    Extend()
            with Note(default_x=98.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=125.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=167.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
        with Measure(number='6', width=1300.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(57.37)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=94.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.54, default_y=-48.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('fort;')
        with Measure(number='7', width=201.15):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(57.37)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-47.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lö')
            with Note(default_x=169.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='8', width=276.3):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mei')
            with Note(default_x=81.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
            with Note(default_x=145.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schiff')
            with Note(default_x=210.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('leins')
                    Extend()
            with Note(default_x=242.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='9', width=174.25):
            with Note(default_x=13.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ru')
            with Note(default_x=112.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-47.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='10', width=140.5):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=46.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Brin')
            with Note(default_x=103.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=247.76):
            with Note(default_x=16.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=76.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
                    Extend()
            with Note(default_x=107.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=137.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sich')
            with Note(default_x=185.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ern')
        with Measure(number='12', width=96.43):
            with Note(default_x=14.71, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.78, default_y=-47.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('Port!')
        with Measure(number='13', width=163.8):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=88.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('mag,')
                    Extend()
            with Note(default_x=125.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=347.15):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(57.37)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=101.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('wer')
            with Note(default_x=158.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
            with Note(default_x=216.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.35, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('will,')
            with Note(default_x=288.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
        with Measure(number='15', width=217.28):
            with Note(default_x=16.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scheu')
            with Note(default_x=139.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-45.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('en,')
        with Measure(number='16', width=237.46):
            with Note(default_x=13.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=125.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
                    Extend()
            with Note(default_x=180.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=281.05):
            with Note(default_x=16.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=78.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('viel')
            with Note(default_x=140.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('mehr')
            with Note(default_x=217.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='18', width=217.26):
            with Note(default_x=15.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('freu')
            with Note(default_x=139.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.5, default_y=-45.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('en;')
        with Measure(number='19', width=412.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(57.37)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=90.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Denn')
            with Note(default_x=170.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('durch')
            with Note(default_x=250.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
            with Note(default_x=330.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm')
        with Measure(number='20', width=270.39):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=97.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
            with Note(default_x=178.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ein')
        with Measure(number='21', width=362.89):
            with Note(default_x=11.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=103.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
            with Note(default_x=177.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=269.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sten')
        with Measure(number='22', width=254.27):
            with Note(default_x=10.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=75.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=139.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.72, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=205.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(67.65)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=138.36, default_y=-147.65):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.24, default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,')
            with Note(default_x=178.88, default_y=-152.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='2', width=220.09):
            with Note(default_x=17.23, default_y=-142.65):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod')
                    Extend()
            with Note(default_x=41.88, default_y=-137.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=66.52, default_y=-132.65):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=119.91, default_y=-132.65):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-63.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schla')
            with Note(default_x=144.55, default_y=-137.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=169.2, default_y=-137.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('fes')
        with Measure(number='3', width=145.42):
            with Note(default_x=16.77, default_y=-137.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-63.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bru')
            with Note(default_x=49.99, default_y=-142.65):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.78, default_y=-152.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-63.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='4', width=128.03):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.66, default_y=-157.65):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm')
            with Note(default_x=94.35, default_y=-157.65):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='5', width=221.08):
            with Note(default_x=16.2, default_y=-152.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-63.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=46.67, default_y=-162.65):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=72.66, default_y=-157.65):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=125.89, default_y=-157.65):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=167.48, default_y=-162.65):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
        with Measure(number='6', width=1300.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.94)
            with Note(default_x=94.18, default_y=-171.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.54, default_y=-63.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('fort;')
        with Measure(number='7', width=201.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.66)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.02, default_y=-150.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-62.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lö')
            with Note(default_x=169.48, default_y=-155.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='8', width=276.3):
            with Note(default_x=17.23, default_y=-145.66):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-62.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mei')
            with Note(default_x=49.42, default_y=-140.66):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=81.6, default_y=-135.66):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
            with Note(default_x=145.97, default_y=-135.66):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-62.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schiff')
            with Note(default_x=178.15, default_y=-140.66):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=210.33, default_y=-140.66):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('leins')
        with Measure(number='9', width=174.25):
            with Note(default_x=13.75, default_y=-140.66):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-62.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ru')
            with Note(default_x=57.58, default_y=-145.66):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.02, default_y=-155.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-62.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='10', width=140.5):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=46.12, default_y=-160.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-62.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Brin')
            with Note(default_x=103.36, default_y=-160.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=247.76):
            with Note(default_x=16.2, default_y=-155.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-62.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
                    Extend()
            with Note(default_x=46.67, default_y=-165.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=76.89, default_y=-160.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
            with Note(default_x=137.35, default_y=-160.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sich')
            with Note(default_x=185.71, default_y=-165.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ern')
        with Measure(number='12', width=96.43):
            with Note(default_x=14.71, default_y=-175.66):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.78, default_y=-62.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('Port!')
        with Measure(number='13', width=163.8):
            with Note(default_x=13.8, default_y=-160.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-62.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=88.18, default_y=-155.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-62.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('mag,')
                    Extend()
            with Note(default_x=125.19, default_y=-150.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=347.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=101.58, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('wer')
            with Note(default_x=158.99, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
            with Note(default_x=216.39, default_y=-140.0):
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
                with Lyric(number='1', default_y=-55.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('will,')
                    Extend()
            with Note(default_x=252.27, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=288.15, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
        with Measure(number='15', width=217.28):
            with Note(default_x=16.83, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-55.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scheu')
            with Note(default_x=71.68, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.89, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-55.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('en,')
        with Measure(number='16', width=237.46):
            with Note(default_x=13.89, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-55.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=125.06, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-55.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
                    Extend()
            with Note(default_x=180.46, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=281.05):
            with Note(default_x=16.2, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=78.14, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('viel')
            with Note(default_x=140.08, default_y=-140.0):
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
                with Lyric(number='1', default_y=-55.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('mehr')
                    Extend()
            with Note(default_x=178.79, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.51, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='18', width=217.26):
            with Note(default_x=16.2, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-55.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('freu')
            with Note(default_x=71.22, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.64, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.5, default_y=-55.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('en;')
        with Measure(number='19', width=412.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.24)
            with Note(default_x=90.38, default_y=-165.24):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('Denn')
            with Note(default_x=170.55, default_y=-165.24):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('durch')
            with Note(default_x=250.72, default_y=-160.24):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
            with Note(default_x=330.88, default_y=-165.24):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm')
        with Measure(number='20', width=270.39):
            with Note(default_x=16.2, default_y=-165.24):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
            with Note(default_x=97.68, default_y=-165.24):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
            with Note(default_x=138.42, default_y=-170.24):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=178.8, default_y=-170.24):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('ein')
        with Measure(number='21', width=362.89):
            with Note(default_x=11.98, default_y=-155.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=103.91, default_y=-155.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
            with Note(default_x=177.44, default_y=-150.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=223.41, default_y=-155.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=315.33, default_y=-160.24):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('sten')
        with Measure(number='22', width=254.27):
            with Note(default_x=10.72, default_y=-155.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=75.43, default_y=-155.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=139.78, default_y=-155.24):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=7.99, default_y=-42.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=205.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(86.37)
            with Attributes():
                Divisions(2.0)
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
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=138.36, default_y=-264.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.24, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,')
            with Note(default_x=178.88, default_y=-254.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='2', width=220.09):
            with Note(default_x=17.23, default_y=-249.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.35, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod,')
            with Note(default_x=66.52, default_y=-239.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=91.17, default_y=-244.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=119.91, default_y=-244.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schla')
            with Note(default_x=169.2, default_y=-239.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('fes')
        with Measure(number='3', width=145.42):
            with Note(default_x=16.77, default_y=-244.02):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bru')
            with Note(default_x=70.75, default_y=-249.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.78, default_y=-254.02):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='4', width=128.03):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.66, default_y=-249.02):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm')
            with Note(default_x=94.35, default_y=-264.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='5', width=221.08):
            with Note(default_x=16.2, default_y=-259.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=72.66, default_y=-259.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=125.89, default_y=-264.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=167.48, default_y=-264.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
                    Extend()
            with Note(default_x=193.48, default_y=-269.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=1300.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.94)
            with Note(default_x=94.18, default_y=-268.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.54, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('fort;')
        with Measure(number='7', width=201.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.15)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.02, default_y=-266.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lö')
            with Note(default_x=169.48, default_y=-256.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='8', width=276.3):
            with Note(default_x=17.23, default_y=-251.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mei')
            with Note(default_x=81.6, default_y=-241.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
                    Extend()
            with Note(default_x=113.78, default_y=-246.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=145.97, default_y=-246.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schiff')
            with Note(default_x=210.33, default_y=-241.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('leins')
        with Measure(number='9', width=174.25):
            with Note(default_x=13.75, default_y=-246.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ru')
            with Note(default_x=84.98, default_y=-251.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.02, default_y=-256.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='10', width=140.5):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=46.12, default_y=-251.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Brin')
            with Note(default_x=103.36, default_y=-266.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=247.76):
            with Note(default_x=16.2, default_y=-261.81):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=76.89, default_y=-261.81):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
            with Note(default_x=137.35, default_y=-266.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sich')
            with Note(default_x=185.71, default_y=-266.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ern')
                    Extend()
            with Note(default_x=215.93, default_y=-271.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='12', width=96.43):
            with Note(default_x=14.71, default_y=-276.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.78, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Port!')
        with Measure(number='13', width=163.8):
            with Note(default_x=13.8, default_y=-266.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
            with Note(default_x=87.82, default_y=-256.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.72, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mag,')
        with Measure(number='14', width=347.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.73)
            with Note(default_x=101.58, default_y=-247.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('wer')
            with Note(default_x=158.99, default_y=-252.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
            with Note(default_x=216.39, default_y=-252.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.35, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('will,')
            with Note(default_x=288.15, default_y=-247.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
        with Measure(number='15', width=217.28):
            with Note(default_x=16.83, default_y=-247.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scheu')
            with Note(default_x=71.68, default_y=-252.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=105.97, default_y=-257.73):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.89, default_y=-262.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('en,')
        with Measure(number='16', width=237.46):
            with Note(default_x=13.89, default_y=-262.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
            with Note(default_x=124.69, default_y=-252.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
        with Measure(number='17', width=281.05):
            with Note(default_x=16.2, default_y=-247.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=78.14, default_y=-252.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('viel')
            with Note(default_x=140.08, default_y=-252.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('mehr')
            with Note(default_x=217.51, default_y=-247.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='18', width=217.26):
            with Note(default_x=16.2, default_y=-247.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('freu')
            with Note(default_x=71.22, default_y=-252.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=105.61, default_y=-257.73):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.64, default_y=-262.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.5, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('en;')
        with Measure(number='19', width=412.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.9)
            with Note(default_x=90.38, default_y=-272.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Denn')
            with Note(default_x=170.55, default_y=-267.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('durch')
            with Note(default_x=250.72, default_y=-272.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
            with Note(default_x=330.88, default_y=-272.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm')
        with Measure(number='20', width=270.39):
            with Note(default_x=16.2, default_y=-267.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                    Extend()
            with Note(default_x=56.94, default_y=-272.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.68, default_y=-277.14):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
            with Note(default_x=178.8, default_y=-282.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ein')
        with Measure(number='21', width=362.89):
            with Note(default_x=11.98, default_y=-282.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=103.91, default_y=-267.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
            with Note(default_x=177.44, default_y=-267.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=223.41, default_y=-272.14):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=269.37, default_y=-267.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sten')
                    Extend()
            with Note(default_x=315.33, default_y=-262.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=254.27):
            with Note(default_x=10.72, default_y=-257.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=75.43, default_y=-262.14):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=139.78, default_y=-257.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', default_y=4.12, relative_y=10.0)
                with Lyric(number='1', default_x=8.72, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=205.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(78.4)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=138.36, default_y=-377.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.24, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm,')
            with Note(default_x=178.88, default_y=-382.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='2', width=220.09):
            with Note(default_x=17.23, default_y=-387.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.35, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod,')
            with Note(default_x=66.52, default_y=-362.42):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=119.91, default_y=-357.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schla')
            with Note(default_x=169.2, default_y=-377.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('fes')
        with Measure(number='3', width=145.42):
            with Note(default_x=16.41, default_y=-372.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Bru')
            with Note(default_x=97.78, default_y=-392.42):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='4', width=128.03):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.66, default_y=-352.42):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Komm')
            with Note(default_x=94.35, default_y=-367.42):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='5', width=221.08):
            with Note(default_x=16.2, default_y=-362.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('füh')
            with Note(default_x=72.66, default_y=-362.42):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=125.89, default_y=-357.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=167.48, default_y=-392.42):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur')
        with Measure(number='6', width=1300.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=94.18, default_y=-358.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.54, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('fort;')
        with Measure(number='7', width=201.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.7)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.02, default_y=-386.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lö')
            with Note(default_x=169.48, default_y=-391.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='8', width=276.3):
            with Note(default_x=17.23, default_y=-396.51):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mei')
            with Note(default_x=81.6, default_y=-371.51):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
            with Note(default_x=145.97, default_y=-366.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schiff')
            with Note(default_x=210.33, default_y=-386.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('leins')
        with Measure(number='9', width=174.25):
            with Note(default_x=13.39, default_y=-381.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ru')
            with Note(default_x=112.02, default_y=-401.51):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=8.25, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('der,')
        with Measure(number='10', width=140.5):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=46.12, default_y=-361.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Brin')
            with Note(default_x=103.36, default_y=-376.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='11', width=247.76):
            with Note(default_x=16.2, default_y=-371.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=76.89, default_y=-371.51):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
            with Note(default_x=137.35, default_y=-366.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sich')
            with Note(default_x=185.71, default_y=-401.51):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ern')
        with Measure(number='12', width=96.43):
            with Note(default_x=14.71, default_y=-386.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=5.78, default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Port!')
        with Measure(number='13', width=163.8):
            with Note(default_x=14.16, default_y=-351.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Es')
                    Extend()
            with Note(default_x=51.17, default_y=-356.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.18, default_y=-361.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-44.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mag,')
                    Extend()
            with Note(default_x=125.19, default_y=-366.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=347.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.01)
            with Note(default_x=101.58, default_y=-368.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('wer')
            with Note(default_x=158.99, default_y=-378.74):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
            with Note(default_x=216.39, default_y=-373.74):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.35, default_y=-46.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('will,')
            with Note(default_x=288.15, default_y=-383.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
        with Measure(number='15', width=217.28):
            with Note(default_x=16.83, default_y=-393.74):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scheu')
            with Note(default_x=71.68, default_y=-388.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.89, default_y=-373.74):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=8.97, default_y=-46.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('en,')
        with Measure(number='16', width=237.46):
            with Note(default_x=14.25, default_y=-348.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
                    Extend()
            with Note(default_x=69.65, default_y=-353.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.06, default_y=-358.74):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-46.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('kannst')
                    Extend()
            with Note(default_x=180.46, default_y=-363.74):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=281.05):
            with Note(default_x=16.2, default_y=-368.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=78.14, default_y=-378.74):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('viel')
            with Note(default_x=140.08, default_y=-373.74):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('mehr')
            with Note(default_x=217.51, default_y=-383.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='18', width=217.26):
            with Note(default_x=16.2, default_y=-393.74):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.24, relative_y=-30.0):
                    Syllabic('middle')
                    Text('freu')
            with Note(default_x=71.22, default_y=-388.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.64, default_y=-373.74):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=9.22, default_y=-46.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('en;')
        with Measure(number='19', width=412.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.39)
            with Note(default_x=90.38, default_y=-394.52):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Denn')
            with Note(default_x=170.55, default_y=-404.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('durch')
            with Note(default_x=250.72, default_y=-399.52):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich')
            with Note(default_x=330.88, default_y=-394.52):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('komm')
        with Measure(number='20', width=270.39):
            with Note(default_x=16.2, default_y=-379.52):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                    Extend()
            with Note(default_x=56.94, default_y=-384.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.68, default_y=-389.52):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('her')
            with Note(default_x=178.8, default_y=-384.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ein')
        with Measure(number='21', width=362.89):
            with Note(default_x=11.98, default_y=-394.52):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                    Extend()
            with Note(default_x=57.95, default_y=-399.52):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=103.91, default_y=-404.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
            with Note(default_x=177.44, default_y=-389.52):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schön')
            with Note(default_x=223.41, default_y=-384.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=269.37, default_y=-379.52):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('sten')
        with Measure(number='22', width=254.27):
            with Note(default_x=10.72, default_y=-384.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=75.43, default_y=-419.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('su')
            with Note(default_x=139.78, default_y=-404.52):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=7.99, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=205.58):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(70.17)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                    Mode('major')
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=138.36, default_y=-487.59):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=178.88, default_y=-492.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=220.09):
            with Note(default_x=17.23, default_y=-497.59):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=66.52, default_y=-472.59):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=119.91, default_y=-467.59):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=169.2, default_y=-487.59):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=145.42):
            with Note(default_x=16.41, default_y=-482.59):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=97.78, default_y=-502.59):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='4', width=128.03):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=42.66, default_y=-497.59):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=94.35, default_y=-477.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=221.08):
            with Note(default_x=16.2, default_y=-472.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.66, default_y=-472.59):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=125.89, default_y=-467.59):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=167.48, default_y=-502.59):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=1300.19):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=94.18, default_y=-463.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='7', width=201.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.28)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.02, default_y=-510.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=169.48, default_y=-515.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=276.3):
            with Note(default_x=17.23, default_y=-520.79):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.6, default_y=-495.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=145.97, default_y=-490.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=210.33, default_y=-510.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=174.25):
            with Note(default_x=13.39, default_y=-505.79):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=112.02, default_y=-525.79):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='10', width=140.5):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=46.12, default_y=-520.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=103.36, default_y=-500.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=247.76):
            with Note(default_x=16.2, default_y=-495.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.89, default_y=-495.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=137.35, default_y=-490.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=185.71, default_y=-525.79):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=96.43):
            with Note(default_x=14.71, default_y=-510.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='13', width=163.8):
            with Note(default_x=14.16, default_y=-475.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.17, default_y=-480.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.18, default_y=-485.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.19, default_y=-490.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=347.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.31)
            with Note(default_x=101.58, default_y=-497.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.99, default_y=-507.05):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=216.39, default_y=-502.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=288.15, default_y=-512.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=217.28):
            with Note(default_x=16.83, default_y=-522.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=71.68, default_y=-517.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.89, default_y=-537.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='16', width=237.46):
            with Note(default_x=14.25, default_y=-477.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.65, default_y=-482.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.06, default_y=-487.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=180.46, default_y=-492.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=281.05):
            with Note(default_x=16.2, default_y=-497.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.14, default_y=-507.05):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=140.08, default_y=-502.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=217.51, default_y=-512.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=217.26):
            with Note(default_x=16.2, default_y=-522.05):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=71.22, default_y=-517.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.64, default_y=-537.05):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=412.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Editorial note:Bach in October 1726 wrote the cantata "Ich will den Kreuzstab gerne tragen" (BWV 56), of which this chorale is the fifth and final movement.This edition is based on Bach-Gesellschaft Ausgabe, Band 12, Breitkopf & Härtel, Leipzig, 1863 (Wilhelm Rust). The autograph score by Bach was also consulted. The old clefs of the SAT voices have been changed to modern clefs. All fermatas except on the last note have been removed, to avoid misconceptions. For composers of the Baroque, fermatas simply indicate the end of a phrase, and the corresponding notes should not necessarily be prolonged.Please also note the copyright notice on page 1.This pdf file is available at www.cpdl.org, and here the chorale is also available as a  music notation file (Sibelius 7), an mp3 file and a midi file.', default_y=15.27, relative_y=20.0, font_family='Times New Roman', font_size='10.7894')
            with Note(default_x=90.38, default_y=-544.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=170.55, default_y=-554.92):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=250.72, default_y=-549.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=330.88, default_y=-544.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=270.39):
            with Note(default_x=16.2, default_y=-564.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.94, default_y=-569.92):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.68, default_y=-574.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=178.8, default_y=-569.92):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=362.89):
            with Note(default_x=11.98, default_y=-544.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.95, default_y=-549.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=103.91, default_y=-554.92):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=177.44, default_y=-539.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=223.41, default_y=-534.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=269.37, default_y=-529.92):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
        with Measure(number='22', width=254.27):
            with Note(default_x=10.72, default_y=-534.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.43, default_y=-569.92):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.78, default_y=-589.92):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')