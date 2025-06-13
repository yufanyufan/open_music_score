with ScorePartwise(version='3.1'):
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
            Millimeters(6.01132)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1975.78)
            PageWidth(1397.75)
            with PageMargins(type='even'):
                LeftMargin(66.5412)
                RightMargin(66.5412)
                TopMargin(66.5412)
                BottomMargin(133.082)
            with PageMargins(type='odd'):
                LeftMargin(66.5412)
                RightMargin(66.5412)
                TopMargin(66.5412)
                BottomMargin(133.082)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Finale Lyrics', font_size='8.5')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('MusicXML Part', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('MusicXML Part', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('MusicXML Part', print_object='no')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('MusicXML Part', print_object='no')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Midi_1')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=161.81):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.16)
                        RightMargin(0.0)
                    TopSystemDistance(265.35)
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
                    with Metronome(parentheses='no', default_x=-37.31, default_y=28.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Als Jesus Christus in der Nacht  (B.A.39. No.13)', relative_y=20.0, font_family='Arial Narrow', font_size='14')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=59.3, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=90.59, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-37.31, default_y=121.88, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Note(default_x=83.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-25.45, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.\xa0\xa0Als')
                with Lyric(number='2', default_x=-25.92, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.\xa0\xa0Da')
                with Lyric(number='3', default_x=-25.92, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.\xa0\xa0Nehmt')
                with Lyric(number='4', default_x=-26.39, default_y=-105.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('4.\xa0\xa0Des')
                with Lyric(number='5', default_x=-25.92, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.\xa0\xa0Hier')
                with Lyric(number='6', default_x=-25.92, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('6.\xa0\xa0Das')
                with Lyric(number='7', default_x=-25.92, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('7.\xa0\xa0O')
        with Measure(number='2', width=263.02):
            with Note(default_x=29.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('nahm')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('hin')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('glei')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('geb')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('macht')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=81.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('sus')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='7', default_x=8.8, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
            with Note(default_x=145.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chri')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='3', default_x=8.71, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('eßt,')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('nahm')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Note(default_x=209.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('stus')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
        with Measure(number='3', width=272.23):
            with Note(default_x=24.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Hand')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('auch')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('teu')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sün')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=72.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('res')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('wig')
            with Note(default_x=150.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.24, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht,')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brot')
                with Lyric(number='3', default_x=9.16, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('Leib,')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Blut')
                with Lyric(number='6', default_x=8.55, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('frei,')
                with Lyric(number='7', default_x=9.3, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dank,')
            with Note(default_x=200.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('für')
        with Measure(number='4', width=281.9):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Melodie: Joh. Crüger (1598-1662)\n', default_y=45.96, relative_y=20.0, font_family='Arial Narrow', font_size='12')
                    Words('Satz: Joh. Seb. Bach (1685-1750)\n')
                    Words('Text: Joh. Heermann (1585-1647)')
            with Note(default_x=30.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('rin')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('brachs')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('für')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kelch')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kel')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=100.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=155.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('ward')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprach')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Treu')
            with Note(default_x=224.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='5', width=279.53):
            with Note(default_x=20.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=6.94, default_y=-44.58, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ra')
                with Lyric(number='2', default_x=6.94, default_y=-64.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fin')
                with Lyric(number='3', default_x=6.94, default_y=-85.12, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge')
                with Lyric(number='4', default_x=6.94, default_y=-105.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='5', default_x=6.94, default_y=-125.67, relative_y=-30.0):
                    Syllabic('middle')
                    Text('nie')
                with Lyric(number='6', default_x=6.94, default_y=-145.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('krän')
                with Lyric(number='7', default_x=6.94, default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
            with Note(default_x=145.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.45, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten,')
                with Lyric(number='2', default_x=8.79, default_y=-64.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('gern,')
                with Lyric(number='3', default_x=9.21, default_y=-85.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben,')
                with Lyric(number='4', default_x=9.18, default_y=-105.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('len:')
                with Lyric(number='5', default_x=9.25, default_y=-125.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßen,')
                with Lyric(number='6', default_x=9.21, default_y=-145.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('ken;')
                with Lyric(number='7', default_x=9.21, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben;')
            with Note(default_x=201.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('sah')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nehmt')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
                with Lyric(number='7', default_x=9.01, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('ach,')
        with Measure(number='6', width=416.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.16)
                        RightMargin(0.0)
                    SystemDistance(145.61)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=86.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-25.45, default_y=-61.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('1.\xa0\xa0un')
                with Lyric(number='2', default_x=-25.92, default_y=-81.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.\xa0\xa0auf')
                with Lyric(number='3', default_x=-25.92, default_y=-102.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('3\xa0.\xa0den')
                with Lyric(number='4', default_x=-26.39, default_y=-122.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.\xa0\xa0hin')
                with Lyric(number='5', default_x=-25.92, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.\xa0\xa0ich')
                with Lyric(number='6', default_x=-25.92, default_y=-162.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('6.\xa0\xa0oft')
                with Lyric(number='7', default_x=-25.92, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('7.\xa0\xa0laß')
            with Note(default_x=168.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='3', default_x=9.14, default_y=-102.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket,')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('für')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihrs')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('durch')
            with Note(default_x=250.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('Heil')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trin')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='6', default_x=8.45, default_y=-162.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('tut,')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=332.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('ganz')
                with Lyric(number='2', default_x=9.12, default_y=-81.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel,')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('sollt')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='7', width=319.27):
            with Note(default_x=18.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('war')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dank')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('eu')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Speis')
            with Note(default_x=97.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=175.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.79, default_y=-61.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('dacht,')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('bleib')
                with Lyric(number='4', default_x=9.16, default_y=-122.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('mein,')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('gut')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('bei')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trank')
            with Note(default_x=238.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('das')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('wollt')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('am')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('auch')
        with Measure(number='8', width=304.18):
            with Note(default_x=31.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('selb')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprach')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kreuz')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mei')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=98.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('jetzt')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=166.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('auch')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('recht')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('werd')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=234.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-81.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
                with Lyric(number='3', default_x=6.58, default_y=-102.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='4', default_x=6.58, default_y=-122.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='5', default_x=6.58, default_y=-142.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='6', default_x=6.58, default_y=-162.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='7', default_x=6.58, default_y=-183.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
        with Measure(number='9', width=218.73):
            with Note(default_x=19.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-61.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('stat')
                with Lyric(number='2', default_x=6.22, default_y=-81.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jün')
                with Lyric(number='3', default_x=6.22, default_y=-102.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le')
                with Lyric(number='4', default_x=6.22, default_y=-122.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fal')
                with Lyric(number='5', default_x=6.22, default_y=-142.67, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gie')
                with Lyric(number='6', default_x=6.22, default_y=-162.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
                with Lyric(number='7', default_x=6.22, default_y=-183.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ha')
            with Note(default_x=154.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='inverted', default_y=-44.6, relative_y=-10.0)
                with Lyric(number='1', default_x=8.45, default_y=-61.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten:')
                with Lyric(number='2', default_x=8.79, default_y=-81.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('gern:')
                with Lyric(number='3', default_x=9.21, default_y=-102.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
                with Lyric(number='4', default_x=9.18, default_y=-122.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('len.')
                with Lyric(number='5', default_x=9.25, default_y=-142.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßen.')
                with Lyric(number='6', default_x=9.21, default_y=-162.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ken.')
                with Lyric(number='7', default_x=9.21, default_y=-183.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=161.81):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(189.84)
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
            with Note(default_x=83.68, default_y=-264.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=263.02):
            with Note(default_x=29.47, default_y=-259.84):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.02, default_y=-259.84):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=113.23, default_y=-264.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=145.45, default_y=-264.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.66, default_y=-269.84):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=209.88, default_y=-264.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=272.23):
            with Note(default_x=24.31, default_y=-264.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.3, default_y=-264.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=107.2, default_y=-269.84):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=150.83, default_y=-279.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=200.83, default_y=-254.84):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=281.9):
            with Note(default_x=30.88, default_y=-254.84):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.52, default_y=-259.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=100.16, default_y=-254.84):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=155.59, default_y=-254.84):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=190.23, default_y=-259.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=224.87, default_y=-254.84):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=279.53):
            with Note(default_x=21.02, default_y=-254.84):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=76.52, default_y=-259.84):
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
            with Note(default_x=145.89, default_y=-269.84):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.38, default_y=-279.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='6', width=416.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(201.9)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=86.23, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=168.35, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=250.48, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=291.54, default_y=-296.9):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=332.61, default_y=-291.9):
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
            with Note(default_x=373.67, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='7', width=319.27):
            with Note(default_x=18.25, default_y=-281.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=57.65, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.04, default_y=-281.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=136.44, default_y=-291.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=175.84, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=238.87, default_y=-301.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=278.27, default_y=-296.9):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=304.18):
            with Note(default_x=31.12, default_y=-291.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.98, default_y=-291.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=166.85, default_y=-291.9):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=234.71, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=218.73):
            with Note(default_x=19.38, default_y=-286.9):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=86.79, default_y=-291.9):
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
            with Note(default_x=154.2, default_y=-301.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='inverted', default_y=-59.6, relative_y=-10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=161.81):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(80.0)
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
            with Note(default_x=83.68, default_y=-359.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=-25.45, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.\xa0\xa0Als')
                with Lyric(number='2', default_x=-25.92, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.\xa0\xa0Da')
                with Lyric(number='3', default_x=-25.92, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.\xa0\xa0Nehmt')
                with Lyric(number='4', default_x=-26.39, default_y=-105.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('4.\xa0\xa0Des')
                with Lyric(number='5', default_x=-25.92, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.\xa0\xa0Hier')
                with Lyric(number='6', default_x=-25.92, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('6.\xa0\xa0Das')
                with Lyric(number='7', default_x=-25.92, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('7.\xa0\xa0O')
        with Measure(number='2', width=263.02):
            with Note(default_x=29.47, default_y=-364.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('nahm')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('hin')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('middle')
                    Text('glei')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('geb')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('macht')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=81.02, default_y=-364.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('sus')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='7', default_x=8.8, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
            with Note(default_x=145.45, default_y=-369.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Chri')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='3', default_x=8.71, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('eßt,')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('nahm')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Note(default_x=209.88, default_y=-364.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('stus')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
        with Measure(number='3', width=272.23):
            with Note(default_x=24.31, default_y=-359.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Hand')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('auch')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('teu')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sün')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=72.3, default_y=-364.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('mein')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('res')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('wig')
            with Note(default_x=129.02, default_y=-369.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=150.83, default_y=-374.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.24, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nacht,')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brot')
                with Lyric(number='3', default_x=9.16, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('Leib,')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wein')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('Blut')
                with Lyric(number='6', default_x=8.55, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('frei,')
                with Lyric(number='7', default_x=9.3, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dank,')
            with Note(default_x=200.83, default_y=-364.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('für')
        with Measure(number='4', width=281.9):
            with Note(default_x=30.88, default_y=-349.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('rin')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('brachs')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('für')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kelch')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kel')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=100.16, default_y=-354.84):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
            with Note(default_x=155.59, default_y=-359.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('ward')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprach')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('Treu')
            with Note(default_x=224.87, default_y=-354.84):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('mehr')
                with Lyric(number='7', default_x=6.58, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='5', width=279.53):
            with Note(default_x=21.02, default_y=-349.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('end')
                    Text('ra')
                with Lyric(number='2', default_y=-64.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fin')
                with Lyric(number='3', default_y=-85.12, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge')
                with Lyric(number='4', default_y=-105.4, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
                with Lyric(number='5', default_y=-125.67, relative_y=-30.0):
                    Syllabic('middle')
                    Text('nie')
                with Lyric(number='6', default_y=-145.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('krän')
                with Lyric(number='7', default_y=-166.22, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ga')
            with Note(default_x=76.52, default_y=-354.84):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=111.2, default_y=-359.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.89, default_y=-364.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=8.45, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('ten,')
                with Lyric(number='2', default_x=8.79, default_y=-64.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('gern,')
                with Lyric(number='3', default_x=9.21, default_y=-85.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben,')
                with Lyric(number='4', default_x=9.18, default_y=-105.4, relative_y=-30.0):
                    Syllabic('end')
                    Text('len:')
                with Lyric(number='5', default_x=9.25, default_y=-125.67, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßen,')
                with Lyric(number='6', default_x=9.21, default_y=-145.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('ken;')
                with Lyric(number='7', default_x=9.21, default_y=-166.22, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben;')
            with Note(default_x=201.38, default_y=-374.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.58, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                with Lyric(number='2', default_x=6.58, default_y=-64.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('sah')
                with Lyric(number='3', default_x=6.58, default_y=-85.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='4', default_x=6.58, default_y=-105.4, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nehmt')
                with Lyric(number='5', default_x=6.58, default_y=-125.67, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
                with Lyric(number='6', default_x=6.58, default_y=-145.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('so')
                with Lyric(number='7', default_x=9.01, default_y=-166.22, relative_y=-30.0):
                    Syllabic('single')
                    Text('ach,')
        with Measure(number='6', width=416.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(80.0)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=86.23, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=-25.45, default_y=-61.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('1.\xa0\xa0un')
                with Lyric(number='2', default_x=-25.92, default_y=-81.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.\xa0\xa0auf')
                with Lyric(number='3', default_x=-25.92, default_y=-101.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('3\xa0.\xa0den')
                with Lyric(number='4', default_x=-26.39, default_y=-121.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.\xa0\xa0hin')
                with Lyric(number='5', default_x=-25.92, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.\xa0\xa0ich')
                with Lyric(number='6', default_x=-25.92, default_y=-162.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('6.\xa0\xa0oft')
                with Lyric(number='7', default_x=-25.92, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('7.\xa0\xa0laß')
            with Note(default_x=168.35, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('gen')
                with Lyric(number='3', default_x=9.14, default_y=-101.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket,')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('für')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihrs')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('durch')
            with Note(default_x=250.48, default_y=-391.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('Heil')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trin')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='6', default_x=8.45, default_y=-162.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('tut,')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=332.61, default_y=-381.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ganz')
                with Lyric(number='2', default_x=9.12, default_y=-81.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel,')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ket')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('sollt')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('se')
        with Measure(number='7', width=319.27):
            with Note(default_x=18.25, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('war')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dank')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('eu')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('in')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('euch')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Speis')
            with Note(default_x=97.04, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('te')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ge')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=175.84, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.79, default_y=-61.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('dacht,')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('bleib')
                with Lyric(number='4', default_x=9.16, default_y=-121.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('mein,')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('gut')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('bei')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trank')
            with Note(default_x=238.87, default_y=-396.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('das')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('wollt')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('am')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('an')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('auch')
        with Measure(number='8', width=304.18):
            with Note(default_x=31.12, default_y=-391.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('selb')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('sprach')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kreuz')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mei')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('mich')
            with Note(default_x=98.98, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('jetzt')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=132.92, default_y=-396.9):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=166.85, default_y=-381.9):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
                with Lyric(number='2', default_y=-81.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sei')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('auch')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('recht')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('single')
                    Text('werd')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('Tod')
                with Lyric(number='7', default_y=-182.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=200.78, default_y=-391.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=234.71, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-81.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen')
                with Lyric(number='3', default_x=6.58, default_y=-101.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('im')
                with Lyric(number='4', default_x=6.58, default_y=-121.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='5', default_x=6.58, default_y=-142.27, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver')
                with Lyric(number='6', default_x=6.58, default_y=-162.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
                with Lyric(number='7', default_x=6.58, default_y=-182.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben')
        with Measure(number='9', width=218.73):
            with Note(default_x=19.38, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-61.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('stat')
                with Lyric(number='2', default_y=-81.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jün')
                with Lyric(number='3', default_y=-101.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Le')
                with Lyric(number='4', default_y=-121.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fal')
                with Lyric(number='5', default_y=-142.27, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gie')
                with Lyric(number='6', default_y=-162.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den')
                with Lyric(number='7', default_y=-182.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ha')
            with Note(default_x=53.08, default_y=-401.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=86.79, default_y=-386.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=120.49, default_y=-391.9):
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
            with Note(default_x=154.2, default_y=-396.9):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Fermata(None, type='inverted', default_y=-44.2, relative_y=-10.0)
                with Lyric(number='1', default_x=8.45, default_y=-61.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('ten:')
                with Lyric(number='2', default_x=8.79, default_y=-81.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('gern:')
                with Lyric(number='3', default_x=9.21, default_y=-101.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
                with Lyric(number='4', default_x=9.18, default_y=-121.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('len.')
                with Lyric(number='5', default_x=9.25, default_y=-142.27, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßen.')
                with Lyric(number='6', default_x=9.21, default_y=-162.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('ken.')
                with Lyric(number='7', default_x=9.21, default_y=-182.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('ben.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=161.81):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(199.93)
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
            with Note(default_x=83.68, default_y=-609.77):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=263.02):
            with Note(default_x=29.47, default_y=-604.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.02, default_y=-599.77):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=145.45, default_y=-594.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=209.88, default_y=-589.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=272.23):
            with Note(default_x=24.31, default_y=-584.77):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.3, default_y=-579.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.83, default_y=-599.77):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=200.83, default_y=-599.77):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=235.73, default_y=-604.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=281.9):
            with Note(default_x=30.88, default_y=-609.77):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=100.16, default_y=-614.77):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=155.59, default_y=-619.77):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=224.87, default_y=-624.77):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=279.53):
            with Note(default_x=21.02, default_y=-609.77):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=76.52, default_y=-604.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.89, default_y=-624.77):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.38, default_y=-624.77):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=416.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(223.52)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('4')
            with Note(default_x=86.23, default_y=-680.42):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=-25.45, default_y=-52.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.\xa0\xa0un')
            with Note(default_x=127.29, default_y=-645.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=209.42, default_y=-650.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser')
            with Note(default_x=250.48, default_y=-655.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('Heil')
            with Note(default_x=291.54, default_y=-640.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=373.67, default_y=-645.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('ganz')
        with Measure(number='7', width=319.27):
            with Note(default_x=18.25, default_y=-650.42):
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
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('war')
            with Note(default_x=57.65, default_y=-655.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.04, default_y=-650.42):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-52.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
            with Note(default_x=136.44, default_y=-660.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=175.84, default_y=-645.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-52.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('dacht,')
            with Note(default_x=238.87, default_y=-645.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('das')
        with Measure(number='8', width=304.18):
            with Note(default_x=31.12, default_y=-650.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('selb')
            with Note(default_x=65.05, default_y=-655.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=98.98, default_y=-660.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=166.85, default_y=-675.42):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-52.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('zu')
            with Note(default_x=234.71, default_y=-670.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-52.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=268.65, default_y=-665.42):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='9', width=218.73):
            with Note(default_x=19.02, default_y=-660.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-52.81, relative_y=-30.0):
                    Syllabic('middle')
                    Text('stat')
            with Note(default_x=154.2, default_y=-645.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.45, default_y=-52.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten:')
            with Barline(location='right'):
                BarStyle('light-heavy')