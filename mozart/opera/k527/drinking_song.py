with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Drinking Song (Don Giovanni, K 527)')
    with Identification():
        Creator('W.A.Mozart (1756-1791)', type='composer')
        Creator('Arr.: M. Sánchez', type='lyricist')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(3.856)
            Tenths(40.0)
        with PageLayout():
            PageHeight(3080.2)
            PageWidth(2179.05)
            with PageMargins(type='even'):
                LeftMargin(103.734)
                RightMargin(103.734)
                TopMargin(103.734)
                BottomMargin(207.469)
            with PageMargins(type='odd'):
                LeftMargin(103.734)
                RightMargin(103.734)
                TopMargin(103.734)
                BottomMargin(207.469)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Drinking Song (Don Giovanni, K 527)', default_x=1089.52, default_y=2976.46, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Orquesta Melitón', default_x=1089.52, default_y=2872.73, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('W.A.Mozart (1756-1791)', default_x=2075.31, default_y=2674.89, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Arr.: M. Sánchez', default_x=103.734, default_y=2674.89, justify='left', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Flauta')
            PartAbbreviation('Fl.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Flauta')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Clarinete en Si♭')
            PartAbbreviation('Cl. Si♭')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Clarinete en Si♭')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(72)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Guitarra clásica')
            PartAbbreviation('Guit.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Guitarra clásica')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(25)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Violín')
            PartAbbreviation('Vln.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Violín')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(5)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Violín')
            PartAbbreviation('Vln.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Violín')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(8)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Viola')
            PartAbbreviation('Vla.')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Viola')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(12)
                MidiProgram(42)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Violonchelo')
            PartAbbreviation('Vc.')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Violonchelo')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(15)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Violonchelo')
            PartAbbreviation('Vc.')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Violonchelo')
            MidiDevice(None, id='P8-I1', port=2)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(2)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P9'):
            PartName('Contrabajo')
            PartAbbreviation('Cb.')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('Contrabajo')
            MidiDevice(None, id='P9-I1', port=2)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(5)
                MidiProgram(44)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=219.98):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(159.31)
                        RightMargin(0.0)
                    TopSystemDistance(371.58)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=97.13):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='4', width=97.56):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.88, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=110.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=55.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=97.13):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='12', width=97.13):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='13', width=100.57):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=55.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=106.0):
            with Note(default_x=14.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.75)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=112.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=171.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=230.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=249.39):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='20', width=249.82):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.91, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.12, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=275.63):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=144.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=209.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(4)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(-1)
                    Chromatic(-2.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.21, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=174.66, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.21, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.56, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.03, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=97.13):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='4', width=97.56):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.84, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.88, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.93, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=110.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=35.34, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.97, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.59, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=55.26, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.36, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=97.13):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='12', width=97.13):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='13', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=13.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=55.26, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.36, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=106.0):
            with Note(default_x=14.16, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.52, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.87, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=81.23, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.36, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=112.15, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=171.63, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=230.76, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=249.39):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='20', width=249.82):
            with Note():
                Rest(measure='yes')
                Duration(4.0)
                Voice('1')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.26, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.52, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.91, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.01, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.12, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=275.63):
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=144.1, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=209.06, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P3'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.57, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=154.11, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.66, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.21, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=52.03, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=97.56):
            with Note(default_x=10.72, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.41, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.75, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.72, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.27, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.84, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.88, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.93, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=110.81):
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=59.97, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.59, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Note(default_x=13.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=55.26, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.8, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=97.13):
            with Note(default_x=10.36, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=97.13):
            with Note(default_x=10.36, default_y=-205.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=100.57):
            with Note(default_x=13.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=55.26, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.8, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=106.0):
            with Note(default_x=13.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=58.51, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.72, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.27, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=111.79, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=230.76, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=249.39):
            with Note(default_x=10.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.26, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.52, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=249.82):
            with Note(default_x=10.72, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.1, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.11, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.72, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.99, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.26, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.52, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.91, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.01, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=212.12, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=275.63):
            with Note(default_x=14.16, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.13, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=144.1, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=209.06, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P4'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.21, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.66, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.21, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.72, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.56, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.03, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='3', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.27, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=97.56):
            with Note(default_x=10.72, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.41, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.11, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.8, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=-300.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.84, default_y=-305.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.88, default_y=-305.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.93, default_y=-305.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=110.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.34, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.97, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.59, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Note(default_x=13.8, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=55.26, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.36, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=97.13):
            with Note(default_x=10.72, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.27, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=55.26, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.36, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.36, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=106.0):
            with Note(default_x=14.16, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.52, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.87, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.23, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.36, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=112.15, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=171.63, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=230.76, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='19', width=249.39):
            with Note(default_x=10.72, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.99, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.26, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.52, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=249.82):
            with Note(default_x=10.72, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.1, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.47, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.85, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.26, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.52, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=-300.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.91, default_y=-305.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.01, default_y=-305.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.12, default_y=-305.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=275.63):
            with Note(default_x=13.8, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=144.1, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=209.06, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P5'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.57, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=154.11, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.66, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=195.21, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.36, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=52.03, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.36, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=97.56):
            with Note(default_x=10.72, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.41, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.75, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.72, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.27, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.84, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.88, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.93, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=110.81):
            with Note(default_x=10.36, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=59.97, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.59, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Note(default_x=13.8, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=55.26, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.8, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.36, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.27, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=97.13):
            with Note(default_x=10.72, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=31.27, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=100.57):
            with Note(default_x=13.8, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=55.26, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.8, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.36, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.36, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='16', width=106.0):
            with Note(default_x=13.8, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=58.51, default_y=-485.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.36, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=112.15, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=171.63, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=230.76, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=249.39):
            with Note(default_x=10.72, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=69.99, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.26, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.52, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=249.82):
            with Note(default_x=10.72, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.1, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.47, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.85, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=128.9, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.91, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=146.01, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=212.12, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=275.63):
            with Note(default_x=14.16, default_y=-485.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.13, default_y=-485.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=144.1, default_y=-485.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=209.06, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-445.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P6'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.57, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=154.11, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.66, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.21, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.72, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.56, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.39, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.23, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.36, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=97.56):
            with Note(default_x=10.72, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.41, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.75, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.84, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.88, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.93, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=110.81):
            with Note(default_x=10.36, default_y=-520.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=59.97, default_y=-515.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.59, default_y=-510.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-505.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Note(default_x=14.16, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.71, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.26, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.72, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-525.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-525.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=97.13):
            with Note(default_x=10.36, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=97.13):
            with Note(default_x=10.36, default_y=-525.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=14.16, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.71, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.26, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.72, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-525.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-525.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.72, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=106.0):
            with Note(default_x=14.16, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.52, default_y=-525.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.51, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.72, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=112.15, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=171.63, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=231.12, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=290.6, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=249.39):
            with Note(default_x=10.36, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.26, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.52, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=249.82):
            with Note(default_x=10.72, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.1, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.11, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=128.9, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=-555.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.91, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.01, default_y=-540.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.12, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=275.63):
            with Note(default_x=14.16, default_y=-535.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.13, default_y=-525.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=144.1, default_y=-515.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=209.06, default_y=-520.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-530.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P7'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.57, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=154.11, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.66, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=195.21, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.72, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.56, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.39, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.23, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.36, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.82, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.37, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=97.56):
            with Note(default_x=10.72, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.41, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.75, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.84, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.88, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.93, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=110.81):
            with Note(default_x=10.36, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=59.97, default_y=-625.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.59, default_y=-620.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-615.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Note(default_x=14.16, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.71, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.26, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.72, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=97.13):
            with Note(default_x=10.36, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.82, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=97.13):
            with Note(default_x=10.36, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=14.16, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.71, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.26, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.8, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.72, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.72, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=106.0):
            with Note(default_x=14.16, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.52, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.51, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.72, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=112.15, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=171.63, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=231.12, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=290.6, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=249.39):
            with Note(default_x=10.36, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.26, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=188.52, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=249.82):
            with Note(default_x=10.72, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.1, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.11, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=128.9, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=-665.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.91, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.01, default_y=-650.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.12, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=275.63):
            with Note(default_x=14.16, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.13, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=144.1, default_y=-625.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=209.06, default_y=-630.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-640.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P8'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(71.31)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.21, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.3, default_y=-776.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.36, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=52.03, default_y=-776.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=97.56):
            with Note(default_x=10.72, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.41, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.11, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.8, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.72, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.8, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.84, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.88, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=97.93, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=110.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-746.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.34, default_y=-756.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.97, default_y=-756.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.59, default_y=-741.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-741.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=-726.31):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=54.9, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.36, default_y=-741.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-741.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.72, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-751.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=97.13):
            with Note(default_x=10.72, default_y=-756.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.27, default_y=-746.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-746.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.37, default_y=-756.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=100.57):
            with Note(default_x=13.8, default_y=-726.31):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=54.9, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.36, default_y=-741.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-741.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.36, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-726.31):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='16', width=106.0):
            with Note(default_x=13.8, default_y=-731.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=58.51, default_y=-741.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.36, default_y=-761.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-776.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=111.79, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=230.76, default_y=-770.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=249.39):
            with Note(default_x=10.72, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.99, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.26, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.52, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=249.82):
            with Note(default_x=10.72, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=70.1, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.47, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.85, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.72, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.99, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.26, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=188.52, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.8, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=79.91, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.01, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=212.12, default_y=-720.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=275.63):
            with Note(default_x=13.8, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=144.1, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=209.06, default_y=-735.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-720.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P9'):
        with Measure(number='1', width=219.98):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(1.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=133.21, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=174.3, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='2', width=98.0):
            with Note(default_x=10.36, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=52.03, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='3', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.36, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='4', width=97.56):
            with Note(default_x=10.36, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.75, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='6', width=127.57):
            with Note(default_x=13.44, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=69.52, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=110.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.36, default_y=-846.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=59.97, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.59, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=74.17):
            with Note(default_x=13.8, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=100.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=54.9, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='10', width=97.13):
            with Note(default_x=10.36, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=97.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=10.36, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='12', width=97.13):
            with Note(default_x=10.36, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='13', width=100.57):
            with Note(default_x=13.8, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=54.9, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='14', width=97.13):
            with Note(default_x=10.36, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.46, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=97.13):
            with Note(default_x=10.36, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='16', width=106.0):
            with Note(default_x=13.8, default_y=-846.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=58.51, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='17', width=97.13):
            with Note(default_x=10.36, default_y=-866.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=51.46, default_y=-881.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='18', width=351.69):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=111.79, default_y=-860.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=230.76, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='19', width=249.39):
            with Note(default_x=10.36, default_y=-860.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=128.9, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='20', width=249.82):
            with Note(default_x=10.36, default_y=-860.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.11, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='21', width=249.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=10.36, default_y=-860.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=128.9, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='22', width=279.83):
            with Note(default_x=13.44, default_y=-860.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=145.65, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='23', width=275.63):
            with Note(default_x=13.8, default_y=-840.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=143.73, default_y=-875.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='24', width=245.07):
            with Note(default_x=13.8, default_y=-860.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')