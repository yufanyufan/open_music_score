with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Ave Verum')
    with Identification():
        Creator('Franz Liszt (1871)\nw/organ ad lib.', type='composer')
        Rights('Copyright © 2014 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded ')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(6.69976)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1772.76)
            PageWidth(1254.12)
            with PageMargins(type='even'):
                LeftMargin(59.7037)
                RightMargin(59.7037)
                TopMargin(59.7037)
                BottomMargin(119.407)
            with PageMargins(type='odd'):
                LeftMargin(59.7037)
                RightMargin(59.7037)
                TopMargin(59.7037)
                BottomMargin(119.407)
        WordFont(font_family='Times New Roman', font_size='12')
        LyricFont(font_family='Times New Roman', font_size='11.4249')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Franz Liszt (1871)\n', default_x=1194.42, default_y=1642.05, justify='right', valign='bottom', font_weight='bold', font_size='10.5347')
        CreditWords('w/organ ad lib.')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Ave Verum', default_x=627.061, default_y=1713.05, justify='center', valign='top', font_weight='bold', font_size='21.0694')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Copyright © 2014 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded ', default_x=627.061, default_y=119.407, justify='center', valign='bottom', font_family='FreeSerif', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Copyright © 2014 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded ', default_x=627.061, default_y=119.407, justify='center', valign='bottom', font_family='FreeSerif', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Copyright © 2014 by CPDL.  This edition can be fully distributed, duplicated, performed, and recorded ', default_x=627.061, default_y=119.407, justify='center', valign='bottom', font_family='FreeSerif', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Sopraan')
            PartAbbreviation('Sop.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Sopraan')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(-24.0)
        with ScorePart(id='P2'):
            PartName('Alt')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alt')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(-16.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(10.0)
        with ScorePart(id='P4'):
            PartName('Bas')
            PartAbbreviation('Bs.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bas')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(17.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P5'):
            PartName('Orgel')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Orgel')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(20)
                Volume(50.3937)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=174.31):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(96.83)
                        RightMargin(-0.0)
                    TopSystemDistance(141.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=40.0):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.36, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Sound(tempo=60.0)
            with Note(default_x=98.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=141.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('ve')
        with Measure(number='2', width=110.94):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=60.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('rum')
        with Measure(number='3', width=118.48):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cor')
            with Note(default_x=58.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('pus')
        with Measure(number='4', width=103.36):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Chri')
        with Measure(number='5', width=78.7):
            with Note(default_x=20.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('sti')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=114.77):
            with Note(default_x=16.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('na')
            with Note(default_x=67.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
        with Measure(number='7', width=102.97):
            with Note(default_x=12.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=56.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Ma')
        with Measure(number='8', width=127.66):
            with Note(default_x=13.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=71.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('a')
        with Measure(number='9', width=106.71):
            with Note(default_x=15.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Vir')
            with Note(default_x=74.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gi')
        with Measure(number='10', width=146.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(60.18)
                        RightMargin(0.0)
                    SystemDistance(300.0)
            with Note(default_x=77.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='11', width=97.69):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=129.94):
            with Direction(placement='above'):
                with DirectionType():
                    Words('espress.', relative_y=25.0, font_weight='bold', font_style='italic', font_family='Bookman Old Style', font_size='11.4249')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=96.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('re')
        with Measure(number='13', width=153.49):
            with Note(default_x=16.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('pas')
            with Note(default_x=74.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=0.84, default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('sum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=127.33):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('im')
            with Note(default_x=83.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mo')
        with Measure(number='15', width=131.72):
            with Note(default_x=16.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('la')
            with Note(default_x=73.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='16', width=136.62):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=43.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=25.0, font_weight='bold', font_style='italic', font_size='11.4249')
            with Note(default_x=73.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cru')
        with Measure(number='17', width=151.1):
            with Note(default_x=17.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('ce')
            with Note(default_x=110.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('single')
                    Text('pro')
        with Measure(number='18', width=209.83):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(60.18)
                        RightMargin(-0.0)
                    TopSystemDistance(150.0)
            with Note(default_x=89.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('down')
                with Notations():
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=171.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
        with Measure(number='19', width=98.23):
            with Note(default_x=14.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_x=0.42, default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
            with Note(default_x=53.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='20', width=122.95):
            with Attributes():
                with Key():
                    Fifths(0)
                    Mode('major')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
        with Measure(number='21', width=124.1):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Cu')
            with Note(default_x=85.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('jus')
        with Measure(number='22', width=123.0):
            with Note(default_x=16.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('la')
            with Note(default_x=61.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('tus')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=119.16):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('per')
            with Note(default_x=85.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('middle')
                    Text('fo')
        with Measure(number='24', width=137.64):
            with Note(default_x=16.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ra')
            with Note(default_x=74.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=139.64):
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=25.0, font_weight='bold', font_style='italic', font_size='11.4249')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=47.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('fu')
            with Note(default_x=103.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('dit')
        with Measure(number='26', width=239.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(60.18)
                        RightMargin(-0.0)
                    SystemDistance(300.0)
            with Note(default_x=70.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('a')
            with Note(default_x=135.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('quam')
            with Note(default_x=189.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('single')
                    Text('cum')
        with Measure(number='27', width=133.29):
            with Direction(placement='above'):
                with DirectionType():
                    Words('molto', default_y=0.84, relative_y=25.0, font_weight='bold', font_style='italic', font_size='11.4249')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=30.0)
            with Note(default_x=17.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('san')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=89.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gui')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='28', width=89.38):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=20.44, relative_y=86.46):
                        Sf()
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=30.0)
            with Note(default_x=13.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-49.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
        with Measure(number='29', width=59.18):
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', default_y=1.68, relative_y=25.0, font_weight='bold', font_style='italic', font_family='Bookman Old Style', font_size='11.4249')
            with Note(default_x=15.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='30', width=94.76):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='31', width=110.86):
            with Attributes():
                with Key():
                    Fifths(2)
                    Mode('major')
            with Direction(placement='above'):
                with DirectionType():
                    Words('dolcissimo', default_y=1.34, relative_y=25.0, font_weight='bold', font_style='italic', font_family='Bookman Old Style', font_size='11.4249')
            with Note(default_x=46.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('E')
            with Note(default_x=86.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=82.04):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=44.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('sto')
        with Measure(number='33', width=82.1):
            with Note(default_x=18.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('no')
            with Note(default_x=57.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=88.36):
            with Note(default_x=12.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('bis')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='35', width=94.75):
            with Note(default_x=18.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-49.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('prae')
            with Note(default_x=69.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=171.56):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(60.18)
                        RightMargin(-0.0)
                    TopSystemDistance(150.0)
            with Note(default_x=92.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=130.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gu')
        with Measure(number='37', width=86.38):
            with Note(default_x=22.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('middle')
                    Text('sta')
            with Note(default_x=61.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='38', width=91.73):
            with Note(default_x=15.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='39', width=92.92):
            with Note(default_x=20.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('begin')
                    Text('mor')
        with Measure(number='40', width=132.76):
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('end')
                    Text('tis')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=70.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=96.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ex')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='41', width=63.6):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=30.0)
            with Note(default_x=20.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('middle')
                    Text('a')
        with Measure(number='42', width=117.94):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=30.0)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=60.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
        with Measure(number='43', width=71.74):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=17.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-48.7, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
        with Measure(number='44', width=58.37):
            with Note(default_x=15.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='45', width=72.76):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='46', width=59.92):
            with Direction(placement='above'):
                with DirectionType():
                    Words('un poco riten.', default_y=1.26, relative_y=25.0, font_weight='bold', font_style='italic', font_family='Bookman Old Style', font_size='11.4249')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=40.0):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.7, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='47', width=54.85):
            with Note(default_x=11.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='48', width=223.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(60.18)
                        RightMargin(-0.0)
                    SystemDistance(300.0)
            with Note(default_x=88.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='49', width=184.4):
            with Note(default_x=17.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.42, default_y=-56.24, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
                    Extend()
            with Note(default_x=99.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='50', width=152.55):
            with Direction(placement='above'):
                with DirectionType():
                    Words('perdendo', relative_y=25.0, font_weight='bold', font_style='italic', font_family='Bookman Old Style', font_size='11.4249')
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-56.24, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='51', width=167.16):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='52', width=184.23):
            with Note(default_x=15.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-56.24, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
                    Extend()
        with Measure(number='53', width=162.3):
            with Note(default_x=15.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=174.31):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=98.43, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=141.65, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('ve')
        with Measure(number='2', width=110.94):
            with Note(default_x=12.0, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=60.49, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('rum')
        with Measure(number='3', width=118.48):
            with Note(default_x=12.0, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cor')
            with Note(default_x=58.45, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('pus')
        with Measure(number='4', width=103.36):
            with Note(default_x=14.96, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Chri')
            with Note(default_x=72.47, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=78.7):
            with Note(default_x=20.67, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('sti')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=114.77):
            with Note(default_x=16.87, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('na')
            with Note(default_x=67.78, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
        with Measure(number='7', width=102.97):
            with Note(default_x=12.36, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=56.69, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Ma')
        with Measure(number='8', width=127.66):
            with Note(default_x=14.0, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=41.23, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.24, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('a')
        with Measure(number='9', width=106.71):
            with Note(default_x=15.84, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Vir')
            with Note(default_x=74.68, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-69.87, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gi')
        with Measure(number='10', width=146.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=77.38, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='11', width=97.69):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=129.94):
            with Note(default_x=12.36, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=96.22, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('end')
                    Text('re')
        with Measure(number='13', width=153.49):
            with Note(default_x=16.56, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('begin')
                    Text('pas')
            with Note(default_x=74.26, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=0.84, default_y=-51.93, relative_y=-25.0):
                    Syllabic('end')
                    Text('sum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=127.33):
            with Note(default_x=12.36, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('begin')
                    Text('im')
            with Note(default_x=83.93, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mo')
        with Measure(number='15', width=131.72):
            with Note(default_x=16.56, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('middle')
                    Text('la')
            with Note(default_x=73.52, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='16', width=136.62):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=43.46, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=73.62, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cru')
        with Measure(number='17', width=151.1):
            with Note(default_x=17.59, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.61, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('end')
                    Text('ce')
            with Note(default_x=110.02, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-51.93, relative_y=-25.0):
                    Syllabic('single')
                    Text('pro')
        with Measure(number='18', width=209.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=89.42, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=171.06, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
        with Measure(number='19', width=98.23):
            with Note(default_x=11.4, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=0.42, default_y=-56.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='20', width=122.95):
            with Attributes():
                with Key():
                    Fifths(0)
                    Mode('major')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
        with Measure(number='21', width=124.1):
            with Note(default_x=12.36, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Cu')
            with Note(default_x=85.54, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('jus')
        with Measure(number='22', width=123.0):
            with Note(default_x=16.87, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('la')
            with Note(default_x=61.83, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('tus')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=119.16):
            with Note(default_x=12.36, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('per')
            with Note(default_x=85.86, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('middle')
                    Text('fo')
        with Measure(number='24', width=137.64):
            with Note(default_x=16.87, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ra')
            with Note(default_x=74.05, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=139.64):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=47.33, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('begin')
                    Text('fu')
            with Note(default_x=103.29, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-56.96, relative_y=-25.0):
                    Syllabic('end')
                    Text('dit')
        with Measure(number='26', width=239.82):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=70.41, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('begin')
                    Text('a')
            with Note(default_x=135.76, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('end')
                    Text('quam')
            with Note(default_x=189.89, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('single')
                    Text('cum')
        with Measure(number='27', width=133.29):
            with Note(default_x=17.59, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=89.88, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gui')
        with Measure(number='28', width=89.38):
            with Note(default_x=13.6, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-62.15, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
        with Measure(number='29', width=59.18):
            with Note(default_x=15.32, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='30', width=94.76):
            with Note(default_x=12.0, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='31', width=110.86):
            with Attributes():
                with Key():
                    Fifths(2)
                    Mode('major')
            with Note(default_x=43.63, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('begin')
                    Text('E')
        with Measure(number='32', width=82.04):
            with Note(default_x=12.36, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.86, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('end')
                    Text('sto')
        with Measure(number='33', width=82.1):
            with Note(default_x=15.32, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('begin')
                    Text('no')
        with Measure(number='34', width=88.36):
            with Note(default_x=12.36, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=44.02, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('end')
                    Text('bis')
                    Extend()
            with Note(default_x=63.59, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=94.75):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-62.15, relative_y=-25.0):
                    Syllabic('begin')
                    Text('prae')
        with Measure(number='36', width=171.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=92.01, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=130.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gu')
        with Measure(number='37', width=86.38):
            with Note(default_x=19.52, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('middle')
                    Text('sta')
        with Measure(number='38', width=91.73):
            with Note(default_x=15.84, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='39', width=92.92):
            with Note(default_x=20.55, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('begin')
                    Text('mor')
        with Measure(number='40', width=132.76):
            with Note(default_x=17.23, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('end')
                    Text('tis')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=70.09, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=96.52, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='41', width=63.6):
            with Note(default_x=20.55, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('middle')
                    Text('a')
        with Measure(number='42', width=117.94):
            with Note(default_x=15.8, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=60.69, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
            with Note(default_x=88.51, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='43', width=71.74):
            with Note(default_x=17.32, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-69.1, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
        with Measure(number='44', width=58.37):
            with Note(default_x=15.32, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='45', width=72.76):
            with Note(default_x=12.36, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='46', width=59.92):
            with Note(default_x=12.0, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-69.1, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='47', width=54.85):
            with Note(default_x=11.8, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
        with Measure(number='48', width=223.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=88.21, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='49', width=184.4):
            with Note(default_x=14.21, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=0.42, default_y=-57.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
        with Measure(number='50', width=152.55):
            with Note(default_x=12.0, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-57.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='51', width=167.16):
            with Note(default_x=14.96, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=90.08, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='52', width=184.23):
            with Note(default_x=15.32, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-57.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
                    Extend()
        with Measure(number='53', width=162.3):
            with Note(default_x=15.32, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=174.31):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=98.43, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=141.65, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('ve')
        with Measure(number='2', width=110.94):
            with Note(default_x=12.0, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=60.49, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('rum')
        with Measure(number='3', width=118.48):
            with Note(default_x=12.0, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cor')
            with Note(default_x=58.81, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('pus')
                    Extend()
            with Note(default_x=87.84, default_y=-340.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=103.36):
            with Note(default_x=14.96, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Chri')
            with Note(default_x=72.47, default_y=-340.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=78.7):
            with Note(default_x=20.67, default_y=-340.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('sti')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=114.77):
            with Note(default_x=16.87, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('na')
            with Note(default_x=67.78, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
        with Measure(number='7', width=102.97):
            with Note(default_x=12.36, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=56.69, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Ma')
        with Measure(number='8', width=127.66):
            with Note(default_x=13.64, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=71.6, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('end')
                    Text('a')
                    Extend()
            with Note(default_x=98.83, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=106.71):
            with Note(default_x=15.84, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Vir')
            with Note(default_x=74.68, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-59.87, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gi')
        with Measure(number='10', width=146.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=77.38, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='11', width=97.69):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
        with Measure(number='12', width=129.94):
            with Note(default_x=12.36, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=96.22, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('re')
        with Measure(number='13', width=153.49):
            with Note(default_x=16.56, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('pas')
            with Note(default_x=74.26, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=0.84, default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('sum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=127.33):
            with Note(default_x=12.36, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('im')
            with Note(default_x=83.93, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mo')
        with Measure(number='15', width=131.72):
            with Note(default_x=16.56, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('middle')
                    Text('la')
            with Note(default_x=73.52, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='16', width=136.62):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=43.46, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=73.62, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cru')
        with Measure(number='17', width=151.1):
            with Note(default_x=17.59, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.61, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('ce')
            with Note(default_x=110.02, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('single')
                    Text('pro')
        with Measure(number='18', width=209.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=89.42, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=171.06, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
        with Measure(number='19', width=98.23):
            with Note(default_x=14.36, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_x=0.42, default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
            with Note(default_x=53.01, default_y=-315.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='20', width=122.95):
            with Attributes():
                with Key():
                    Fifths(0)
                    Mode('major')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
        with Measure(number='21', width=124.1):
            with Note(default_x=12.36, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Cu')
            with Note(default_x=85.54, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('jus')
        with Measure(number='22', width=123.0):
            with Note(default_x=16.87, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('la')
            with Note(default_x=61.83, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('tus')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=119.16):
            with Note(default_x=12.36, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('per')
            with Note(default_x=85.86, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('middle')
                    Text('fo')
        with Measure(number='24', width=137.64):
            with Note(default_x=16.87, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ra')
            with Note(default_x=74.05, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=139.64):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=47.33, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('fu')
            with Note(default_x=103.29, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('dit')
        with Measure(number='26', width=239.82):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=70.41, default_y=-305.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('a')
            with Note(default_x=135.76, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('quam')
            with Note(default_x=189.89, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('single')
                    Text('cum')
        with Measure(number='27', width=133.29):
            with Note(default_x=17.59, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=62.22, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=89.88, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gui')
        with Measure(number='28', width=89.38):
            with Note(default_x=16.56, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=0.42, default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
            with Note(default_x=51.99, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
        with Measure(number='29', width=59.18):
            with Note(default_x=15.32, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='30', width=94.76):
            with Note(default_x=12.0, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='31', width=110.86):
            with Attributes():
                with Key():
                    Fifths(2)
                    Mode('major')
            with Note(default_x=43.63, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('E')
        with Measure(number='32', width=82.04):
            with Note(default_x=12.36, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.86, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('sto')
        with Measure(number='33', width=82.1):
            with Note(default_x=15.32, default_y=-315.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('no')
        with Measure(number='34', width=88.36):
            with Note(default_x=12.36, default_y=-310.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('bis')
                    Extend()
            with Note(default_x=43.66, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=94.75):
            with Note(default_x=18.76, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('prae')
            with Note(default_x=50.06, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
        with Measure(number='36', width=171.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=92.01, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=130.8, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gu')
        with Measure(number='37', width=86.38):
            with Note(default_x=19.52, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('middle')
                    Text('sta')
        with Measure(number='38', width=91.73):
            with Note(default_x=15.84, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='39', width=92.92):
            with Note(default_x=20.55, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('begin')
                    Text('mor')
        with Measure(number='40', width=132.76):
            with Note(default_x=17.23, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('end')
                    Text('tis')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=70.09, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=96.52, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='41', width=63.6):
            with Note(default_x=20.55, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('middle')
                    Text('a')
        with Measure(number='42', width=117.94):
            with Note(default_x=15.8, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.32, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
        with Measure(number='43', width=71.74):
            with Note(default_x=17.32, default_y=-320.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=0.42, default_y=-43.99, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
        with Measure(number='44', width=58.37):
            with Note(default_x=15.32, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
        with Measure(number='45', width=72.76):
            with Note(default_x=12.36, default_y=-325.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='46', width=59.92):
            with Note(default_x=12.0, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-43.99, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='47', width=54.85):
            with Note(default_x=11.8, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='48', width=223.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=88.21, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='49', width=184.4):
            with Note(default_x=14.21, default_y=-330.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=0.42, default_y=-52.36, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
        with Measure(number='50', width=152.55):
            with Note(default_x=12.0, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-52.36, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='51', width=167.16):
            with Note(default_x=12.0, default_y=-340.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='52', width=184.23):
            with Note(default_x=15.32, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-52.36, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
                    Extend()
        with Measure(number='53', width=162.3):
            with Note(default_x=15.32, default_y=-335.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=174.31):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=98.43, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
            with Note(default_x=141.65, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('ve')
        with Measure(number='2', width=110.94):
            with Note(default_x=12.0, default_y=-475.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=60.49, default_y=-475.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('rum')
        with Measure(number='3', width=118.48):
            with Note(default_x=12.0, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cor')
            with Note(default_x=58.45, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('pus')
        with Measure(number='4', width=103.36):
            with Note(default_x=12.0, default_y=-485.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Chri')
        with Measure(number='5', width=78.7):
            with Note(default_x=20.67, default_y=-485.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('sti')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='6', width=114.77):
            with Note(default_x=16.87, default_y=-475.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('na')
            with Note(default_x=67.78, default_y=-475.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
        with Measure(number='7', width=102.97):
            with Note(default_x=12.36, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('single')
                    Text('de')
            with Note(default_x=56.69, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Ma')
        with Measure(number='8', width=127.66):
            with Note(default_x=13.64, default_y=-475.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ri')
            with Note(default_x=71.24, default_y=-475.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('a')
        with Measure(number='9', width=106.71):
            with Note(default_x=15.84, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Vir')
            with Note(default_x=74.68, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_y=-53.33, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gi')
        with Measure(number='10', width=146.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=77.38, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
        with Measure(number='11', width=97.69):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=40.0):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('espress.', relative_y=25.0, font_weight='bold', font_style='italic', font_family='Bookman Old Style', font_size='11.4249')
            with Note(default_x=12.36, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ve')
            with Note(default_x=67.84, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('re')
        with Measure(number='12', width=129.94):
            with Note(default_x=12.36, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('pas')
            with Note(default_x=64.11, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=0.84, default_y=-41.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('sum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='13', width=153.49):
            with Note(default_x=16.56, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('im')
            with Note(default_x=110.09, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mo')
        with Measure(number='14', width=127.33):
            with Note(default_x=12.36, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('la')
            with Note(default_x=56.54, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('single')
                    Text('tum,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='15', width=131.72):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=34.0)
            with Note(default_x=45.22, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=73.52, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('cru')
            with Note(default_x=101.82, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
        with Measure(number='16', width=136.62):
            with Note(default_x=12.94, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.1, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=104.5, default_y=-460.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='17', width=151.1):
            with Note(default_x=17.59, default_y=-460.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('ce')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=110.02, default_y=-460.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-41.83, relative_y=-25.0):
                    Syllabic('single')
                    Text('pro')
        with Measure(number='18', width=209.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=89.42, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=139.8, default_y=-460.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=171.06, default_y=-465.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
        with Measure(number='19', width=98.23):
            with Note(default_x=11.4, default_y=-465.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=0.42, default_y=-48.31, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='20', width=122.95):
            with Attributes():
                with Key():
                    Fifths(0)
                    Mode('major')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=21.6, default_y=-440.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('begin')
                    Text('Cu')
            with Note(default_x=84.39, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('end')
                    Text('jus')
        with Measure(number='21', width=124.1):
            with Note(default_x=12.36, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('begin')
                    Text('la')
            with Note(default_x=57.53, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('end')
                    Text('tus')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='22', width=123.0):
            with Note(default_x=16.87, default_y=-440.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('begin')
                    Text('per')
            with Note(default_x=89.7, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('middle')
                    Text('fo')
        with Measure(number='23', width=119.16):
            with Note(default_x=12.36, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('middle')
                    Text('ra')
            with Note(default_x=57.73, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=137.64):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=38.91)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=45.28, default_y=-440.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('begin')
                    Text('fu')
            with Note(default_x=102.45, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('end')
                    Text('dit')
        with Measure(number='25', width=139.64):
            with Note(default_x=12.94, default_y=-445.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.31, relative_y=-25.0):
                    Syllabic('begin')
                    Text('a')
            with Note(default_x=47.33, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=103.29, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='26', width=239.82):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=70.41, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('quam')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=189.89, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('single')
                    Text('cum')
        with Measure(number='27', width=133.29):
            with Note(default_x=17.59, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('san')
            with Note(default_x=62.22, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=89.88, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gui')
        with Measure(number='28', width=89.38):
            with Note(default_x=16.56, default_y=-450.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=0.42, default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
            with Note(default_x=51.99, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
        with Measure(number='29', width=59.18):
            with Note(default_x=15.32, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='30', width=94.76):
            with Note(default_x=12.0, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='31', width=110.86):
            with Attributes():
                with Key():
                    Fifths(2)
                    Mode('major')
            with Note(default_x=43.63, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('E')
        with Measure(number='32', width=82.04):
            with Note(default_x=12.36, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.86, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('sto')
        with Measure(number='33', width=82.1):
            with Note(default_x=15.32, default_y=-455.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('no')
        with Measure(number='34', width=88.36):
            with Note(default_x=12.36, default_y=-460.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=43.66, default_y=-460.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('end')
                    Text('bis')
        with Measure(number='35', width=94.75):
            with Note(default_x=15.8, default_y=-465.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.83, relative_y=-25.0):
                    Syllabic('begin')
                    Text('prae')
        with Measure(number='36', width=171.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=92.01, default_y=-465.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=130.8, default_y=-465.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('gu')
        with Measure(number='37', width=86.38):
            with Note(default_x=19.52, default_y=-465.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('sta')
        with Measure(number='38', width=91.73):
            with Note(default_x=15.84, default_y=-460.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=47.44, default_y=-465.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('tum')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='39', width=92.92):
            with Note(default_x=20.55, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('mor')
        with Measure(number='40', width=132.76):
            with Note(default_x=17.23, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('tis')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=70.09, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('single')
                    Text('in')
            with Note(default_x=96.52, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('ex')
        with Measure(number='41', width=63.6):
            with Note(default_x=20.55, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('sharp')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('a')
        with Measure(number='42', width=117.94):
            with Note(default_x=15.8, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.32, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('middle')
                    Text('mi')
        with Measure(number='43', width=71.74):
            with Note(default_x=17.32, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-52.06, relative_y=-25.0):
                    Syllabic('end')
                    Text('ne.')
                    Extend()
        with Measure(number='44', width=58.37):
            with Note(default_x=15.32, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='45', width=72.76):
            with Note(default_x=12.36, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='46', width=59.92):
            with Note(default_x=12.0, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-52.06, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='47', width=54.85):
            with Note(default_x=11.8, default_y=-475.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
        with Measure(number='48', width=223.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(110.0)
            with Note(default_x=88.21, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('whole')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='49', width=184.4):
            with Note(default_x=14.21, default_y=-480.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Lyric(number='1', default_x=0.42, default_y=-47.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
        with Measure(number='50', width=152.55):
            with Note(default_x=12.0, default_y=-485.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.33, relative_y=-25.0):
                    Syllabic('begin')
                    Text('A')
        with Measure(number='51', width=167.16):
            with Note(default_x=12.0, default_y=-485.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='52', width=184.23):
            with Note(default_x=15.32, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=0.42, default_y=-47.33, relative_y=-25.0):
                    Syllabic('end')
                    Text('men.')
                    Extend()
        with Measure(number='53', width=162.3):
            with Note(default_x=15.32, default_y=-470.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=174.31):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-490.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(-1)
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
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='2', width=110.94):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='3', width=118.48):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='4', width=103.36):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='5', width=78.7):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='6', width=114.77):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='7', width=102.97):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='8', width=127.66):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='9', width=106.71):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='10', width=146.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-490.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='11', width=97.69):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=12.36, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=67.84, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=129.94):
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.11, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='13', width=153.49):
            with Note(default_x=16.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.56, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.56, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=74.26, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.26, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.26, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=16.56, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=110.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='14', width=127.33):
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.54, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='15', width=131.72):
            with Note(default_x=16.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.56, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.56, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=73.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=73.52, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=73.52, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=16.56, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=101.82, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='16', width=136.62):
            with Note(default_x=9.62, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=9.62, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=9.62, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=12.94, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=43.1, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=104.5, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=151.1):
            with Note(default_x=17.59, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.59, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.59, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=74.25, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=74.25, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=17.59, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=110.02, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=209.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-490.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=89.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=89.42, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=89.42, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=171.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=171.06, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=171.06, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=89.42, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=139.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=171.06, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=98.23):
            with Note(default_x=14.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=14.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=14.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.01, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.01, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=11.4, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='20', width=122.95):
            with Attributes():
                with Key():
                    Fifths(0)
                    Mode('major')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=21.6, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=84.39, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=124.1):
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.36, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=57.53, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='22', width=123.0):
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.87, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=61.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.83, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.83, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=16.87, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=89.7, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='23', width=119.16):
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.36, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=57.73, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='24', width=137.64):
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.87, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=74.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.05, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.05, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=16.87, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=102.45, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='25', width=139.64):
            with Note(default_x=9.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=9.62, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=9.62, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=12.94, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.33, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=103.29, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=239.82):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-490.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=70.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=70.41, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=70.41, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=135.4, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=70.77, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=135.4, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=135.4, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='27', width=133.29):
            with Note(default_x=17.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(4.0)
            with Note(default_x=14.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=17.59, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=17.59, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.86, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=61.86, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=89.38):
            with Note(default_x=13.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=13.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=16.56, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=16.56, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=51.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=51.99, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='29', width=59.18):
            with Note(default_x=18.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=18.28, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=18.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=18.28, default_y=5.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='30', width=94.76):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='31', width=110.86):
            with Attributes():
                with Key():
                    Fifths(2)
                    Mode('major')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='32', width=82.04):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='33', width=82.1):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='34', width=88.36):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='35', width=94.75):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='36', width=171.56):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-490.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='37', width=86.38):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='38', width=91.73):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='39', width=92.92):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=20.55, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Note(default_x=20.55, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=20.55, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Note(default_x=20.55, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
        with Measure(number='40', width=132.76):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='41', width=63.6):
            with Note(default_x=20.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=20.55, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('whole')
                Accidental('sharp')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Backup():
                Duration(4.0)
            with Note(default_x=20.55, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=20.55, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='42', width=117.94):
            with Note(default_x=12.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(4.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=88.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.84, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.84, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='43', width=71.74):
            with Note(default_x=17.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=17.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('whole')
                Accidental('natural')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(4.0)
            with Note(default_x=17.32, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(default_x=17.32, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='44', width=58.37):
            with Note(default_x=15.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(4.0)
            with Note(default_x=15.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(4.0)
            with Note(default_x=15.32, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(default_x=15.32, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='45', width=72.76):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='46', width=59.92):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='47', width=54.85):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='48', width=223.9):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-490.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='49', width=184.4):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='50', width=152.55):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='51', width=167.16):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='52', width=184.23):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='53', width=162.3):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')