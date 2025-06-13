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
            Millimeters(6.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1898.5)
            PageWidth(1343.08)
            with PageMargins(type='even'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
            with PageMargins(type='odd'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Großer Gott, wir loben dich\n', default_x=671.541, default_y=1834.57, justify='center', valign='top', font_family='Times New Roman', font_size='16')
        CreditWords('Grand Dieu, nous te bénisons\n')
        CreditWords('Holy God, we praise Thy Name')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Katholisches Gesangbuch (Wien 1776)', default_x=1279.14, default_y=1670.28, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Ig\xadnaz Franz (Deutsch)\n', default_x=63.9387, default_y=1670.28, justify='left', valign='bottom', font_family='Times New Roman')
        CreditWords('Henri-Louis Empaytaz (Français)\n')
        CreditWords('Clar\xadence A. Wal\xadworth (English)')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Organ', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Organ')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=222.28):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.85)
                        RightMargin(-0.0)
                    TopSystemDistance(234.29)
                with StaffLayout(number=2):
                    StaffDistance(183.55)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=99.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-74.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gros', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('Grand', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-126.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ho', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=174.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('ser', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=9.03, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('Dieu,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=99.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=174.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=99.27, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=174.12, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=99.27, default_y=-263.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=99.27, default_y=-228.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=174.12, default_y=-263.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.12, default_y=-228.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=129.88):
            with Note(default_x=12.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('nous', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_x=0.9, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('God,', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=51.24, default_y=-35.0):
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
            with Note(default_x=89.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('wir', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('Te', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('we', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=89.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.72, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.24, default_y=-223.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=89.76, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.72, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=51.24, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=89.76, default_y=-253.55):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=148.85):
            with Note(default_x=12.36, default_y=-25.0):
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
                with Lyric(number='1', default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('lo', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('bé', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('praise', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=57.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('ben', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nis', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=57.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.29, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=102.29, default_y=-233.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-248.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=57.32, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.29, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=97.58):
            with Note(default_x=31.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.69, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('dich,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=8.72, default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('sons,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=8.85, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Name;', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=31.53, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=31.53, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=31.53, default_y=-263.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='5', width=124.98):
            with Note(default_x=28.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Herr', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nous', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lord', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=86.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('wir', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('cé', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('of', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=86.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=86.95, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=86.95, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=146.21):
            with Note(default_x=16.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('prei', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('lé', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_x=0.45, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('all,', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=58.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('sen', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('brons', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('we', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=16.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=58.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=101.79, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=16.16, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=58.98, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.79, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=164.83):
            with Note(default_x=24.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('dei', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('tes', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('bow', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=67.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=109.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('lou', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fore', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=24.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=109.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=24.45, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=109.99, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=24.45, default_y=-233.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=109.99, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=136.61, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=158.75):
            with Note(default_x=23.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Stär', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('middle')
                    Text('an', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thee!', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=85.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.8, default_y=-74.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ke.', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=9.6, default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('ges!', font_family='Times New Roman', font_size='11.2781')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=85.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.01, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.08, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.01, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=85.08, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='9', width=169.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.85)
                        RightMargin(0.0)
                    SystemDistance(121.13)
                with StaffLayout(number=2):
                    StaffDistance(183.55)
            with Note(default_x=78.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Vor', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('E', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('All', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=133.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ter', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('on', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=133.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=133.73, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-263.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=78.21, default_y=-228.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=133.73, default_y=-263.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=133.73, default_y=-228.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=183.68):
            with Note(default_x=18.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nei', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=0.45, default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('nel,', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Earth', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=73.21, default_y=-35.0):
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
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('gt', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=127.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('die', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('nous', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=18.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=127.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=18.73, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.21, default_y=-223.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=127.65, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=18.73, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=73.21, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=127.65, default_y=-253.55):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=127.91):
            with Note(default_x=12.36, default_y=-25.0):
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
                with Lyric(number='1', default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Er', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text("t'e", font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('scep', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=50.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('de', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('xal', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('ter', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=50.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=88.33, default_y=-233.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-248.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=50.34, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=88.33, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=101.17):
            with Note(default_x=29.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('sich', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=8.4, default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('tons,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=8.69, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('claim,', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=29.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=29.65, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=29.65, default_y=-263.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='13', width=121.35):
            with Note(default_x=21.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('und', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('De', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('All', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=82.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('con', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=21.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=82.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=21.97, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=82.29, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=21.97, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=82.29, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=187.12):
            with Note(default_x=23.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-74.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('wun', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('cert', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hea', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=77.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('ven', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=131.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('dert', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=77.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=22.88, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=131.43, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.24, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=77.33, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.43, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=152.42):
            with Note(default_x=16.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('dei', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('vec', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-126.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('bove', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=57.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('ne', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('les', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=99.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=99.03, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-233.55):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=99.03, default_y=-228.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=124.93, default_y=-218.55):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=149.89):
            with Note(default_x=25.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-74.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wer', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-100.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('an', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-126.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('dore', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=71.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.8, default_y=-74.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ke.', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=9.15, default_y=-100.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('ges,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=9.09, default_y=-126.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thee;', font_family='Times New Roman', font_size='11.2781')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=25.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=71.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=25.04, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=71.2, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=25.04, default_y=-208.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.2, default_y=-243.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='17', width=179.53):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.85)
                        RightMargin(0.0)
                    SystemDistance(121.13)
                with StaffLayout(number=2):
                    StaffDistance(174.36)
            with Note(default_x=78.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Et', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-112.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('In', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=139.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('du', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-86.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pros', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-112.45, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fi', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=139.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=139.71, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-234.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=139.71, default_y=-244.36):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=151.9):
            with Note(default_x=22.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('war', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_y=-86.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-112.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('nite', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=64.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('st', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=107.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('vor', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('nés', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-112.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=22.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=64.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=22.33, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.99, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.64, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=22.33, default_y=-249.36):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=64.99, default_y=-234.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.64, default_y=-234.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=124.42):
            with Note(default_x=23.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-60.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-86.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('de', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-112.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('vast', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=84.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-86.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('vant', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-112.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=84.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.1, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=84.6, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.1, default_y=-219.36):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=84.6, default_y=-229.36):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=88.27):
            with Note(default_x=27.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.04, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zeit,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=8.61, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Toi,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=8.71, default_y=-112.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('main,', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=27.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.15, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.15, default_y=-244.36):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='21', width=161.02):
            with Note(default_x=28.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('so', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nous', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-112.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('E', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=109.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('bleibst', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-86.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text("t'a", font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-112.45, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ver', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=109.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-204.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=109.13, default_y=-204.36):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-239.36):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=109.13, default_y=-229.36):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=125.8):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('du', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-86.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('do', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-112.45, relative_y=-30.0):
                    Syllabic('end')
                    Text('las', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=48.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=9.04, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('rons,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-112.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('ting', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-214.36):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=83.73, default_y=-219.36):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-224.36):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.04, default_y=-234.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.73, default_y=-229.36):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=146.56):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('E', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('ô', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-112.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=58.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wig', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('grand', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-112.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=101.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-194.36):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.85, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.9, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-239.36):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=58.85, default_y=-234.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.9, default_y=-234.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=91.0):
            with Note(default_x=27.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.48, default_y=-60.5, relative_y=-30.0):
                    Syllabic('end')
                    Text('keit.', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=9.1, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Roi!', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=8.77, default_y=-112.45, relative_y=-30.0):
                    Syllabic('single')
                    Text('reign.', font_family='Times New Roman', font_size='11.2781')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.77, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Backup():
                Duration(6.0)
            with Note(default_x=27.77, default_y=-219.36):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='25', width=124.87):
            with Note(default_x=23.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('Wie', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-86.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('Et', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-112.45, relative_y=-30.0):
                    Syllabic('begin')
                    Text('In', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=85.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-60.5, relative_y=-30.0):
                    Syllabic('single')
                    Text('du', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-86.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pros', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-112.45, relative_y=-30.0):
                    Syllabic('middle')
                    Text('fi', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=85.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.55, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=85.05, default_y=-199.36):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.55, default_y=-234.36):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=85.05, default_y=-244.36):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=248.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.85)
                        RightMargin(-0.0)
                    SystemDistance(121.13)
                with StaffLayout(number=2):
                    StaffDistance(177.56)
            with Note(default_x=78.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('war', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_y=-88.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-113.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('nite', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=134.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('st', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=190.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-62.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('vor', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-88.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('nés', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-113.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=134.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=190.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-197.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=134.55, default_y=-202.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=190.88, default_y=-202.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=78.21, default_y=-252.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=134.55, default_y=-237.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=190.88, default_y=-237.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=165.45):
            with Note(default_x=23.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-62.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-88.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text('de', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-113.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('vast', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=109.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-62.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('ler', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-88.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('vant', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-113.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=23.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=109.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.1, default_y=-202.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=109.85, default_y=-197.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=23.1, default_y=-222.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=109.85, default_y=-232.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=129.3):
            with Note(default_x=27.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=9.04, default_y=-62.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('Zeit,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=8.61, default_y=-88.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('Toi,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=8.71, default_y=-113.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('main,', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=27.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.15, default_y=-202.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.15, default_y=-247.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='29', width=188.8):
            with Note(default_x=28.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.22, default_y=-62.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('so', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.22, default_y=-88.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('Nous', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.22, default_y=-113.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('E', font_family='Times New Roman', font_size='11.2781')
            with Note(default_x=126.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-62.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('bleibst', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-88.01, relative_y=-30.0):
                    Syllabic('begin')
                    Text("t'a", font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-113.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('ver', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=126.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-207.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=126.22, default_y=-207.56):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=28.29, default_y=-242.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=126.22, default_y=-232.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=154.93):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-62.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('du', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-88.01, relative_y=-30.0):
                    Syllabic('end')
                    Text('do', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-113.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('las', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=59.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=106.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-62.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('in', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=9.04, default_y=-88.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('rons,', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-113.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('ting', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=59.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=106.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-217.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=106.34, default_y=-222.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-227.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=59.35, default_y=-237.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=106.34, default_y=-232.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=174.45):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-62.04, relative_y=-30.0):
                    Syllabic('single')
                    Text('E', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='2', default_y=-88.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('ô', font_family='Times New Roman', font_size='11.2781')
                    Extend()
                with Lyric(number='3', default_y=-113.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('is', font_family='Times New Roman', font_size='11.2781')
                    Extend()
            with Note(default_x=68.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=6.58, default_y=-62.04, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wig', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=6.58, default_y=-88.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('grand', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=6.58, default_y=-113.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Thy', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=120.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-197.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.15, default_y=-202.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.5, default_y=-202.56):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-242.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.15, default_y=-237.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.5, default_y=-237.56):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=131.62):
            with Note(default_x=27.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Lyric(number='1', default_x=8.48, default_y=-62.04, relative_y=-30.0):
                    Syllabic('end')
                    Text('keit.', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='2', default_x=8.65, default_y=-88.01, relative_y=-30.0):
                    Syllabic('single')
                    Text('Roi.', font_family='Times New Roman', font_size='11.2781')
                with Lyric(number='3', default_x=8.77, default_y=-113.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('reign.', font_family='Times New Roman', font_size='11.2781')
            with Backup():
                Duration(6.0)
            with Note(default_x=27.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.77, default_y=-212.56):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=27.77, default_y=-222.56):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')