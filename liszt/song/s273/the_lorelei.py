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
            Millimeters(7.05556)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.36)
            PageWidth(1190.88)
            with PageMargins(type='even'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
            with PageMargins(type='odd'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Die Lorelei', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Die schönsten Volkslieder, S. 12', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Deutsches Volkslied', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Heinrich Heine', default_x=56.6929, default_y=1526.67, justify='left', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
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
        with Measure(number='1', width=203.4):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(63.6)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
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
            with Note(default_x=155.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-14.9, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.Ich', font_family='Times New Roman')
                with Lyric(number='2', default_x=-15.7, default_y=-74.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.Die', font_family='Times New Roman')
                with Lyric(number='3', default_x=-15.3, default_y=-99.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.Den', font_family='Times New Roman')
        with Measure(number='2', width=306.76):
            with Note(default_x=26.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sch', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sch', font_family='Times New Roman')
            with Note(default_x=81.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ö', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('middle')
                    Text('i', font_family='Times New Roman')
            with Note(default_x=124.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('was', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('nste', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('ffer', font_family='Times New Roman')
            with Note(default_x=169.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Jung', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('im', font_family='Times New Roman')
            with Note(default_x=214.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fr', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('klei', font_family='Times New Roman')
            with Note(default_x=259.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('au', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('nen', font_family='Times New Roman')
        with Measure(number='3', width=168.67):
            with Note(default_x=28.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('middle')
                    Text('deu', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sitz', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schif', font_family='Times New Roman')
            with Note(default_x=85.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.75, default_y=-48.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten,', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('et', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('fe', font_family='Times New Roman')
            with Note(default_x=132.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('daß', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('dort', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er', font_family='Times New Roman')
        with Measure(number='4', width=230.5):
            with Note(default_x=28.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('ich', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ob', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('greift', font_family='Times New Roman')
            with Note(default_x=85.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('so', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('en', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman')
            with Note(default_x=121.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('tr', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wu', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit', font_family='Times New Roman')
            with Note(default_x=156.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('middle')
                    Text('au', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('middle')
                    Text('n', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wil', font_family='Times New Roman')
            with Note(default_x=193.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-48.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('rig', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('middle')
                    Text('der', font_family='Times New Roman')
                with Lyric(number='3', default_x=2.58, default_y=-99.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('dem', font_family='Times New Roman')
        with Measure(number='5', width=104.56):
            with Note(default_x=26.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.93, default_y=-48.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('bin.', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-74.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('bar', font_family='Times New Roman')
                with Lyric(number='3', default_x=8.82, default_y=-99.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('Weh.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=167.94):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
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
            with Note(default_x=133.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ein', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Ihr', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('er', font_family='Times New Roman')
        with Measure(number='7', width=305.89):
            with Note(default_x=33.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mär', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gol', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('schaut', font_family='Times New Roman')
            with Note(default_x=87.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('middle')
                    Text('den', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht', font_family='Times New Roman')
            with Note(default_x=127.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('es', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('die', font_family='Times New Roman')
            with Note(default_x=171.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Fe', font_family='Times New Roman')
            with Note(default_x=215.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('l', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schm', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('l', font_family='Times New Roman')
            with Note(default_x=259.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten', font_family='Times New Roman')
                with Lyric(number='2', default_x=2.47, default_y=-70.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('eide', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sen', font_family='Times New Roman')
        with Measure(number='8', width=137.97):
            with Note(default_x=20.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Zei', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('blit', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('rif', font_family='Times New Roman')
            with Note(default_x=65.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.75, default_y=-45.0):
                    Syllabic('end')
                    Text('ten,', font_family='Times New Roman')
                with Lyric(number='2', default_x=8.77, default_y=-70.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('zet,', font_family='Times New Roman')
                with Lyric(number='3', default_x=8.84, default_y=-96.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('fe,', font_family='Times New Roman')
            with Note(default_x=103.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('das', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('sie', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('er', font_family='Times New Roman')
        with Measure(number='9', width=282.09):
            with Note(default_x=36.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('kommt', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('kämmt', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('schaut', font_family='Times New Roman')
            with Note(default_x=103.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('mir', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('ihr', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('nur', font_family='Times New Roman')
            with Note(default_x=150.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('go', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('hinauf', font_family='Times New Roman')
            with Note(default_x=197.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('aus', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lde', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman')
            with Note(default_x=238.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-70.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('die', font_family='Times New Roman')
        with Measure(number='10', width=132.0):
            with Note(default_x=26.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.61, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Sinn.', font_family='Times New Roman')
                with Lyric(number='2', default_x=8.81, default_y=-70.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('Haar.', font_family='Times New Roman')
                with Lyric(number='3', default_x=9.24, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('Höh.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=88.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-15.7, default_y=-45.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.Die', font_family='Times New Roman')
                with Lyric(number='2', default_x=-16.1, default_y=-70.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.Sie', font_family='Times New Roman')
                with Lyric(number='3', default_x=-15.7, default_y=-96.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('6.Ich', font_family='Times New Roman')
        with Measure(number='11', width=353.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=85.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lu', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kä', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gla', font_family='Times New Roman')
            with Note(default_x=139.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('ft', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('mmt', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('middle')
                    Text('u', font_family='Times New Roman')
            with Note(default_x=173.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('ist', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman')
                with Lyric(number='3', default_x=8.8, default_y=-103.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('be,', font_family='Times New Roman')
            with Note(default_x=218.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('kühl', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('die', font_family='Times New Roman')
            with Note(default_x=262.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gol', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wel', font_family='Times New Roman')
            with Note(default_x=307.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('es', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('middle')
                    Text('de', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('len', font_family='Times New Roman')
        with Measure(number='12', width=229.81):
            with Note(default_x=24.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dun', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('nem', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ver', font_family='Times New Roman')
            with Note(default_x=111.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('kelt', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Kam', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('schlingen', font_family='Times New Roman')
            with Note(default_x=183.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('me', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('am', font_family='Times New Roman')
        with Measure(number='13', width=287.69):
            with Note(default_x=24.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ru', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('Und', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En', font_family='Times New Roman')
            with Note(default_x=98.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('hig', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('singt', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('de', font_family='Times New Roman')
            with Note(default_x=110.52, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=146.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('begin')
                    Text('flie', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ein', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Schif', font_family='Times New Roman')
            with Note(default_x=193.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('end')
                    Text('ßt', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16):
                    Syllabic('middle')
                    Text('Lied', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('fer', font_family='Times New Roman')
            with Note(default_x=239.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman')
        with Measure(number='14', width=154.79):
            with Note(default_x=31.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.11, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rhein.', font_family='Times New Roman')
                with Lyric(number='2', default_x=8.75, default_y=-77.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('bei.', font_family='Times New Roman')
                with Lyric(number='3', default_x=9.16, default_y=-103.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Kahn.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=117.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.25, relative_y=-30.0):
                    Syllabic('single')
                    Text('der', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-77.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('Das', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-103.07, relative_y=-30.0):
                    Syllabic('single')
                    Text('Und', font_family='Times New Roman')
        with Measure(number='15', width=367.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=85.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gip', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('das', font_family='Times New Roman')
            with Note(default_x=143.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('fel', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ei', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('hat', font_family='Times New Roman')
            with Note(default_x=175.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('des', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit', font_family='Times New Roman')
            with Note(default_x=222.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Be', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wu', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ih', font_family='Times New Roman')
            with Note(default_x=270.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('r', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('und', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('h', font_family='Times New Roman')
            with Note(default_x=318.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('ges', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('rem', font_family='Times New Roman')
        with Measure(number='16', width=225.22):
            with Note(default_x=19.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fun', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sa', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('S', font_family='Times New Roman')
            with Note(default_x=82.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('k', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('me', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('in', font_family='Times New Roman')
            with Note(default_x=121.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('elt', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen', font_family='Times New Roman')
            with Note(default_x=184.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('single')
                    Text('im', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('wal', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('die', font_family='Times New Roman')
        with Measure(number='17', width=267.49):
            with Note(default_x=17.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('tig', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Lo', font_family='Times New Roman')
            with Note(default_x=88.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('bend', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=132.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('so', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Me', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le', font_family='Times New Roman')
            with Note(default_x=177.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('n', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('elo', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('i', font_family='Times New Roman')
            with Note(default_x=221.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-43.75, relative_y=-30.0):
                    Syllabic('middle')
                    Text('nen', font_family='Times New Roman')
                with Lyric(number='2', default_x=6.58, default_y=-69.66, relative_y=-30.0):
                    Syllabic('middle')
                    Text('lo', font_family='Times New Roman')
                with Lyric(number='3', default_x=6.58, default_y=-95.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge', font_family='Times New Roman')
        with Measure(number='18', width=165.61):
            with Note(default_x=32.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.09, default_y=-43.75, relative_y=-30.0):
                    Syllabic('end')
                    Text('schein.', font_family='Times New Roman')
                with Lyric(number='2', default_x=8.95, default_y=-69.66, relative_y=-30.0):
                    Syllabic('end')
                    Text('dei.', font_family='Times New Roman')
                with Lyric(number='3', default_x=8.75, default_y=-95.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')