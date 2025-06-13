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
            Millimeters(5.6896)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2142.86)
            PageWidth(1517.86)
            with PageMargins(type='even'):
                LeftMargin(69.6429)
                RightMargin(69.6429)
                TopMargin(69.6429)
                BottomMargin(141.071)
            with PageMargins(type='odd'):
                LeftMargin(69.6429)
                RightMargin(69.6429)
                TopMargin(69.6429)
                BottomMargin(141.071)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Lacrymosa', default_x=758.929, default_y=2073.21, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('From "Requiem in D Minor", K. 626', default_x=758.929, default_y=2002.91, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Wolfgang Amadeus Mozart', default_x=1448.21, default_y=1870.29, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(50.3937)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(42.5197)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(42.5197)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(43.3071)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P5'):
            PartName('Piano', print_object='no')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(1)
                Volume(50.3937)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=656.18):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(185.98)
                        RightMargin(-0.0)
                    TopSystemDistance(592.06)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Lacrymosa dies illa,Qua resurget ex favillaJudicandus homo reus.Huic ergo parce, Deus,Pie Jesu Domine,Dona eis requiem. Amen.', relative_x=-98.25, relative_y=254.26, font_style='italic', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Larghetto', default_x=-47.49, default_y=258.7, relative_x=-46.12, relative_y=20.4, font_weight='bold', font_family='Times New Roman', font_size='12.3782')
                Sound(tempo=60.0)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='2', width=536.42):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='3', width=477.87):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=3.29, relative_y=22.06):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=179.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.75, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=244.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cry', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=280.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mo', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=378.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=9.19, default_y=-46.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='4', width=403.24):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=112.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=144.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=176.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('es', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=208.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=305.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=8.95, default_y=-46.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=441.8):
            with Note(default_x=21.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-46.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=231.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-46.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=336.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('get', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=497.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=81.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=192.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_y=-51.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=293.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_y=-51.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=394.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('la', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=409.78):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-22.03, relative_y=27.51):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_x=-4.61, relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=114.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di', font_family='Times New Roman', font_size='11.1404')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=4.04, relative_y=26.46):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=212.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=310.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='8', width=415.5):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=4.03, relative_y=23.62):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=113.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman', font_size='11.1404')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=7.49, relative_y=34.22):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=213.95, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=313.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.06, default_y=-51.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=495.63):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-26.81, relative_y=18.94):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Sotto voce.', relative_x=-40.35, relative_y=44.61, font_family='Times New Roman')
            with Note(default_x=89.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-44.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=190.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=258.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cry', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=291.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-44.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mo', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=392.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=426.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=460.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa', font_family='Times New Roman', font_size='11.1404')
        with Measure(number='10', width=415.29):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-44.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=116.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=182.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('es', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=215.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=314.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.95, default_y=-44.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='11', width=411.99):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=7.15, relative_y=27.31):
                        Mf()
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=32.31)
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-44.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua', font_family='Times New Roman', font_size='11.1404')
                    Extend()
            with Note(default_x=114.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.6, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-52.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=5.37, relative_x=12.43, relative_y=21.94):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=180.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=213.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur', font_family='Times New Roman', font_size='11.1404')
            with Note(default_x=311.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('get', font_family='Times New Roman', font_size='11.1404')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=453.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=86.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex', font_family='Times New Roman')
                    Extend()
            with Note(default_x=175.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=205.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=235.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa', font_family='Times New Roman')
            with Note(default_x=265.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vil', font_family='Times New Roman')
            with Note(default_x=354.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('la', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='13', width=460.67):
            with Note(default_x=16.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju', font_family='Times New Roman')
            with Note(default_x=126.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=163.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=200.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di', font_family='Times New Roman')
            with Note(default_x=237.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can', font_family='Times New Roman')
            with Note(default_x=348.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='14', width=408.93):
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho', font_family='Times New Roman')
            with Note(default_x=117.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=181.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=27.25)
            with Note(default_x=214.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=310.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.79, default_y=-41.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-22.28)
        with Measure(number='15', width=487.53):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=9.45, relative_y=21.58):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hu', font_family='Times New Roman')
            with Note(default_x=190.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('ic', font_family='Times New Roman')
            with Note(default_x=290.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er', font_family='Times New Roman')
            with Note(default_x=388.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('go', font_family='Times New Roman')
        with Measure(number='16', width=425.41):
            with Note(default_x=36.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par', font_family='Times New Roman')
            with Note(default_x=133.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('ce', font_family='Times New Roman')
            with Note(default_x=230.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De', font_family='Times New Roman')
            with Note(default_x=327.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.79, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('us,', font_family='Times New Roman')
        with Measure(number='17', width=409.97):
            with Note(default_x=25.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi', font_family='Times New Roman')
            with Note(default_x=121.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=217.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je', font_family='Times New Roman')
            with Note(default_x=312.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=0.5, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,', font_family='Times New Roman')
                    Extend()
            with Note(default_x=376.5, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='18', width=501.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=77.5, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je', font_family='Times New Roman')
            with Note(default_x=182.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=217.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=252.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('su', font_family='Times New Roman')
            with Note(default_x=289.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-46.07, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do', font_family='Times New Roman')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=394.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=429.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=464.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.07, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi', font_family='Times New Roman')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=375.62):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=0.54, relative_y=22.67):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.43, default_y=-46.07, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne!', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='20', width=446.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='21', width=478.67):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='22', width=421.28):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=6.03, relative_x=0.4, relative_y=13.08):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do', font_family='Times New Roman')
            with Note(default_x=116.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
            with Note(default_x=217.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=318.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('is', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='23', width=422.97):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman')
            with Note(default_x=117.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui', font_family='Times New Roman')
            with Note(default_x=218.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=0.5, default_y=-45.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('em,', font_family='Times New Roman')
                    Extend()
            with Note(default_x=319.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='24', width=474.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=274.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Note(default_x=374.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
        with Measure(number='25', width=441.79):
            with Note(default_x=20.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=125.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.73, default_y=-46.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('is,', font_family='Times New Roman')
            with Note(default_x=230.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Note(default_x=335.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
        with Measure(number='26', width=406.69):
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=15.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=113.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('is', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=3.34, relative_x=9.67, relative_y=8.01):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=210.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-46.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.81, relative_x=7.07, relative_y=10.05):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=307.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='27', width=470.42):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(55.66)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=93.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=186.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=278.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=15.37, relative_y=19.54):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=371.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui', font_family='Times New Roman')
        with Measure(number='28', width=394.81):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=11.41, relative_y=19.05):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=18.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.13, default_y=-41.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('em.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='29', width=350.43):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-6.13, relative_y=18.96):
                        Ff()
                Sound(dynamics=140.0)
            with Note(default_x=15.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-41.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    Words('rit.', relative_x=-4.45, relative_y=18.7, font_style='italic', font_family='Times New Roman', font_size='12.3782')
                Offset(-5.0)
                Sound(tempo=54.0)
        with Measure(number='30', width=107.26):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=-19.6, relative_y=34.24):
                        BeatUnit('quarter')
                        PerMinute('56')
                Sound(tempo=48.0)
            with Note(default_x=20.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=12.2, default_y=-41.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=656.18):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='2', width=536.42):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='3', width=477.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.47)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=2.03, relative_y=21.53):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-168.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-55.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La')
            with Note(default_x=179.11, default_y=-168.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.75, default_y=-178.47):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=244.39, default_y=-158.47):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('cry')
            with Note(default_x=280.42, default_y=-163.47):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mo')
            with Note(default_x=378.35, default_y=-163.47):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.0, default_y=-55.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='4', width=403.24):
            with Note(default_x=15.8, default_y=-168.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-55.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di')
            with Note(default_x=112.26, default_y=-168.47):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=144.41, default_y=-178.47):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=176.57, default_y=-158.47):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
            with Note(default_x=208.72, default_y=-163.47):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il')
            with Note(default_x=305.18, default_y=-163.47):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.7, default_y=-55.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=441.8):
            with Note(default_x=21.54, default_y=-193.47):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.77, default_y=-183.47):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-55.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=231.91, default_y=-178.47):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-55.52, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=336.05, default_y=-173.47):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('get')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=497.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(120.91)
            with Note(default_x=81.18, default_y=-195.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=192.6, default_y=-215.91):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_y=-55.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=293.75, default_y=-200.91):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-55.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=394.89, default_y=-190.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=409.78):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-11.4, relative_y=20.6):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=16.2, default_y=-190.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-4.13, relative_y=18.57):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=114.19, default_y=-190.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Note(default_x=212.19, default_y=-195.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=7.27, relative_y=26.95):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=310.18, default_y=-185.91):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus')
        with Measure(number='8', width=415.5):
            with Note(default_x=14.0, default_y=-190.91):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=4.18, relative_y=25.78):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=113.98, default_y=-170.91):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo')
            with Note(default_x=213.95, default_y=-170.91):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=313.93, default_y=-175.91):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=8.64, default_y=-55.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=495.63):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(116.55)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=4.59, relative_x=-27.85, relative_y=15.86):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('S.v.', relative_x=-34.59, relative_y=38.85, font_family='Times New Roman')
            with Note(default_x=89.42, default_y=-186.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La')
            with Note(default_x=190.57, default_y=-186.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=258.01, default_y=-186.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cry')
            with Note(default_x=291.72, default_y=-191.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mo')
            with Note(default_x=392.88, default_y=-191.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=426.6, default_y=-201.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=460.31, default_y=-181.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa')
        with Measure(number='10', width=415.29):
            with Note(default_x=17.23, default_y=-186.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di')
            with Note(default_x=116.35, default_y=-186.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=182.42, default_y=-206.55):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
            with Note(default_x=215.46, default_y=-181.55):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il')
            with Note(default_x=314.57, default_y=-191.55):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.7, default_y=-48.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='11', width=411.99):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=7.38, relative_x=1.58, relative_y=26.83):
                        Mf()
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=39.21)
            with Note(default_x=16.2, default_y=-176.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.55, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua')
                    Extend()
            with Note(default_x=114.75, default_y=-176.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-33.42)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=8.16, relative_x=13.55, relative_y=26.05):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=147.6, default_y=-186.55):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=180.45, default_y=-176.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=213.3, default_y=-176.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur')
            with Note(default_x=311.84, default_y=-176.55):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('get')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=453.31):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.97)
            with Note(default_x=86.18, default_y=-159.97):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-48.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
                    Extend()
            with Note(default_x=175.76, default_y=-159.97):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=235.47, default_y=-164.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa')
            with Note(default_x=265.33, default_y=-169.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vil')
            with Note(default_x=354.91, default_y=-169.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=384.77, default_y=-154.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Lyric(number='1', default_y=-48.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
                    Extend()
            with Note(default_x=418.94, default_y=-159.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
        with Measure(number='13', width=460.67):
            with Note(default_x=16.2, default_y=-159.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_y=-48.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju')
            with Note(default_x=126.92, default_y=-164.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=200.73, default_y=-164.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Note(default_x=237.64, default_y=-164.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.95, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can')
            with Note(default_x=348.36, default_y=-164.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='14', width=408.93):
            with Note(default_x=21.03, default_y=-174.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-48.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=117.61, default_y=-174.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.8, default_y=-159.97):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=181.99, default_y=-164.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=32.34)
            with Note(default_x=214.18, default_y=-164.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.95, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=310.75, default_y=-169.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.64, default_y=-48.95, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-29.71)
        with Measure(number='15', width=487.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.85)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=5.41, relative_y=21.65):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hu')
            with Note(default_x=190.26, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ie')
            with Note(default_x=290.18, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=388.06, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('go')
        with Measure(number='16', width=425.41):
            with Note(default_x=36.87, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
            with Note(default_x=133.6, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('ce')
            with Note(default_x=230.34, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Note(default_x=327.07, default_y=-158.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-45.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('us,')
        with Measure(number='17', width=409.97):
            with Note(default_x=25.87, default_y=-163.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi')
            with Note(default_x=121.49, default_y=-163.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=217.12, default_y=-163.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=312.75, default_y=-183.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.14, default_y=-45.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
        with Measure(number='18', width=501.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=77.5, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=182.33, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=217.27, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=252.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('su')
            with Note(default_x=289.99, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-51.55, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=394.82, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=464.7, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.55, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=375.62):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=2.09, relative_y=14.09):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.6, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.55, default_y=-51.55, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne!')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='20', width=446.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='21', width=478.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.54)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='22', width=421.28):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-4.21, relative_y=17.65):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-171.54):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=116.77, default_y=-171.54):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.43, default_y=-181.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=184.08, default_y=-161.54):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=217.74, default_y=-166.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=318.71, default_y=-166.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('is')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='23', width=422.97):
            with Note(default_x=15.8, default_y=-171.54):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=117.19, default_y=-171.54):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.99, default_y=-181.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=184.79, default_y=-161.54):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.02, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui')
            with Note(default_x=218.58, default_y=-166.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('em')
                    Extend()
            with Note(default_x=319.98, default_y=-166.54):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='24', width=474.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(115.4)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='25', width=441.79):
            with Note(default_x=20.0, default_y=-195.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Note(default_x=125.05, default_y=-195.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
            with Note(default_x=230.09, default_y=-195.4):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=335.14, default_y=-200.4):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.73, default_y=-59.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('is,', font_family='Times New Roman')
        with Measure(number='26', width=406.69):
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=15.83, default_y=-210.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=3.25, relative_x=5.35, relative_y=8.1):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=113.15, default_y=-210.4):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.18, relative_x=3.9, relative_y=10.68):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=210.46, default_y=-215.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=307.78, default_y=-215.4):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('is', font_family='Times New Roman')
        with Measure(number='27', width=470.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.78)
            with Note(default_x=93.22, default_y=-178.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-49.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=17.74, relative_y=12.1):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=185.7, default_y=-173.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=371.73, default_y=-178.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-49.98, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui', font_family='Times New Roman')
        with Measure(number='28', width=394.81):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=7.51, relative_x=6.58, relative_y=3.35):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=18.25, default_y=-173.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.13, default_y=-49.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('em.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='29', width=350.43):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=0.26, relative_y=13.92):
                        Ff()
                Sound(dynamics=140.0)
            with Note(default_x=15.32, default_y=-158.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=3.26, default_y=-49.98, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman')
        with Measure(number='30', width=107.26):
            with Note(default_x=20.55, default_y=-163.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('sharp')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=5.56, default_y=-49.98, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=656.18):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='2', width=536.42):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='3', width=477.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.37)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-1.27, relative_y=15.94):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-280.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La')
            with Note(default_x=179.11, default_y=-280.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.75, default_y=-295.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=244.39, default_y=-305.84):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('cry')
            with Note(default_x=280.42, default_y=-290.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mo')
            with Note(default_x=378.35, default_y=-295.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.0, default_y=-46.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='4', width=403.24):
            with Note(default_x=15.8, default_y=-295.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-46.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di')
            with Note(default_x=112.26, default_y=-295.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=176.57, default_y=-305.84):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
            with Note(default_x=208.72, default_y=-290.84):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il')
            with Note(default_x=305.18, default_y=-295.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.7, default_y=-46.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=441.8):
            with Note(default_x=21.54, default_y=-305.84):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.77, default_y=-295.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-46.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=231.91, default_y=-295.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-46.78, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=336.05, default_y=-285.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('get')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=497.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(124.87)
            with Note(default_x=81.18, default_y=-340.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=192.6, default_y=-355.77):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=293.75, default_y=-350.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-50.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=394.89, default_y=-345.77):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=409.78):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-16.79, relative_y=13.4):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=16.2, default_y=-340.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju')
            with Note(default_x=114.19, default_y=-340.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-1.2, relative_y=15.38):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=212.19, default_y=-340.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can')
            with Note(default_x=310.18, default_y=-330.77):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus')
        with Measure(number='8', width=415.5):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-7.5, relative_y=20.92):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=14.0, default_y=-335.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=113.98, default_y=-325.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-3.0, relative_y=25.11):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=213.95, default_y=-325.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=313.93, default_y=-330.77):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=8.64, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=495.63):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(117.42)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=0.21, relative_x=-35.34, relative_y=20.25):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('S.v.', relative_x=-39.2, relative_y=38.85, font_family='Times New Roman')
            with Note(default_x=89.42, default_y=-318.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La')
            with Note(default_x=190.57, default_y=-318.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.29, default_y=-323.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=258.01, default_y=-328.97):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cry')
            with Note(default_x=291.72, default_y=-323.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mo')
            with Note(default_x=392.88, default_y=-323.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=426.6, default_y=-338.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=460.31, default_y=-348.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa')
        with Measure(number='10', width=415.29):
            with Note(default_x=17.23, default_y=-333.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di')
            with Note(default_x=116.35, default_y=-333.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.38, default_y=-338.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=182.42, default_y=-338.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
            with Note(default_x=215.46, default_y=-338.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il')
            with Note(default_x=314.57, default_y=-338.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.7, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='11', width=411.99):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=2.89, relative_x=3.43, relative_y=27.68):
                        Mf()
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.56)
            with Note(default_x=16.2, default_y=-318.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua')
                    Extend()
            with Note(default_x=114.75, default_y=-318.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-22.28)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=14.03, relative_x=8.39, relative_y=16.53):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=147.6, default_y=-333.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=180.45, default_y=-308.97):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=213.3, default_y=-313.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur')
            with Note(default_x=311.84, default_y=-313.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('get')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=453.31):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(107.28)
            with Note(default_x=86.18, default_y=-282.25):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.03, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
                    Extend()
            with Note(default_x=175.76, default_y=-282.25):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=205.61, default_y=-292.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=235.47, default_y=-307.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa')
            with Note(default_x=265.33, default_y=-292.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vil')
            with Note(default_x=354.91, default_y=-292.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='13', width=460.67):
            with Note(default_x=16.2, default_y=-282.25):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju')
            with Note(default_x=126.92, default_y=-282.25):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=163.82, default_y=-292.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=200.73, default_y=-302.25):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Note(default_x=237.64, default_y=-312.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.03, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can')
            with Note(default_x=348.36, default_y=-312.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=385.26, default_y=-297.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=422.17, default_y=-302.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus')
        with Measure(number='14', width=408.93):
            with Note(default_x=21.03, default_y=-302.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-51.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=117.61, default_y=-302.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=149.8, default_y=-307.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=181.99, default_y=-287.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=36.72)
            with Note(default_x=214.18, default_y=-287.25):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.03, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=310.75, default_y=-292.25):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.64, default_y=-51.03, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.42)
        with Measure(number='15', width=487.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(99.45)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=2.11, relative_y=28.01):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hu')
            with Note(default_x=190.26, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ie')
            with Note(default_x=290.18, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=388.06, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('go')
        with Measure(number='16', width=425.41):
            with Note(default_x=36.87, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
            with Note(default_x=133.6, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ce')
            with Note(default_x=230.34, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Note(default_x=327.07, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.89, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('us,')
        with Measure(number='17', width=409.97):
            with Note(default_x=25.87, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi')
            with Note(default_x=121.49, default_y=-278.3):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=217.12, default_y=-278.3):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=312.75, default_y=-273.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.14, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
        with Measure(number='18', width=501.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(74.7)
            with Note(default_x=77.5, default_y=-239.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=182.33, default_y=-244.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=252.21, default_y=-244.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('su')
            with Note(default_x=289.99, default_y=-244.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=394.82, default_y=-239.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=464.7, default_y=-239.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=375.62):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=1.97, relative_x=2.96, relative_y=16.63):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.6, default_y=-244.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.55, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne!')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='20', width=446.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='21', width=478.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.77)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='22', width=421.28):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-5.2, relative_y=15.9):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-281.31):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=116.77, default_y=-281.31):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.43, default_y=-296.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.08, default_y=-306.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=217.74, default_y=-291.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=318.71, default_y=-296.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('is')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='23', width=422.97):
            with Note(default_x=15.8, default_y=-296.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-41.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=117.19, default_y=-296.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.79, default_y=-306.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui')
            with Note(default_x=218.58, default_y=-291.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_y=-41.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('em')
                    Extend()
            with Note(default_x=319.98, default_y=-296.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='24', width=474.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(129.37)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=274.91, default_y=-334.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Note(default_x=374.69, default_y=-324.77):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
        with Measure(number='25', width=441.79):
            with Note(default_x=20.0, default_y=-319.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=125.05, default_y=-354.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.73, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('is,', font_family='Times New Roman')
            with Note(default_x=230.09, default_y=-344.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Note(default_x=335.14, default_y=-349.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
        with Measure(number='26', width=406.69):
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=15.83, default_y=-354.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=113.15, default_y=-359.77):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.77, relative_y=-30.0):
                    Syllabic('end')
                    Text('is', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=4.51, relative_x=7.36, relative_y=6.84):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=210.46, default_y=-364.77):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-47.77, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=1.3, relative_y=13.68):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=307.78, default_y=-359.77):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='27', width=470.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(100.61)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=2.96, relative_x=11.43, relative_y=15.65):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.86, default_y=-294.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=278.89, default_y=-294.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=371.73, default_y=-294.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui', font_family='Times New Roman')
        with Measure(number='28', width=394.81):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=6.81, relative_x=12.62, relative_y=11.8):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=18.25, default_y=-294.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.13, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('em.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='29', width=350.43):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=2.56, relative_y=16.78):
                        Ff()
                Sound(dynamics=140.0)
            with Note(default_x=15.32, default_y=-289.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman')
        with Measure(number='30', width=107.26):
            with Note(default_x=20.55, default_y=-294.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=5.56, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=656.18):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='2', width=536.42):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='3', width=477.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.71)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=21.02):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=81.18, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La')
            with Note(default_x=179.11, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=244.39, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('cry')
            with Note(default_x=280.42, default_y=-419.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mo')
            with Note(default_x=378.35, default_y=-439.55):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.0, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='4', width=403.24):
            with Note(default_x=15.8, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di')
            with Note(default_x=112.26, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=176.57, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
            with Note(default_x=208.72, default_y=-419.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il')
            with Note(default_x=305.18, default_y=-439.55):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.7, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=441.8):
            with Note(default_x=21.54, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.77, default_y=-439.55):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=231.91, default_y=-424.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_y=-47.28, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=336.05, default_y=-429.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('get')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=497.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(119.92)
            with Note(default_x=81.18, default_y=-495.69):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=192.6, default_y=-500.69):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_y=-45.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=293.75, default_y=-520.69):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_y=-45.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vi')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=394.89, default_y=-525.69):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='7', width=409.78):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-14.54, relative_y=17.79):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=16.2, default_y=-510.69):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-15.81, relative_y=30.06):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=114.19, default_y=-480.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Note(default_x=212.19, default_y=-485.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-8.6, relative_y=30.24):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=310.18, default_y=-475.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus')
        with Measure(number='8', width=415.5):
            with Note(default_x=14.0, default_y=-480.69):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=1.95, relative_x=3.14, relative_y=32.4):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=113.98, default_y=-480.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo')
            with Note(default_x=213.95, default_y=-485.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=313.93, default_y=-485.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.64, default_y=-45.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='9', width=495.63):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(115.14)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-31.0, relative_y=20.56):
                        Pp()
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('S.v.', relative_x=-38.05, relative_y=37.69, font_family='Times New Roman')
            with Note(default_x=89.42, default_y=-494.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('La')
            with Note(default_x=190.57, default_y=-504.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('cry')
            with Note(default_x=291.72, default_y=-489.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mo')
            with Note(default_x=392.88, default_y=-504.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('sa')
        with Measure(number='10', width=415.29):
            with Note(default_x=17.23, default_y=-484.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('di')
            with Note(default_x=116.35, default_y=-504.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('es')
            with Note(default_x=215.46, default_y=-479.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('il')
            with Note(default_x=314.57, default_y=-504.11):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.7, default_y=-43.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('la,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='11', width=411.99):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=2.17, relative_x=-0.28, relative_y=27.38):
                        Mf()
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=34.55)
            with Note(default_x=16.2, default_y=-474.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('single')
                    Text('qua')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Note(default_x=114.75, default_y=-509.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=8.37, relative_y=21.99):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=213.3, default_y=-504.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('sur')
            with Note(default_x=311.84, default_y=-469.11):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('get')
        with Measure(number='12', width=453.31):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(115.94)
            with Note(default_x=86.18, default_y=-438.19):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('single')
                    Text('ex')
            with Note(default_x=175.76, default_y=-473.19):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('fa')
            with Note(default_x=265.33, default_y=-468.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('vil')
            with Note(default_x=354.91, default_y=-433.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('la')
        with Measure(number='13', width=460.67):
            with Note(default_x=16.2, default_y=-433.19):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ju')
            with Note(default_x=126.92, default_y=-468.19):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('di')
            with Note(default_x=237.64, default_y=-463.19):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('middle')
                    Text('can')
            with Note(default_x=348.36, default_y=-428.19):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('dus')
        with Measure(number='14', width=408.93):
            with Note(default_x=21.03, default_y=-428.19):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ho')
            with Note(default_x=117.61, default_y=-463.19):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('mo')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=43.31)
            with Note(default_x=214.18, default_y=-423.19):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.82, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=310.75, default_y=-458.19):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.64, default_y=-41.82, relative_y=-30.0):
                    Syllabic('end')
                    Text('us.')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-27.85)
        with Measure(number='15', width=487.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(101.52)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=1.06, relative_y=35.6):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=92.38, default_y=-399.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hu')
            with Note(default_x=190.26, default_y=-404.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ie')
            with Note(default_x=290.18, default_y=-409.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=388.06, default_y=-409.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('go')
        with Measure(number='16', width=425.41):
            with Note(default_x=36.87, default_y=-409.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('par')
            with Note(default_x=133.6, default_y=-404.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('ce')
            with Note(default_x=230.34, default_y=-399.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('De')
            with Note(default_x=327.07, default_y=-399.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.89, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('us,')
        with Measure(number='17', width=409.97):
            with Note(default_x=25.87, default_y=-399.81):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('pi')
            with Note(default_x=121.49, default_y=-404.81):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('e')
            with Note(default_x=217.12, default_y=-409.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=312.75, default_y=-414.81):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.14, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('su,')
        with Measure(number='18', width=501.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.68)
            with Note(default_x=77.5, default_y=-363.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Je')
            with Note(default_x=182.33, default_y=-353.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('su')
            with Note(default_x=289.99, default_y=-358.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-45.48, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=394.82, default_y=-358.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=464.7, default_y=-358.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.48, relative_y=-30.0):
                    Syllabic('middle')
                    Text('mi')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='19', width=375.62):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=0.26, relative_x=6.58, relative_y=10.59):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=15.6, default_y=-378.38):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.55, default_y=-45.48, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne!')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='20', width=446.05):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='21', width=478.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.07)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='22', width=421.28):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-2.9, relative_y=20.4):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-427.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Do')
            with Note(default_x=116.77, default_y=-427.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.08, default_y=-427.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('na')
            with Note(default_x=217.74, default_y=-422.38):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e')
            with Note(default_x=318.71, default_y=-442.38):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('is')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='23', width=422.97):
            with Note(default_x=15.8, default_y=-427.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-50.53, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re')
            with Note(default_x=117.19, default_y=-427.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.79, default_y=-427.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.53, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui')
            with Note(default_x=218.58, default_y=-422.38):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-50.53, relative_y=-30.0):
                    Syllabic('end')
                    Text('em')
                    Extend()
            with Note(default_x=319.98, default_y=-422.38):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='24', width=474.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(117.16)
            with Note(default_x=81.18, default_y=-466.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Note(default_x=178.05, default_y=-471.93):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
            with Note(default_x=274.91, default_y=-476.93):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=374.69, default_y=-481.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.73, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('is,', font_family='Times New Roman')
        with Measure(number='25', width=441.79):
            with Note(default_x=20.0, default_y=-486.93):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('do', font_family='Times New Roman')
            with Note(default_x=125.05, default_y=-506.93):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('na', font_family='Times New Roman')
            with Note(default_x=230.09, default_y=-506.93):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('e', font_family='Times New Roman')
            with Note(default_x=335.14, default_y=-501.93):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.28, relative_y=-30.0):
                    Syllabic('end')
                    Text('is', font_family='Times New Roman')
        with Measure(number='26', width=406.69):
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', relative_y=40.0, font_style='italic', font_family='Times New Roman')
            with Note(default_x=15.83, default_y=-521.93):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_y=-46.28, relative_y=-30.0):
                    Syllabic('begin')
                    Text('re', font_family='Times New Roman')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-1.57, relative_y=13.16):
                        Mf()
                Sound(dynamics=88.89)
            with Note(default_x=113.15, default_y=-521.93):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.21, relative_y=16.96):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=210.1, default_y=-516.93):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='27', width=470.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.63)
            with Note(default_x=92.86, default_y=-438.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=278.89, default_y=-438.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=2.68, relative_y=12.81):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=371.73, default_y=-438.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.32, relative_y=-30.0):
                    Syllabic('middle')
                    Text('qui', font_family='Times New Roman')
        with Measure(number='28', width=394.81):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=5.09, relative_x=2.08, relative_y=5.76):
                        Pp()
                Sound(dynamics=36.67)
            with Note(default_x=18.25, default_y=-423.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.13, default_y=-42.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('em.', font_family='Times New Roman')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('whole')
        with Measure(number='29', width=350.43):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=4.87, relative_y=19.78):
                        Ff()
                Sound(dynamics=140.0)
            with Note(default_x=15.32, default_y=-408.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Lyric(number='1', default_x=9.9, default_y=-42.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('A', font_family='Times New Roman')
        with Measure(number='30', width=107.26):
            with Note(default_x=20.55, default_y=-423.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=12.2, default_y=-42.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('men.', font_family='Times New Roman')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=656.18):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(680.77)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('12')
                    BeatType('8')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=-24.84, relative_y=-36.85):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=155.27, default_y=-1050.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=200.66, default_y=-1045.77):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=291.44, default_y=-1025.77):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=336.84, default_y=-1020.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=427.62, default_y=-1045.77):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=473.01, default_y=-1050.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=563.79, default_y=-1015.77):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=609.19, default_y=-1020.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=109.88, default_y=-1080.77):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.88, default_y=-1070.77):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=246.05, default_y=-1070.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=246.05, default_y=-1060.77):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=382.23, default_y=-1075.77):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=382.23, default_y=-1065.77):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=518.4, default_y=-1065.77):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=518.4, default_y=-1050.77):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=536.42):
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.68, default_y=-1025.77):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=99.24, default_y=-1010.77):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Full of tears shall be that day,\n', relative_x=4.05, relative_y=660.99, font_family='Times New Roman')
                    Words('When from the ashes shall arise,\n')
                    Words('All humanity to be judged.\n')
                    Words('Spare us by your mercy, Lord,\n')
                    Words('Gentle Lord Jesus,\n')
                    Words('Grant them eternal rest. Amen.')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=186.35, default_y=-1020.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=229.91, default_y=-1030.77):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=317.03, default_y=-1040.77):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=360.58, default_y=-1035.77):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=447.7, default_y=-1025.77):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=491.26, default_y=-1050.77):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.12, default_y=-1070.77):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=12.12, default_y=-1045.77):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(2)
            with Note(default_x=142.79, default_y=-1145.77):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=142.79, default_y=-1120.77):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(2)
            with Note(default_x=273.47, default_y=-1140.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=273.47, default_y=-1125.77):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.01)
                Staff(2)
            with Note(default_x=404.14, default_y=-1140.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=404.14, default_y=-1110.77):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='3', width=477.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(111.65)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=113.82, default_y=-571.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.46, default_y=-566.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=211.75, default_y=-546.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=244.39, default_y=-541.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=313.06, default_y=-566.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=345.7, default_y=-571.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=410.99, default_y=-541.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=443.63, default_y=-546.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=81.18, default_y=-591.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=179.11, default_y=-581.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=280.42, default_y=-586.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=378.35, default_y=-586.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=378.35, default_y=-571.2):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=81.18, default_y=-716.2):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.18, default_y=-681.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=179.11, default_y=-706.2):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=179.11, default_y=-671.2):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=280.42, default_y=-711.2):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=280.42, default_y=-676.2):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=378.35, default_y=-731.2):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=378.35, default_y=-696.2):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='4', width=403.24):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=47.95, default_y=-571.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.11, default_y=-566.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=144.41, default_y=-546.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.57, default_y=-541.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=240.88, default_y=-566.2):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=273.03, default_y=-571.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=337.34, default_y=-541.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=369.49, default_y=-546.2):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-591.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-566.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=112.26, default_y=-581.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=208.72, default_y=-586.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=305.18, default_y=-586.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=305.18, default_y=-571.2):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-716.2):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-681.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=112.26, default_y=-706.2):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=112.26, default_y=-671.2):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=208.72, default_y=-711.2):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=208.72, default_y=-676.2):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=305.18, default_y=-731.2):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=305.18, default_y=-696.2):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='5', width=441.8):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=56.25, default_y=-601.2):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.97, default_y=-616.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=162.49, default_y=-596.2):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=197.2, default_y=-616.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=266.63, default_y=-591.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=301.34, default_y=-616.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=370.77, default_y=-586.2):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=405.48, default_y=-606.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.54, default_y=-626.2):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=127.77, default_y=-616.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=127.77, default_y=-606.2):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=231.91, default_y=-616.2):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=231.91, default_y=-601.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=336.05, default_y=-606.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=336.05, default_y=-596.2):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.54, default_y=-716.2):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=21.54, default_y=-681.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=127.77, default_y=-731.2):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.77, default_y=-696.2):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=231.91, default_y=-716.2):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=231.91, default_y=-681.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=336.05, default_y=-721.2):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=336.05, default_y=-686.2):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='6', width=497.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.73)
                with StaffLayout(number=2):
                    StaffDistance(87.85)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=114.89, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=148.61, default_y=-649.42):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=226.32, default_y=-634.42):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=260.03, default_y=-654.42):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=327.46, default_y=-629.42):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=361.18, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=428.61, default_y=-624.42):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=462.32, default_y=-644.42):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=81.18, default_y=-664.42):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=81.18, default_y=-649.42):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=192.6, default_y=-679.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=192.6, default_y=-669.42):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=293.75, default_y=-674.42):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=293.75, default_y=-654.42):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=394.89, default_y=-669.42):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=394.89, default_y=-644.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=81.18, default_y=-787.28):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.18, default_y=-752.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=192.6, default_y=-792.28):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=192.6, default_y=-757.28):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=293.75, default_y=-812.28):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=293.75, default_y=-777.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=394.89, default_y=-817.28):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=394.89, default_y=-782.28):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='7', width=409.78):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=48.86, default_y=-619.42):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=81.53, default_y=-629.42):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=146.86, default_y=-619.42):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.52, default_y=-629.42):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=12.72, relative_x=2.79, relative_y=15.94):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=244.85, default_y=-614.42):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=277.52, default_y=-629.42):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=342.85, default_y=-614.42):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=375.51, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-664.42):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=16.2, default_y=-644.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=114.19, default_y=-644.42):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=114.19, default_y=-629.42):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=212.19, default_y=-649.42):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=-629.42):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=310.18, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=310.18, default_y=-619.42):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', relative_x=-7.43, relative_y=38.53, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=16.2, default_y=-802.28):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=16.2, default_y=-767.28):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-3.43, relative_y=27.66):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=114.19, default_y=-772.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=114.19, default_y=-737.28):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=212.19, default_y=-777.28):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=212.19, default_y=-742.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=2.03, relative_x=1.28, relative_y=24.34):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Note(default_x=310.18, default_y=-767.28):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=310.18, default_y=-732.28):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='8', width=415.5):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=15.25, relative_x=-2.91, relative_y=13.91):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=47.33, default_y=-609.42):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.65, default_y=-644.42):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=147.3, default_y=-609.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.63, default_y=-644.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=21.06, relative_x=7.94, relative_y=18.1):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=247.28, default_y=-604.42):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=280.6, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=347.25, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=380.58, default_y=-674.42):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=-644.42):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=14.0, default_y=-624.42):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=113.98, default_y=-624.42):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=113.98, default_y=-614.42):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=213.95, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=213.95, default_y=-624.42):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=213.95, default_y=-614.42):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=313.93, default_y=-639.42):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=313.93, default_y=-629.42):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=313.93, default_y=-619.42):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=14.0, default_y=-772.28):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=14.0, default_y=-737.28):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=5.26, relative_y=25.69):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=113.98, default_y=-772.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=113.98, default_y=-737.28):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=213.95, default_y=-777.28):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=213.95, default_y=-742.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=313.93, default_y=-812.28):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=313.93, default_y=-777.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='9', width=495.63):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.19)
                with StaffLayout(number=2):
                    StaffDistance(105.71)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=123.14, default_y=-630.3):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.85, default_y=-650.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=224.29, default_y=-610.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=258.01, default_y=-615.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=325.44, default_y=-635.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=359.16, default_y=-650.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=426.6, default_y=-590.3):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=460.31, default_y=-600.3):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=426.6, default_y=-615.3):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-28.67, relative_y=28.53):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=89.42, default_y=-761.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=89.42, default_y=-751.01):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=89.42, default_y=-741.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=190.57, default_y=-771.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=190.57, default_y=-761.01):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=190.57, default_y=-741.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=291.72, default_y=-756.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=291.72, default_y=-746.01):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=392.88, default_y=-771.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=392.88, default_y=-756.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=392.88, default_y=-746.01):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='10', width=415.29):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=50.27, default_y=-620.3):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=83.31, default_y=-645.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=149.38, default_y=-600.3):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=182.42, default_y=-595.3):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=248.5, default_y=-635.3):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.5, default_y=-615.3):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=281.54, default_y=-650.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=347.61, default_y=-605.3):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=380.65, default_y=-600.3):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=149.38, default_y=-620.3):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=347.61, default_y=-625.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=347.61, default_y=-615.3):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-751.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=17.23, default_y=-741.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=17.23, default_y=-731.01):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=116.35, default_y=-771.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=116.35, default_y=-761.01):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=116.35, default_y=-736.01):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=215.46, default_y=-746.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=215.46, default_y=-736.01):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=314.57, default_y=-771.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=314.57, default_y=-756.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=314.57, default_y=-746.01):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=5.06, relative_x=-17.64, relative_y=25.71):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='11', width=411.99):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-58.53, relative_x=-2.22, relative_y=-32.22):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=49.05, default_y=-595.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=81.9, default_y=-630.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=147.6, default_y=-585.3):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.45, default_y=-595.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=246.15, default_y=-595.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=279.0, default_y=-625.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=344.69, default_y=-600.3):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=377.54, default_y=-610.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-630.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=16.2, default_y=-610.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=114.75, default_y=-630.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=114.75, default_y=-610.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=213.3, default_y=-625.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=213.3, default_y=-610.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=311.84, default_y=-625.3):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=311.84, default_y=-610.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=37.4)
                Staff(2)
            with Note(default_x=16.2, default_y=-776.01):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=16.2, default_y=-741.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=13.0)
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=11.36, relative_y=21.76):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=114.75, default_y=-811.01):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.75, default_y=-776.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=213.3, default_y=-806.01):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=213.3, default_y=-771.01):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=311.84, default_y=-771.01):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=311.84, default_y=-736.01):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='12', width=453.31):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.49)
                with StaffLayout(number=2):
                    StaffDistance(69.42)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=116.04, default_y=-577.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=145.9, default_y=-612.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=205.61, default_y=-567.68):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=235.47, default_y=-572.68):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=295.19, default_y=-572.68):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=325.05, default_y=-602.68):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=384.77, default_y=-577.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=418.94, default_y=-557.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=86.18, default_y=-602.68):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=86.18, default_y=-592.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=175.76, default_y=-592.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=235.47, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=265.33, default_y=-602.68):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=354.91, default_y=-587.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=418.94, default_y=-592.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=86.18, default_y=-712.1):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=86.18, default_y=-677.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=175.76, default_y=-747.1):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=175.76, default_y=-712.1):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=265.33, default_y=-742.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=265.33, default_y=-707.1):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=354.91, default_y=-707.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=354.91, default_y=-672.1):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='13', width=460.67):
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=53.11, default_y=-557.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.01, default_y=-592.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=163.82, default_y=-562.68):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=200.73, default_y=-567.68):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=274.54, default_y=-567.68):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=311.45, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=385.26, default_y=-572.68):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=422.17, default_y=-552.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-592.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=16.2, default_y=-567.68):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=126.92, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=126.92, default_y=-577.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=237.64, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=237.64, default_y=-582.68):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=348.36, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=348.36, default_y=-582.68):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=16.2, default_y=-707.1):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=16.2, default_y=-672.1):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=126.92, default_y=-742.1):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=126.92, default_y=-707.1):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=237.64, default_y=-737.1):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=237.64, default_y=-702.1):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=348.36, default_y=-702.1):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=348.36, default_y=-667.1):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='14', width=408.93):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=53.22, default_y=-552.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.41, default_y=-587.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=149.8, default_y=-557.68):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=181.99, default_y=-562.68):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-76.75)
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=246.37, default_y=-562.68):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=278.56, default_y=-592.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=342.94, default_y=-567.68):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=375.14, default_y=-542.68):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-37.13)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.03, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.03, default_y=-572.68):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=117.61, default_y=-592.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=117.61, default_y=-572.68):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=181.99, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=214.18, default_y=-597.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=214.18, default_y=-572.68):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=310.75, default_y=-602.68):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=310.75, default_y=-577.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.03, default_y=-702.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=21.03, default_y=-667.1):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=117.61, default_y=-737.1):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=117.61, default_y=-702.1):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=214.18, default_y=-732.1):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=214.18, default_y=-697.1):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=310.75, default_y=-697.1):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=310.75, default_y=-662.1):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='15', width=487.53):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=1.78, relative_y=-24.88):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=125.01, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.64, default_y=-539.81):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=222.89, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=255.51, default_y=-534.81):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=322.8, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=355.43, default_y=-529.81):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=420.68, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=453.31, default_y=-529.81):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=92.38, default_y=-644.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=92.38, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=92.38, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=92.38, default_y=-609.81):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=190.26, default_y=-649.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=190.26, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=190.26, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=190.26, default_y=-614.81):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=290.18, default_y=-654.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=290.18, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=278.31, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=290.18, default_y=-619.81):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=388.06, default_y=-654.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=388.06, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=376.19, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=388.06, default_y=-619.81):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='16', width=425.41):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=69.11, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=101.36, default_y=-529.81):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=165.85, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=198.09, default_y=-534.81):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=262.58, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=294.83, default_y=-539.81):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=359.32, default_y=-554.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=391.56, default_y=-539.81):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=36.87, default_y=-654.81):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=36.87, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=25.0, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=36.87, default_y=-619.81):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=133.6, default_y=-649.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=133.6, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=133.6, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=133.6, default_y=-614.81):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=230.34, default_y=-644.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=230.34, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=230.34, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=230.34, default_y=-609.81):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=327.07, default_y=-644.81):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=327.07, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=327.07, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=327.07, default_y=-609.81):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='17', width=409.97):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=57.74, default_y=-549.81):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.62, default_y=-539.81):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=153.37, default_y=-549.81):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=185.24, default_y=-534.81):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=248.99, default_y=-559.81):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=280.87, default_y=-529.81):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=344.62, default_y=-534.81):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=376.5, default_y=-519.81):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=25.87, default_y=-644.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=14.0, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=25.87, default_y=-629.81):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=25.87, default_y=-609.81):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=121.49, default_y=-649.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.49, default_y=-639.81):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.49, default_y=-629.81):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.49, default_y=-614.81):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=217.12, default_y=-654.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=217.12, default_y=-639.81):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=217.12, default_y=-629.81):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=217.12, default_y=-619.81):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=312.75, default_y=-659.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=312.75, default_y=-649.81):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=312.75, default_y=-634.81):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=312.75, default_y=-624.81):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='18', width=501.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.9)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=112.44, default_y=-454.28):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=147.38, default_y=-444.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=217.27, default_y=-419.28):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=252.21, default_y=-429.28):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=324.93, default_y=-424.28):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=359.87, default_y=-434.28):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=429.76, default_y=-429.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=464.7, default_y=-439.28):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Forward():
                Duration(8.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(10.0)
            with Note(default_x=77.5, default_y=-579.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.5, default_y=-569.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.5, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.5, default_y=-544.28):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=182.33, default_y=-569.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=182.33, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=182.33, default_y=-549.28):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=289.99, default_y=-574.28):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=289.99, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=289.99, default_y=-549.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=394.82, default_y=-574.28):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=394.82, default_y=-564.28):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=394.82, default_y=-544.28):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='19', width=375.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.47, relative_x=6.27, relative_y=-15.84):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=45.47, default_y=-479.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=75.33, default_y=-444.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=135.07, default_y=-479.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=164.94, default_y=-444.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=224.68, default_y=-479.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=254.54, default_y=-444.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=284.41, default_y=-469.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=314.28, default_y=-459.28):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=344.15, default_y=-444.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-75.88)
                Staff(2)
            with Note(default_x=15.6, default_y=-559.28):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.6, default_y=-549.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-73.65)
                Staff(2)
            with Note(default_x=105.2, default_y=-584.28):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=105.2, default_y=-574.28):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=105.2, default_y=-564.28):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=117.07, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-8.07)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-82.76)
                Staff(2)
            with Note(default_x=194.81, default_y=-579.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=194.81, default_y=-569.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=194.81, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-79.01)
                Staff(2)
            with Note(default_x=284.41, default_y=-574.28):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=272.55, default_y=-564.28):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=284.41, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-20.75)
                Staff(2)
        with Measure(number='20', width=446.05):
            with Note(default_x=12.12, default_y=-444.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=120.2, default_y=-444.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=156.23, default_y=-454.28):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=192.26, default_y=-464.28):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=264.31, default_y=-424.28):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=300.34, default_y=-434.28):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=372.39, default_y=-429.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=408.42, default_y=-439.28):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=48.15, default_y=-479.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=84.17, default_y=-464.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(3.0)
                Voice('2')
                Type('quarter')
                Dot()
                Staff(1)
            with Note(default_x=228.28, default_y=-459.28):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=336.37, default_y=-459.28):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=372.39, default_y=-464.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=408.42, default_y=-474.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-82.76)
                Staff(2)
            with Note(default_x=12.12, default_y=-579.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.12, default_y=-569.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.12, default_y=-544.28):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-75.26)
                Staff(2)
            with Note(default_x=120.2, default_y=-569.28):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.2, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.2, default_y=-549.28):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.22)
                Staff(2)
            with Note(default_x=228.28, default_y=-574.28):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=228.28, default_y=-559.28):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=228.28, default_y=-549.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-79.01)
                Staff(2)
            with Note(default_x=336.37, default_y=-574.28):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=336.37, default_y=-554.28):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=324.5, default_y=-544.28):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=336.37, default_y=-539.28):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='21', width=478.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(114.9)
                with StaffLayout(number=2):
                    StaffDistance(73.65)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=110.62, default_y=-567.28):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.75, default_y=-562.28):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-82.0)
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=212.07, default_y=-542.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=245.19, default_y=-537.28):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=311.44, default_y=-572.28):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=344.57, default_y=-577.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=410.82, default_y=-552.28):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=443.94, default_y=-577.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-34.59)
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=77.5, default_y=-597.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=176.87, default_y=-587.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=176.87, default_y=-572.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=278.32, default_y=-582.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=278.32, default_y=-572.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=377.69, default_y=-602.28):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=377.69, default_y=-587.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-67.76)
                Staff(2)
            with Note(default_x=77.5, default_y=-685.93):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.5, default_y=-675.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-73.96)
                Staff(2)
            with Note(default_x=176.87, default_y=-720.93):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=176.87, default_y=-685.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-78.96)
                Staff(2)
            with Note(default_x=278.32, default_y=-725.93):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=278.32, default_y=-690.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.96)
                Staff(2)
            with Note(default_x=377.69, default_y=-745.93):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=377.69, default_y=-710.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-17.29)
                Staff(2)
        with Measure(number='22', width=421.28):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-58.17, relative_x=5.76, relative_y=-28.83):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=49.46, default_y=-577.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=83.11, default_y=-572.28):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=150.43, default_y=-552.28):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=184.08, default_y=-547.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=251.39, default_y=-572.28):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=285.05, default_y=-577.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=352.36, default_y=-547.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=386.02, default_y=-552.28):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-597.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=116.77, default_y=-587.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=217.74, default_y=-592.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=318.71, default_y=-592.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=318.71, default_y=-577.28):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-730.93):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-695.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=116.77, default_y=-720.93):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=116.77, default_y=-685.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=217.74, default_y=-725.93):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=217.74, default_y=-690.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=318.71, default_y=-745.93):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=318.71, default_y=-710.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='23', width=422.97):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=49.6, default_y=-577.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=83.39, default_y=-572.28):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=150.99, default_y=-552.28):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=184.79, default_y=-547.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=252.38, default_y=-572.28):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=286.18, default_y=-577.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=353.77, default_y=-547.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=387.57, default_y=-552.28):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-597.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-572.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=117.19, default_y=-587.28):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=218.58, default_y=-592.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=319.98, default_y=-592.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=319.98, default_y=-577.28):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-730.93):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-695.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=117.19, default_y=-720.93):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=117.19, default_y=-685.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=218.58, default_y=-725.93):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=218.58, default_y=-690.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=319.98, default_y=-745.93):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=319.98, default_y=-710.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='24', width=474.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(102.96)
                with StaffLayout(number=2):
                    StaffDistance(82.24)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-43.86, relative_x=-5.14, relative_y=-35.2):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=113.47, default_y=-639.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=145.76, default_y=-634.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=210.34, default_y=-609.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=242.62, default_y=-614.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-48.35, relative_x=6.18, relative_y=-27.4):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=307.2, default_y=-639.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=339.49, default_y=-634.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=406.98, default_y=-599.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=440.54, default_y=-604.89):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=81.18, default_y=-659.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=81.18, default_y=-634.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=178.05, default_y=-634.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=274.91, default_y=-644.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=374.69, default_y=-634.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=374.69, default_y=-624.89):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=374.69, default_y=-614.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=81.18, default_y=-802.13):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.18, default_y=-767.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=178.05, default_y=-792.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=178.05, default_y=-757.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=274.91, default_y=-787.13):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=274.91, default_y=-752.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=374.69, default_y=-802.13):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=374.69, default_y=-767.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='25', width=441.79):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-48.1, relative_x=-13.52, relative_y=-35.15):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=55.02, default_y=-634.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.03, default_y=-629.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=160.06, default_y=-609.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.08, default_y=-614.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=265.11, default_y=-624.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=300.12, default_y=-629.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=370.16, default_y=-614.89):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=405.17, default_y=-599.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=20.0, default_y=-654.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=20.0, default_y=-644.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=113.18, default_y=-654.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=125.05, default_y=-649.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=125.05, default_y=-629.89):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=230.09, default_y=-654.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=230.09, default_y=-644.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=230.09, default_y=-629.89):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=335.14, default_y=-659.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=335.14, default_y=-649.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=335.14, default_y=-634.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=20.0, default_y=-797.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=20.0, default_y=-762.13):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=125.05, default_y=-807.13):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=125.05, default_y=-772.13):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=230.09, default_y=-807.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=230.09, default_y=-772.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=335.14, default_y=-802.13):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=335.14, default_y=-767.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='26', width=406.69):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=48.27, default_y=-629.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.71, default_y=-634.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=145.59, default_y=-599.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=178.02, default_y=-624.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=5.47, relative_x=-10.13, relative_y=22.1):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=242.9, default_y=-639.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=275.34, default_y=-629.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=32.26, relative_x=-4.52, relative_y=21.02):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=340.22, default_y=-624.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=372.65, default_y=-599.89):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.83, default_y=-654.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.83, default_y=-644.89):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=113.15, default_y=-644.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=113.15, default_y=-634.89):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=210.46, default_y=-649.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=210.46, default_y=-639.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=307.78, default_y=-634.89):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=307.78, default_y=-624.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', relative_x=-2.31, relative_y=43.46, font_style='italic', font_family='Times New Roman')
                Staff(2)
            with Note(default_x=15.83, default_y=-822.13):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.83, default_y=-787.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-0.7, relative_y=32.9):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Note(default_x=113.15, default_y=-822.13):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=113.15, default_y=-787.13):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-0.6, relative_y=26.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=210.46, default_y=-817.13):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=210.46, default_y=-782.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=307.78, default_y=-817.13):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=307.78, default_y=-782.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='27', width=470.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(96.7)
                with StaffLayout(number=2):
                    StaffDistance(70.79)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=124.16, default_y=-544.73):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.11, default_y=-529.73):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=10.1, relative_x=-6.2, relative_y=30.78):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=217.0, default_y=-514.73):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=247.95, default_y=-549.73):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=309.84, default_y=-544.73):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=340.79, default_y=-529.73):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=10.99, relative_y=-29.79):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=406.93, default_y=-519.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=437.87, default_y=-529.73):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=93.22, default_y=-554.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=93.22, default_y=-544.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=186.06, default_y=-549.73):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=186.06, default_y=-539.73):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=278.89, default_y=-564.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=267.03, default_y=-549.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=278.89, default_y=-544.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=371.73, default_y=-564.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=371.73, default_y=-554.73):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=371.73, default_y=-544.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=93.22, default_y=-720.52):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.22, default_y=-685.52):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=186.06, default_y=-720.52):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=186.06, default_y=-685.52):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=278.89, default_y=-720.52):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=278.89, default_y=-685.52):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=371.73, default_y=-720.52):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=371.73, default_y=-685.52):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='28', width=394.81):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=49.25, default_y=-554.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.25, default_y=-549.73):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=142.25, default_y=-549.73):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=142.25, default_y=-534.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=173.64, default_y=-574.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=173.64, default_y=-539.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=235.64, default_y=-539.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=235.64, default_y=-524.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=266.64, default_y=-564.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=266.64, default_y=-529.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=328.64, default_y=-539.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=328.64, default_y=-514.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=362.21, default_y=-554.73):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=362.21, default_y=-519.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(default_x=142.25, default_y=-564.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=235.64, default_y=-554.73):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=328.64, default_y=-549.73):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.96)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=43.54)
                Staff(2)
            with Note(default_x=18.25, default_y=-705.52):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=18.25, default_y=-670.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.96)
                Staff(2)
            with Note(default_x=111.25, default_y=-705.52):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=111.25, default_y=-670.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-6.92)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.96)
                Staff(2)
            with Note(default_x=204.64, default_y=-705.52):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=204.64, default_y=-670.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-6.92)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.96)
                Staff(2)
            with Note(default_x=297.64, default_y=-705.52):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=297.64, default_y=-670.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-38.05)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-20.75)
                Staff(2)
        with Measure(number='29', width=350.43):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-43.39, relative_x=3.05, relative_y=-30.85):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=46.16, default_y=-524.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=73.67, default_y=-569.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=73.67, default_y=-534.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=128.7, default_y=-534.73):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.22, default_y=-584.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=156.22, default_y=-549.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=211.25, default_y=-549.73):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=238.76, default_y=-594.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=238.76, default_y=-559.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=293.8, default_y=-559.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=321.31, default_y=-604.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=321.31, default_y=-569.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=46.16, default_y=-559.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=46.16, default_y=-549.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=128.7, default_y=-569.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=128.7, default_y=-559.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=211.25, default_y=-584.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=211.25, default_y=-569.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=293.8, default_y=-594.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=293.8, default_y=-584.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-74.95)
                Staff(2)
            with Note(default_x=18.64, default_y=-690.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=18.64, default_y=-655.52):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.24)
                Staff(2)
            with Note(default_x=101.19, default_y=-705.52):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=101.19, default_y=-670.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-14.99)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.93)
                Staff(2)
            with Note(default_x=183.73, default_y=-715.52):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=183.73, default_y=-680.52):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-107.91)
                Staff(2)
            with Note(default_x=266.28, default_y=-725.52):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=266.28, default_y=-690.52):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-21.9)
                Staff(2)
        with Measure(number='30', width=107.26):
            with Note(default_x=20.55, default_y=-574.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('sharp')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=8.92, relative_y=10.0)
            with Note(default_x=20.55, default_y=-564.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
            with Note(default_x=20.55, default_y=-549.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
            with Note(default_x=20.55, default_y=-539.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('sharp')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=20.55, default_y=-740.52):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=14.6, relative_y=10.0)
                    Fermata(None, type='inverted', default_y=-89.42, relative_y=-10.0)
            with Note(default_x=20.55, default_y=-705.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
            with Note(default_x=20.55, default_y=-670.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
            with Note(default_x=20.55, default_y=-660.52):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('whole')
                Dot()
                Accidental('sharp')
                Staff(2)
            with Note(default_x=20.55, default_y=-650.52):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
            with Note(default_x=20.55, default_y=-635.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')