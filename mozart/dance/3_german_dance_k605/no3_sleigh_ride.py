with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('3 German Dances')
    with Identification():
        Creator('W.A. Mozart', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(5.2)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2284.07)
            PageWidth(1615.84)
            with PageMargins(type='even'):
                LeftMargin(76.9231)
                RightMargin(76.9231)
                TopMargin(76.9231)
                BottomMargin(153.846)
            with PageMargins(type='odd'):
                LeftMargin(76.9231)
                RightMargin(76.9231)
                TopMargin(76.9231)
                BottomMargin(153.846)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('3 German Dances', default_x=807.922, default_y=2207.15, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('No. 3 "Sleigh Ride"', default_x=807.922, default_y=2130.23, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('W.A. Mozart', default_x=1538.92, default_y=2107.15, justify='right', valign='bottom', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Flauto piccolo.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piccolo')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(73)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Oboi.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Oboe')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Fagotti.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(71)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Schnell in A.')
            with ScoreInstrument(id='P4-I84'):
                InstrumentName('Cabasa')
            MidiDevice(None, port=1)
            with MidiInstrument(id='P4-I84'):
                MidiChannel(10)
                MidiProgram(1)
                MidiUnpitched(84)
                Volume(69.2913)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Schnell in F.')
            with ScoreInstrument(id='P5-I84'):
                InstrumentName('Cabasa')
            MidiDevice(None, port=2)
            with MidiInstrument(id='P5-I84'):
                MidiChannel(10)
                MidiProgram(1)
                MidiUnpitched(84)
                Volume(70.8661)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Schnell in E.')
            with ScoreInstrument(id='P6-I84'):
                InstrumentName('Cabasa')
            MidiDevice(None, port=3)
            with MidiInstrument(id='P6-I84'):
                MidiChannel(10)
                MidiProgram(1)
                MidiUnpitched(84)
                Volume(70.8661)
                Pan(0.0)
        with ScorePart(id='P7'):
            PartName('Schnell in C.')
            with ScoreInstrument(id='P7-I84'):
                InstrumentName('Cabasa')
            MidiDevice(None, port=4)
            with MidiInstrument(id='P7-I84'):
                MidiChannel(10)
                MidiProgram(1)
                MidiUnpitched(84)
                Volume(69.2913)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Schnell in G.')
            with ScoreInstrument(id='P8-I84'):
                InstrumentName('Cabasa')
            MidiDevice(None, port=5)
            with MidiInstrument(id='P8-I84'):
                MidiChannel(10)
                MidiProgram(1)
                MidiUnpitched(84)
                Volume(70.8661)
                Pan(0.0)
        with PartGroup(type='start', number='2'):
            GroupSymbol('brace')
        with ScorePart(id='P9'):
            PartName('B♭ Trumpet')
            with ScoreInstrument(id='P9-I1'):
                InstrumentName('B♭ Trumpet')
            MidiDevice(None, id='P9-I1', port=1)
            with MidiInstrument(id='P9-I1'):
                MidiChannel(4)
                MidiProgram(57)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P10'):
            PartName('Posthorn in F.')
            with ScoreInstrument(id='P10-I1'):
                InstrumentName('F Trumpet')
            MidiDevice(None, id='P10-I1', port=1)
            with MidiInstrument(id='P10-I1'):
                MidiChannel(6)
                MidiProgram(57)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='2')
        with ScorePart(id='P11'):
            PartName('Clarini in C.')
            with ScoreInstrument(id='P11-I1'):
                InstrumentName('C Trumpet')
            MidiDevice(None, id='P11-I1', port=1)
            with MidiInstrument(id='P11-I1'):
                MidiChannel(8)
                MidiProgram(57)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P12'):
            PartName('Timpani')
            with ScoreInstrument(id='P12-I1'):
                InstrumentName('Timpani')
            MidiDevice(None, id='P12-I1', port=1)
            with MidiInstrument(id='P12-I1'):
                MidiChannel(11)
                MidiProgram(48)
                Volume(86.6142)
                Pan(0.0)
        with PartGroup(type='start', number='2'):
            GroupSymbol('brace')
        with ScorePart(id='P13'):
            PartName('Violino I.')
            with ScoreInstrument(id='P13-I1'):
                InstrumentName('Violins')
            MidiDevice(None, id='P13-I1', port=1)
            with MidiInstrument(id='P13-I1'):
                MidiChannel(12)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P14'):
            PartName('Violino II.')
            with ScoreInstrument(id='P14-I1'):
                InstrumentName('Violins')
            MidiDevice(None, id='P14-I1', port=1)
            with MidiInstrument(id='P14-I1'):
                MidiChannel(15)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='2')
        with ScorePart(id='P15'):
            PartName('Basso')
            with ScoreInstrument(id='P15-I1'):
                InstrumentName('Violoncellos')
            MidiDevice(None, id='P15-I1', port=2)
            with MidiInstrument(id='P15-I1'):
                MidiChannel(2)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=206.9):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(177.53)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegro ', default_x=-36.0, default_y=21.88, relative_y=20.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, default_y=21.88, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('144')
                Sound(tempo=144.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=109.61, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.03, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.22, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.9, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.22, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.9, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=196.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=200.35, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.24, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.23, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.67, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.1, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.53, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.97, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.24, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.32, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.4, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.32, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.4, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=197.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.78, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.75, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.71, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio. Die Schlittenfahrt.', relative_x=-20.43, relative_y=29.79, font_weight='bold', font_size='12')
                Sound(tempo=80.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=32.15, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('134')
                Sound(tempo=134.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='29', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=170.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=149.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C.', relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Direction(placement='above'):
                with DirectionType():
                    Coda(default_x=-13.57, default_y=7.07, relative_y=20.0)
                Sound(coda='coda')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=31.11, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('150')
                Sound(tempo=150.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=142.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='42', width=140.34):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='43', width=193.82):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='44', width=140.34):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='45', width=193.82):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='46', width=158.36):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.25, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=108.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='47', width=162.73):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=61.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=111.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.27, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=88.55, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=111.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=135.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=181.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.08, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='49', width=99.9):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('144')
                Sound(tempo=144.0)
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=145.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=116.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=111.95):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.84, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=144.19, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.46, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=152.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=146.72):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='72', width=123.5):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=118.6):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.97, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=150.83, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='77', width=99.33):
            with Note(default_x=12.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=61.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(26.97)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=88.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=139.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=190.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=216.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=91.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=42.15, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=68.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Offset(-3.0)
                Sound(tempo=90.0)
        with Measure(number='85', width=140.66):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.71, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('144')
                Sound(tempo=144.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Offset(-3.0)
                Sound(tempo=90.0)
        with Measure(number='86', width=113.41):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Sound(tempo=120.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.71, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('144')
                Sound(tempo=144.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(82.96)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-47.4, relative_x=3.29, relative_y=-36.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=109.61, default_y=-152.96):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.61, default_y=-102.96):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.5, default_y=-162.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.5, default_y=-117.96):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=-152.96):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-117.96):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.44, default_y=-162.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.44, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=-152.96):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-117.96):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.87, default_y=-162.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=47.87, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.7, default_y=-162.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.7, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-162.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.0, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.35, default_y=-172.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.35, default_y=-137.96):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.69, default_y=-137.96):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.69, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-132.96):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-122.96):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-137.96):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.48, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-132.96):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-122.96):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-137.96):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.48, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=196.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-132.96):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-122.96):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.55, default_y=-132.96):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.55, default_y=-122.96):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.3, default_y=-132.96):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.3, default_y=-122.96):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=-137.96):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-127.96):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.72, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=200.35, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=200.35, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.67, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.67, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.53, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=141.53, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=87.76, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.76, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.88, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.88, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=197.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.75, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.75, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.71, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.71, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='29', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=170.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=149.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Direction(placement='above'):
                with DirectionType():
                    Words('a 2.', relative_y=40.0)
            with Note(default_x=15.8, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=127.29, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=142.95, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.85, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='42', width=140.34):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='43', width=193.82):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.49, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.15, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.05, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='44', width=140.34):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='45', width=193.82):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=123.49, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=139.15, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.05, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='46', width=158.36):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.25, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=108.5, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='47', width=162.73):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.71, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.42, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.16, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=181.77, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='49', width=99.9):
            with Note(default_x=15.44, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='50', width=95.74):
            with Note(default_x=12.36, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='51', width=108.33):
            with Note(default_x=12.36, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=24.95, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='52', width=108.33):
            with Note(default_x=12.36, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=24.95, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='53', width=145.03):
            with Note(default_x=16.16, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=16.16, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=145.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=116.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=111.95):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.84, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.84, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=152.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=146.72):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='72', width=123.5):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=118.6):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.97, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.97, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('a 2.', relative_y=35.0)
            with Note(default_x=44.07, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=72.33, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='77', width=99.33):
            with Note(default_x=12.94, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.2, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.47, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.72, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=61.64, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.56, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=107.48, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=130.4, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.13, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=139.71, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.3, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=190.88, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=216.46, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.82, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.82, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=62.31, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=91.37, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.44, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=149.51, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=42.15, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=68.51, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.86, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=121.21, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=147.57, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(107.93)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a 2.', relative_y=40.0)
            with Note(default_x=109.61, default_y=-260.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.5, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.44, default_y=-285.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.87, default_y=-285.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.28, default_y=-285.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-285.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-285.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-285.9):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.35, default_y=-295.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.69, default_y=-260.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-260.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-260.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=196.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.55, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.3, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=-260.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.24, default_y=-275.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.68, default_y=-295.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=200.35, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.67, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=141.53, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=87.76, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=197.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.75, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.71, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.44, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.09, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=108.56, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=212.78, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=241.63, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=158.08):
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.1, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.31, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=179.32):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=120.02, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=148.87, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=158.08):
            with Note(default_x=12.94, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.1, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.31, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=179.32):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=120.02, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=148.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=158.08):
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.1, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.31, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=188.06):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=125.64, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.05, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=142.02):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=108.56, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=201.71, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=227.49, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='26', width=180.46):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.12, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=117.76, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=158.88):
            with Note(default_x=12.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=105.73, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.51, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=180.46):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.12, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=117.76, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=169.93):
            with Note(default_x=12.94, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=169.93):
            with Note(default_x=12.94, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=170.85):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=114.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=141.91, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=97.0, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.27, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='54', width=118.34):
            with Note(default_x=12.94, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.88, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.8, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='55', width=140.66):
            with Note(default_x=15.8, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=94.21, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.9, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='56', width=125.58):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.09, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.69, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='57', width=144.78):
            with Note(default_x=15.8, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=96.75, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.02, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='58', width=118.34):
            with Note(default_x=12.94, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.88, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.8, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.19, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=163.2, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=183.94, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='60', width=142.63):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='61', width=140.08):
            with Note(default_x=15.44, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=92.05, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.31, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='62', width=145.93):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.1, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.74, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='63', width=140.08):
            with Note(default_x=15.44, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=92.05, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.31, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='64', width=116.86):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=46.4, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.66, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=111.95):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.84, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.19, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=171.44, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=194.71, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='70', width=152.57):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.42, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=95.94, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='71', width=146.72):
            with Note(default_x=15.44, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=98.69, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.96, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='72', width=123.5):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.45, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.26, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=118.6):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.97, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=99.33):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=69.47, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=190.88, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(45.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('percussion')
                    Line(2)
                with StaffDetails():
                    StaffLines(1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=104.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=139.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=134.97):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=196.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=125.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=206.0):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=197.26):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=140.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(45.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-45.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=12.94, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.1, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.31, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='21', width=179.32):
            with Note(default_x=16.16, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.32, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.02, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note(default_x=15.8, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.83, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(45.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-55.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.12, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=117.76, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note(default_x=15.8, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.12, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=117.76, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=169.93):
            with Note(default_x=12.94, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.59, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.9, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='31', width=170.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.08, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.36, default_y=-105.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(45.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=140.08):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.69, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.05, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='62', width=145.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=140.08):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.69, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.05, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='64', width=116.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=192.22):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=124.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(45.0)
            with Note(default_x=88.55, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.39, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=171.44, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='70', width=152.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=146.72):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.64, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.69, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P4-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='72', width=123.5):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='73', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='74', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='75', width=198.87):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='76', width=102.2):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='77', width=99.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='78', width=155.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-250.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='80', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='81', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='82', width=180.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='83', width=181.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='84', width=145.18):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('percussion')
                    Line(2)
                with StaffDetails():
                    StaffLines(1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=104.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=139.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=134.97):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=196.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=125.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=206.0):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=197.26):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=140.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(42.33)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-50.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=108.92, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=155.08, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=212.78, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note(default_x=12.94, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.1, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.31, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='21', width=179.32):
            with Note(default_x=16.16, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.32, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.02, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note(default_x=15.8, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.83, default_y=-187.33):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(52.87)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-49.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=108.92, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=150.16, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=201.71, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='26', width=180.46):
            with Note(default_x=15.8, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.12, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=117.76, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='27', width=158.88):
            with Note(default_x=12.94, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.18, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.73, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='28', width=180.46):
            with Note(default_x=15.8, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.12, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=117.76, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=169.93):
            with Note(default_x=12.94, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.59, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.9, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='31', width=170.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.08, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.36, default_y=-197.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(295.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-50.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=25.31, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.45, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.59, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='52', width=108.33):
            with Note(default_x=25.31, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.45, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.59, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='53', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=118.34):
            with Note(default_x=12.94, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.88, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='55', width=140.66):
            with Note(default_x=16.16, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=50.85, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.21, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note(default_x=12.94, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.88, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note(default_x=88.55, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.73, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.2, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='60', width=142.63):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=140.08):
            with Note(default_x=15.8, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.69, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.05, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='62', width=145.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=140.08):
            with Note(default_x=15.8, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.69, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.05, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='64', width=116.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=192.22):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=124.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note(default_x=88.55, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.39, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=171.44, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='70', width=152.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=146.72):
            with Note(default_x=15.8, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.64, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.69, default_y=-380.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P5-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='72', width=123.5):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='73', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='74', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='75', width=198.87):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='76', width=102.2):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='77', width=99.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='78', width=155.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='80', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='81', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='82', width=180.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='83', width=181.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='84', width=145.18):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('percussion')
                    Line(2)
                with StaffDetails():
                    StaffLines(1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=104.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=139.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=134.97):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=196.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=125.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=206.0):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=197.26):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=140.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(30.83)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-55.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=12.94, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.1, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.31, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=179.32):
            with Note(default_x=16.16, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.32, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.02, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note(default_x=12.94, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.1, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.31, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=188.06):
            with Note(default_x=16.16, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.82, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.64, default_y=-258.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(30.37)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='29', width=169.93):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-59.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.94, default_y=-268.24):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.59, default_y=-268.24):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.9, default_y=-268.24):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='30', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=170.85):
            with Note(default_x=16.16, default_y=-268.24):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.9, default_y=-268.24):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.57, default_y=-268.24):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='32', width=149.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(30.83)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-45.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.16, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.09, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.0, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note(default_x=15.8, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.09, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.69, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='57', width=144.78):
            with Note(default_x=16.16, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.98, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.75, default_y=-385.83):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note(default_x=15.8, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.96, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.16, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=145.93):
            with Note(default_x=15.8, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.1, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.74, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='63', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=116.86):
            with Note(default_x=15.8, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.4, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.66, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='65', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=192.22):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.16, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.52, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=152.57):
            with Note(default_x=15.8, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.42, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.94, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='71', width=146.72):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='72', width=123.5):
            with Note(default_x=15.8, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.45, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=89.26, default_y=-445.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='73', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='74', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='75', width=198.87):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='76', width=102.2):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='77', width=99.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='78', width=155.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(295.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-54.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=88.55, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.71, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.31, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.44, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.04, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.27, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='85', width=140.66):
            with Note(default_x=12.36, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.22, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.09, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='86', width=113.41):
            with Note(default_x=12.36, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.51, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.66, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='87', width=122.12):
            with Note(default_x=12.0, default_y=-315.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P6-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('percussion')
                    Line(2)
                with StaffDetails():
                    StaffLines(1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=104.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=139.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=134.97):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=196.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=125.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=206.0):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=197.26):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=140.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(35.83)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-48.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.16, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.32, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.02, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=158.08):
            with Note(default_x=12.94, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.1, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.31, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=188.06):
            with Note(default_x=16.16, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.82, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.64, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=142.02):
            with Note(default_x=15.8, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.82, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.83, default_y=-333.98):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(56.87)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-61.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.12, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=117.76, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note(default_x=15.8, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.12, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=117.76, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=169.93):
            with Note(default_x=12.94, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.59, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.9, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='30', width=169.93):
            with Note(default_x=12.94, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.59, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.9, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='31', width=170.85):
            with Note(default_x=16.16, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.9, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.57, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.08, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.36, default_y=-365.11):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(42.33)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-47.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.16, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.09, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.0, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note(default_x=15.8, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.09, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.69, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='57', width=144.78):
            with Note(default_x=16.16, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.98, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.75, default_y=-468.15):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.96, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.16, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=140.08):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.69, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.05, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='62', width=145.93):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.1, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.74, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='63', width=140.08):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.69, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.05, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='64', width=116.86):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.4, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.66, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='65', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=192.22):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.16, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.52, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note(default_x=88.55, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.39, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=171.44, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='70', width=152.57):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.42, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.94, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='71', width=146.72):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.64, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=98.69, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='72', width=123.5):
            with Note(default_x=15.8, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.45, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=89.26, default_y=-510.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='73', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='74', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='75', width=198.87):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='76', width=102.2):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='77', width=99.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='78', width=155.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(51.87)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-54.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=88.55, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.71, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.31, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.44, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.04, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.27, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='85', width=140.66):
            with Note(default_x=12.36, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.22, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.09, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='86', width=113.41):
            with Note(default_x=12.36, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.51, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.66, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='87', width=122.12):
            with Note(default_x=12.0, default_y=-406.87):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P7-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('percussion')
                    Line(2)
                with StaffDetails():
                    StaffLines(1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=104.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=139.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=134.97):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=196.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=125.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=206.0):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=197.26):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=140.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(28.83)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-53.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=16.16, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.32, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.02, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note(default_x=12.94, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.1, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.31, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=188.06):
            with Note(default_x=16.16, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.82, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=125.64, default_y=-402.81):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(42.37)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='29', width=169.93):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-55.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.94, default_y=-447.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.59, default_y=-447.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.9, default_y=-447.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='30', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=170.85):
            with Note(default_x=16.16, default_y=-447.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.9, default_y=-447.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.57, default_y=-447.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='32', width=149.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(44.33)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-43.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=15.8, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.3, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=70.8, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='50', width=95.74):
            with Note(default_x=12.72, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=39.86, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.0, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='51', width=108.33):
            with Note(default_x=25.31, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.45, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.59, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='52', width=108.33):
            with Note(default_x=25.31, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.45, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=79.59, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='53', width=145.03):
            with Note(default_x=16.16, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.09, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.0, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='54', width=118.34):
            with Note(default_x=12.94, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.88, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.8, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='55', width=140.66):
            with Note(default_x=16.16, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=50.85, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.21, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='56', width=125.58):
            with Note(default_x=15.8, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.09, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.69, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='57', width=144.78):
            with Note(default_x=16.16, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.98, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.75, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='58', width=118.34):
            with Note(default_x=12.94, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.88, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.8, default_y=-552.48):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note(default_x=88.55, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.73, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.2, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='60', width=142.63):
            with Note(default_x=15.8, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.96, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.16, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='61', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=145.93):
            with Note(default_x=15.8, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.1, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=90.74, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='63', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=116.86):
            with Note(default_x=15.8, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.4, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.66, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='65', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=192.22):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.16, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.52, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(25.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=152.57):
            with Note(default_x=15.8, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.42, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=95.94, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='71', width=146.72):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='72', width=123.5):
            with Note(default_x=15.8, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.45, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=89.26, default_y=-575.0):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='73', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='74', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='75', width=198.87):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='76', width=102.2):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='77', width=99.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='78', width=155.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(51.87)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=-51.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=88.55, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.71, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=190.88, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=103.59, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.31, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=120.44, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.04, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.27, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='85', width=140.66):
            with Note(default_x=12.36, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.22, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=84.09, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='86', width=113.41):
            with Note(default_x=12.36, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.51, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.66, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='87', width=122.12):
            with Note(default_x=12.0, default_y=-498.74):
                with Unpitched():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Instrument(id='P8-I84')
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P9'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(45.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(-1)
                    Chromatic(-2.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=104.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=139.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=134.97):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=196.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=125.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=206.0):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=197.26):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=140.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-422.81)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(46.37)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=108.56, default_y=-543.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='26', width=180.46):
            with Note(default_x=15.8, default_y=-508.85):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=146.08, default_y=-543.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='27', width=158.88):
            with Note(default_x=12.58, default_y=-543.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='28', width=180.46):
            with Note(default_x=15.8, default_y=-508.85):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=170.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=149.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                with Key():
                    Fifths(2)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-572.48)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-595.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=145.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=116.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=192.22):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=124.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-595.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=152.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=146.72):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='72', width=123.5):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='73', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='74', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='75', width=198.87):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='76', width=102.2):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='77', width=99.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='78', width=155.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-518.74)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='80', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='81', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='82', width=180.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='83', width=181.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='84', width=145.18):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P10'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(3)
                    Chromatic(5.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='2', width=104.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='3', width=139.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='4', width=134.97):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='5', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='6', width=187.91):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='7', width=196.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='8', width=125.3):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='10', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='11', width=206.0):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='12', width=135.01):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='13', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='14', width=188.52):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='15', width=197.26):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='16', width=140.94):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=146.08, default_y=-648.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='29', width=169.93):
            with Note(default_x=12.58, default_y=-648.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.56, default_y=-648.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='30', width=169.93):
            with Note(default_x=12.58, default_y=-648.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.56, default_y=-648.85):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='31', width=170.85):
            with Note(default_x=15.8, default_y=-613.85):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-623.85):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                with Key():
                    Fifths(1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='34', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='35', width=246.11):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='36', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='37', width=212.23):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='38', width=166.38):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='39', width=157.64):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='41', width=197.62):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='42', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='43', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='44', width=140.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='45', width=193.82):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='46', width=158.36):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='47', width=162.73):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(640.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=108.26, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='61', width=140.08):
            with Note(default_x=15.44, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='62', width=145.93):
            with Note(default_x=15.8, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=111.55, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='63', width=140.08):
            with Note(default_x=15.44, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='64', width=116.86):
            with Note(default_x=15.8, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='65', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='66', width=111.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='67', width=192.22):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='68', width=124.62):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=90.24, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(640.0)
            with Note(default_x=88.19, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='70', width=152.57):
            with Note(default_x=15.8, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=118.2, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='71', width=146.72):
            with Note(default_x=15.44, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='72', width=123.5):
            with Note(default_x=15.8, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='73', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='74', width=118.6):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='75', width=198.87):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='76', width=102.2):
            with Note(default_x=15.44, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='77', width=99.33):
            with Note(default_x=12.94, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.44, default_y=-670.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(563.74)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='80', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='81', width=153.95):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='82', width=180.17):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='83', width=181.94):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=147.57, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.44, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=88.27, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=120.41, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='85', width=140.66):
            with Note(default_x=12.0, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.09, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=115.89, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='86', width=113.41):
            with Note(default_x=12.0, default_y=-593.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='87', width=122.12):
            with Note(default_x=12.0, default_y=-558.74):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P11'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a 2.', relative_y=29.0)
            with Note(default_x=109.61, default_y=-925.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.5, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.44, default_y=-950.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.87, default_y=-950.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.28, default_y=-950.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-950.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-950.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-950.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.35, default_y=-960.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.69, default_y=-960.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.69, default_y=-925.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.48, default_y=-960.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.48, default_y=-925.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Note(default_x=15.44, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Forward():
                Duration(12.0)
        with Measure(number='6', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.48, default_y=-960.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.48, default_y=-925.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Note(default_x=15.44, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Forward():
                Duration(12.0)
        with Measure(number='7', width=196.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.55, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.3, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Note(default_x=15.8, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.55, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.3, default_y=-940.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=-960.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-940.9):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(315.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.72, default_y=-325.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=200.35, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=158.54, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=200.35, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-325.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-325.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.67, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.53, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=78.67, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.53, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-325.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=87.76, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.76, default_y=-330.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.88, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.88, default_y=-330.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Note(default_x=15.44, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Forward():
                Duration(12.0)
        with Measure(number='14', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=129.88, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.88, default_y=-330.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Note(default_x=15.44, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Forward():
                Duration(12.0)
        with Measure(number='15', width=197.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.75, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.71, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Note(default_x=15.8, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.75, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.71, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-345.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-658.85)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='29', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=170.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=149.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a 2.', relative_y=32.0)
            with Note(default_x=89.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=137.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=174.79, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=211.7, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=248.62, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='34', width=166.38):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=246.11):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=64.07, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=100.98, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=100.98, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=137.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.9, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=174.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=174.81, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='36', width=166.38):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=212.23):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.78, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=82.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=82.83, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=111.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=111.88, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=140.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=140.93, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='38', width=166.38):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=157.64):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.87, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.95, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(210.0)
            with Note(default_x=88.55, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.55, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.17, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.17, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.79, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=193.79, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='41', width=197.62):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(36.0)
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(24.0)
        with Measure(number='42', width=140.34):
            with Direction(placement='above'):
                with DirectionType():
                    Words('a 2.', relative_y=33.0)
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.03, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.06, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='43', width=193.82):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='44', width=140.34):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.03, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.06, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='45', width=193.82):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=158.36):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.25, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.5, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='47', width=162.73):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.71, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.42, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=145.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=116.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=111.95):
            with Note(default_x=15.8, default_y=-760.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-750.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-760.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-750.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-760.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-750.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.84, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.84, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-795.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-760.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=152.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=146.72):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='72', width=123.5):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=118.6):
            with Note(default_x=15.8, default_y=-760.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-750.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-760.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-750.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-760.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-750.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.97, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.97, default_y=-755.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=-795.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-760.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('a 2.', relative_y=33.0)
            with Note(default_x=44.07, default_y=-785.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=72.33, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='77', width=99.33):
            with Note(default_x=12.94, default_y=-785.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=41.2, default_y=-795.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-795.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.64, default_y=-785.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=107.48, default_y=-775.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-708.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=139.71, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='80', width=153.95):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=54.82, default_y=-698.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.82, default_y=-683.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=79.2, default_y=-698.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=79.2, default_y=-683.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=103.59, default_y=-698.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=103.59, default_y=-683.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=127.97, default_y=-698.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=127.97, default_y=-683.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-698.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-683.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-708.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.82, default_y=-698.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=79.2, default_y=-708.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=79.2, default_y=-698.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=103.59, default_y=-708.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=103.59, default_y=-698.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=127.97, default_y=-708.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=127.97, default_y=-698.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-708.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-698.74):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.31, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.31, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=91.37, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=91.37, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.44, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=120.44, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=149.51, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=149.51, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-718.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-708.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P12'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=109.61, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.5, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.44, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.87, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.28, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.35, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.69, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=187.91):
            with Note(default_x=15.8, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=129.48, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=187.91):
            with Note(default_x=15.8, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=129.48, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=196.65):
            with Note(default_x=15.8, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.55, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.3, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=165.18, default_y=-1055.9):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=-1040.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.78, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.76, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=87.76, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=188.52):
            with Note(default_x=15.8, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=129.88, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=188.52):
            with Note(default_x=15.8, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=129.88, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=197.26):
            with Note(default_x=15.8, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=75.75, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=105.73, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=135.71, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=165.68, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='18', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='19', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='20', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='21', width=179.32):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='22', width=158.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='23', width=188.06):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='24', width=142.02):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='26', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='27', width=158.88):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='28', width=180.46):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='29', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='30', width=169.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='31', width=170.85):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='32', width=149.65):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=89.6, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=211.7, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=248.62, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='34', width=166.38):
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=84.97, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=111.57, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=138.18, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='35', width=246.11):
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=137.9, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=174.81, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='36', width=166.38):
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=84.97, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=111.57, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=138.18, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=212.23):
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=111.88, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=140.93, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='38', width=166.38):
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=84.97, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=111.57, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=138.18, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='39', width=157.64):
            with Note(default_x=15.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.87, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=80.91, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=105.95, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.17, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.79, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='41', width=197.62):
            with Note(default_x=15.8, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='42', width=140.34):
            with Note(default_x=12.0, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.03, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.06, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='43', width=193.82):
            with Note(default_x=12.0, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='44', width=140.34):
            with Note(default_x=12.0, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.03, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.06, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='45', width=193.82):
            with Note(default_x=12.0, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='46', width=158.36):
            with Note(default_x=12.0, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.25, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.5, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='47', width=162.73):
            with Note(default_x=12.0, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=61.71, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.42, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='49', width=99.9):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='54', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='55', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='56', width=125.58):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='57', width=144.78):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='58', width=118.34):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='60', width=142.63):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='61', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='62', width=145.93):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='63', width=140.08):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='64', width=116.86):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.32, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.84, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='66', width=111.95):
            with Note(default_x=15.8, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.32, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=78.84, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=56.15, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=114.84, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=144.19, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='70', width=152.57):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='71', width=146.72):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='72', width=123.5):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.53, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.27, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='74', width=118.6):
            with Note(default_x=15.8, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=49.53, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=83.27, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.24, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=119.97, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=150.83, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=99.33):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=69.47, default_y=-890.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-875.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=190.88, default_y=-813.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=79.2, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=103.59, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.97, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.82, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=79.2, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=103.59, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.97, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.31, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=91.37, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=120.44, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=149.51, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-798.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P13'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(82.96)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=109.61, default_y=-1168.86):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.61, default_y=-1143.86):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=109.61, default_y=-1118.86):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.5, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.44, default_y=-1143.86):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.87, default_y=-1143.86):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.28, default_y=-1143.86):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-1143.86):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-1143.86):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-1143.86):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.35, default_y=-1153.86):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.69, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.03, default_y=-1118.86):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-1118.86):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.22, default_y=-1123.86):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.64, default_y=-1128.86):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.06, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.48, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.9, default_y=-1118.86):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-1118.86):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.22, default_y=-1123.86):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.64, default_y=-1128.86):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.06, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.48, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.9, default_y=-1118.86):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=196.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-1118.86):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.68, default_y=-1123.86):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.55, default_y=-1128.86):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.43, default_y=-1133.86):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.3, default_y=-1128.86):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.18, default_y=-1123.86):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=-1118.86):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=200.35, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=-510.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.78, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.76, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.24, default_y=-510.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.23, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.67, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.1, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.53, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.97, default_y=-500.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=-510.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.78, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.76, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.24, default_y=-505.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-505.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.32, default_y=-510.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.84, default_y=-515.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.36, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.88, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.4, default_y=-505.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='14', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-505.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.32, default_y=-510.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.84, default_y=-515.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.36, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.88, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.4, default_y=-505.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=197.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-505.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.78, default_y=-510.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=75.75, default_y=-515.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.73, default_y=-520.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.71, default_y=-515.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.68, default_y=-510.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=-505.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(486.69)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=108.56, default_y=-486.69):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=212.78, default_y=-476.69):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=241.63, default_y=-486.69):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=158.08):
            with Note(default_x=12.94, default_y=-491.69):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.1, default_y=-481.69):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.31, default_y=-471.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=179.32):
            with Note(default_x=15.8, default_y=-471.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=120.02, default_y=-481.69):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=148.87, default_y=-491.69):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=158.08):
            with Note(default_x=12.94, default_y=-486.69):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.1, default_y=-476.69):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.31, default_y=-466.69):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=179.32):
            with Note(default_x=15.8, default_y=-466.69):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=120.02, default_y=-476.69):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=148.87, default_y=-486.69):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=158.08):
            with Note(default_x=12.94, default_y=-491.69):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.1, default_y=-481.69):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.31, default_y=-471.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=188.06):
            with Note(default_x=15.8, default_y=-471.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=125.64, default_y=-481.69):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.05, default_y=-491.69):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=142.02):
            with Note(default_x=15.8, default_y=-486.69):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(723.85)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=108.56, default_y=-723.85):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=201.71, default_y=-708.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=227.49, default_y=-698.85):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='26', width=180.46):
            with Note(default_x=15.8, default_y=-703.85):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.12, default_y=-713.85):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=117.76, default_y=-723.85):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=158.88):
            with Note(default_x=12.58, default_y=-723.85):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=105.73, default_y=-708.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.51, default_y=-698.85):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=180.46):
            with Note(default_x=15.8, default_y=-703.85):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.12, default_y=-713.85):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=117.76, default_y=-723.85):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=169.93):
            with Note(default_x=12.58, default_y=-728.85):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=108.9, default_y=-718.85):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.56, default_y=-728.85):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='30', width=169.93):
            with Note(default_x=12.94, default_y=-723.85):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.59, default_y=-713.85):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=108.9, default_y=-703.85):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=170.85):
            with Note(default_x=15.8, default_y=-708.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=114.57, default_y=-718.85):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=141.91, default_y=-728.85):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-723.85):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=89.6, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.62, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=271.88, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.15, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='34', width=166.38):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=246.11):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=174.81, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=198.08, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.35, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='36', width=166.38):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=212.23):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=140.93, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=164.2, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.46, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='38', width=166.38):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=157.64):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.87, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=80.91, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=105.95, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-425.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.86, default_y=-425.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.17, default_y=-415.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=167.48, default_y=-415.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=193.79, default_y=-400.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=220.11, default_y=-400.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='41', width=197.62):
            with Note(default_x=15.8, default_y=-405.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.64, default_y=-450.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.52, default_y=-450.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.41, default_y=-450.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.29, default_y=-450.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='42', width=140.34):
            with Note(default_x=12.0, default_y=-450.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=-465.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=-450.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='43', width=193.82):
            with Note(default_x=12.0, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.84, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=71.72, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.61, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.49, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='44', width=140.34):
            with Note(default_x=12.0, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=-450.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='45', width=193.82):
            with Note(default_x=12.0, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.84, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=71.72, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.61, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.49, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='46', width=158.36):
            with Note(default_x=12.0, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.25, default_y=-440.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=108.5, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=162.73):
            with Note(default_x=12.0, default_y=-415.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.71, default_y=-430.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.42, default_y=-415.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(617.48)
            with Note(default_x=88.55, default_y=-602.48):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.16, default_y=-612.48):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=181.77, default_y=-592.48):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='49', width=99.9):
            with Note(default_x=15.8, default_y=-682.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-647.48):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-632.48):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=97.0, default_y=-622.48):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.27, default_y=-632.48):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='54', width=118.34):
            with Note(default_x=12.94, default_y=-637.48):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.88, default_y=-627.48):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.8, default_y=-617.48):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='55', width=140.66):
            with Note(default_x=15.8, default_y=-617.48):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=94.21, default_y=-627.48):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.9, default_y=-637.48):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='56', width=125.58):
            with Note(default_x=15.8, default_y=-632.48):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.09, default_y=-622.48):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.69, default_y=-612.48):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='57', width=144.78):
            with Note(default_x=15.8, default_y=-612.48):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=96.75, default_y=-622.48):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.02, default_y=-632.48):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='58', width=118.34):
            with Note(default_x=12.94, default_y=-637.48):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.88, default_y=-627.48):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.8, default_y=-617.48):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.39)
            with Note(default_x=88.19, default_y=-961.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=163.2, default_y=-971.39):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=183.94, default_y=-981.39):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='60', width=142.63):
            with Note(default_x=15.8, default_y=-976.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='61', width=140.08):
            with Note(default_x=15.44, default_y=-961.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=92.05, default_y=-951.39):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.31, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='62', width=145.93):
            with Note(default_x=15.8, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.1, default_y=-956.39):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.74, default_y=-966.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='63', width=140.08):
            with Note(default_x=15.44, default_y=-961.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=92.05, default_y=-951.39):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.31, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='64', width=116.86):
            with Note(default_x=15.8, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=46.4, default_y=-956.39):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.66, default_y=-966.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-991.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-971.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-946.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-946.39):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-946.39):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=111.95):
            with Note(default_x=15.8, default_y=-991.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-966.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-941.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=-936.39):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-936.39):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.5, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=114.84, default_y=-946.39):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=144.19, default_y=-936.39):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(71.39)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=88.19, default_y=-961.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=171.44, default_y=-951.39):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=194.71, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='70', width=152.57):
            with Note(default_x=15.8, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.42, default_y=-956.39):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=95.94, default_y=-966.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='71', width=146.72):
            with Note(default_x=15.44, default_y=-961.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=98.69, default_y=-951.39):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.96, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='72', width=123.5):
            with Note(default_x=15.8, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.45, default_y=-956.39):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=89.26, default_y=-966.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-991.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-971.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-946.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-946.39):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-946.39):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=118.6):
            with Note(default_x=15.8, default_y=-991.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-966.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-941.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=-936.39):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-936.39):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.1, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=119.97, default_y=-946.39):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.83, default_y=-936.39):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=-941.39):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=99.33):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=69.47, default_y=-991.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.47, default_y=-971.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.47, default_y=-946.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-991.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-966.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-941.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=190.88, default_y=-908.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.88, default_y=-888.74):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.88, default_y=-863.74):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-908.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-883.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-858.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-908.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-883.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-858.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-908.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-883.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-858.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-908.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-883.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-858.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.51, default_y=-883.74):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.51, default_y=-858.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.21, default_y=-883.74):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.21, default_y=-858.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-908.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-883.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-858.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P14'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(86.36)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=109.61, default_y=-1295.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.61, default_y=-1270.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=109.61, default_y=-1245.22):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.5, default_y=-1260.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=-1260.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.44, default_y=-1270.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=-1260.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.87, default_y=-1270.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.28, default_y=-1270.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-1270.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-1270.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-1270.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.35, default_y=-1280.22):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('div.', relative_y=30.0)
            with Note(default_x=86.69, default_y=-1280.22):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.69, default_y=-1270.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-1275.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-1265.22):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-1280.22):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.48, default_y=-1270.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-1275.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-1265.22):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-1280.22):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.48, default_y=-1270.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=196.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-1275.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1265.22):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.55, default_y=-1275.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.55, default_y=-1265.22):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.3, default_y=-1275.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.3, default_y=-1265.22):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=-1280.22):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1270.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=200.35, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=-650.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.78, default_y=-660.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.76, default_y=-660.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=110.24, default_y=-650.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.23, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=78.67, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.1, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.53, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.97, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=-650.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.78, default_y=-660.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='above'):
                with DirectionType():
                    Words('div.', relative_y=30.0)
            with Note(default_x=87.76, default_y=-645.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.76, default_y=-635.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-630.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-645.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.88, default_y=-635.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=15.44, default_y=-630.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-645.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.88, default_y=-635.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=197.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-630.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.75, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.75, default_y=-630.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.71, default_y=-640.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.71, default_y=-630.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=-645.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-635.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-52.65, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=155.08, default_y=-651.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=183.93, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=212.78, default_y=-651.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='18', width=158.08):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=57.1, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=84.71, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=112.31, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=179.32):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=62.32, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=91.17, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=120.02, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=158.08):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=57.1, default_y=-651.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=84.71, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=112.31, default_y=-651.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=179.32):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=62.32, default_y=-651.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=91.17, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=120.02, default_y=-651.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='22', width=158.08):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=57.1, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=84.71, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=112.31, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='23', width=188.06):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=64.82, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=95.23, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=125.64, default_y=-646.69):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=156.05, default_y=-641.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=142.02):
            with Note(default_x=15.8, default_y=-651.69):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.31, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=150.16, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=175.94, default_y=-873.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=201.71, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='26', width=180.46):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=61.12, default_y=-888.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=89.44, default_y=-878.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=117.76, default_y=-888.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=158.88):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=54.18, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=79.96, default_y=-873.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=105.73, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=180.46):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=61.12, default_y=-888.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=89.44, default_y=-878.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=117.76, default_y=-888.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=169.93):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=55.59, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=82.25, default_y=-878.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.9, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='30', width=169.93):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=55.59, default_y=-888.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=82.25, default_y=-878.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.9, default_y=-888.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=170.85):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=59.9, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=87.24, default_y=-878.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=114.57, default_y=-883.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=141.91, default_y=-878.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-888.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Key():
                    Fifths(0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=89.6, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.62, default_y=-380.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=271.88, default_y=-375.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.15, default_y=-370.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='34', width=166.38):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=246.11):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=174.81, default_y=-380.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=198.08, default_y=-375.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.35, default_y=-370.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='36', width=166.38):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=212.23):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=140.93, default_y=-380.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=164.2, default_y=-375.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.46, default_y=-370.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='38', width=166.38):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=157.64):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.87, default_y=-355.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=80.91, default_y=-355.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=105.95, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.0, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.86, default_y=-540.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=141.17, default_y=-530.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=167.48, default_y=-530.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=193.79, default_y=-530.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=220.11, default_y=-530.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='41', width=197.62):
            with Note(default_x=15.8, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.64, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.52, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=101.41, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.29, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='42', width=140.34):
            with Note(default_x=12.0, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=-570.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='43', width=193.82):
            with Note(default_x=12.0, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.84, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=71.72, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.61, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.49, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='44', width=140.34):
            with Note(default_x=12.0, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.03, default_y=-570.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.06, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='45', width=193.82):
            with Note(default_x=12.0, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.84, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=71.72, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=97.61, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.49, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='46', width=158.36):
            with Note(default_x=12.0, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.25, default_y=-555.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=108.5, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=162.73):
            with Note(default_x=12.0, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.71, default_y=-545.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.42, default_y=-535.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-717.48):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.16, default_y=-732.48):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=181.77, default_y=-707.48):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='49', width=99.9):
            with Note(default_x=15.8, default_y=-787.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-752.48):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.85, relative_x=6.58, relative_y=-45.0):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.85, relative_x=6.58, relative_y=-46.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=52.09, default_y=-762.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.54, default_y=-752.48):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=97.0, default_y=-762.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=51.73, default_y=-787.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='54', width=118.34):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=44.88, default_y=-757.48):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=64.84, default_y=-752.48):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=84.8, default_y=-757.48):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=44.52, default_y=-787.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='55', width=140.66):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=50.85, default_y=-757.48):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.53, default_y=-752.48):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.21, default_y=-757.48):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=50.49, default_y=-787.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='56', width=125.58):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.09, default_y=-762.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=69.89, default_y=-752.48):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.69, default_y=-762.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=48.72, default_y=-787.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='57', width=144.78):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=51.98, default_y=-762.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.37, default_y=-752.48):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=96.75, default_y=-762.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=51.62, default_y=-787.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='58', width=118.34):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=44.88, default_y=-757.48):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=64.84, default_y=-752.48):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=84.8, default_y=-757.48):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=44.52, default_y=-787.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.51)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=121.73, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=142.47, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=163.2, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=121.37, default_y=-1139.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='60', width=142.63):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=47.96, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.06, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.16, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=47.6, default_y=-1139.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='61', width=140.08):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.69, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.87, default_y=-1099.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.05, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=49.33, default_y=-1134.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='62', width=145.93):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.1, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=69.92, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.74, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=48.74, default_y=-1139.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='63', width=140.08):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.69, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.87, default_y=-1099.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.05, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=49.33, default_y=-1134.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='64', width=116.86):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=46.4, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.53, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=84.66, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=46.04, default_y=-1139.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1084.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-1084.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-1084.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=111.95):
            with Direction(placement='above'):
                with DirectionType():
                    Words('div.', relative_y=35.0)
            with Note(default_x=15.8, default_y=-1089.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1079.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-1089.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-1079.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-1089.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-1079.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=-1074.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-1074.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.5, default_y=-1079.9):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=114.84, default_y=-1084.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=144.19, default_y=-1074.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-1079.9):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.51)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-59.55, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-59.55, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=125.39, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=148.42, default_y=-1099.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=171.44, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=125.03, default_y=-1134.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='70', width=152.57):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=51.42, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=73.68, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.94, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=51.06, default_y=-1139.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='71', width=146.72):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=52.64, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.67, default_y=-1099.9):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=98.69, default_y=-1109.9):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=52.28, default_y=-1134.9):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='72', width=123.5):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=48.45, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.85, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=89.26, default_y=-1114.9):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=48.09, default_y=-1139.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.4, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1084.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-1084.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-1084.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=118.6):
            with Direction(placement='above'):
                with DirectionType():
                    Words('div.', relative_y=35.0)
            with Note(default_x=15.8, default_y=-1089.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1079.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-1089.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-1079.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-1089.9):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-1079.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=-1074.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-1074.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.1, default_y=-1079.9):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=119.97, default_y=-1084.9):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=150.83, default_y=-1074.9):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=-1079.9):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=99.33):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=69.47, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.47, default_y=-1084.9):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=69.47, default_y=-1059.9):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-1104.9):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1079.9):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-1054.9):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=190.88, default_y=-1013.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.88, default_y=-993.74):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.88, default_y=-968.74):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-1013.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-988.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-963.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-1013.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-988.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-963.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-1013.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-988.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-963.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-1013.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-988.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-963.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.51, default_y=-988.74):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.51, default_y=-963.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.21, default_y=-988.74):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.21, default_y=-963.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-1013.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-988.74):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-963.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P15'):
        with Measure(number='1', width=206.9):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(76.36)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=109.61, default_y=-1371.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.5, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='2', width=104.93):
            with Note(default_x=12.0, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.44, default_y=-1396.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=139.88):
            with Note(default_x=12.0, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.87, default_y=-1396.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.28, default_y=-1396.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-1396.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-1396.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=134.97):
            with Note(default_x=12.0, default_y=-1396.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.35, default_y=-1406.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=86.69, default_y=-1371.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-1371.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='6', width=187.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.48, default_y=-1371.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=196.65):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.55, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.3, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=125.3):
            with Note(default_x=15.8, default_y=-1371.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.24, default_y=-1386.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.68, default_y=-1406.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=243.76):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=116.72, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=158.54, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=200.35, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=135.01):
            with Note(default_x=15.8, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=206.0):
            with Note(default_x=15.8, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.67, default_y=-745.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=141.53, default_y=-755.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=135.01):
            with Note(default_x=15.8, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=87.76, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='14', width=188.52):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.44, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=129.88, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=197.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=75.75, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.71, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='16', width=140.94):
            with Note(default_x=15.8, default_y=-725.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.44, default_y=-740.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.09, default_y=-760.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=272.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Key():
                    Fifths(-1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=108.92, default_y=-706.69):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='18', width=158.08):
            with Note(default_x=12.94, default_y=-721.69):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='19', width=179.32):
            with Note(default_x=16.16, default_y=-721.69):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='20', width=158.08):
            with Note(default_x=12.94, default_y=-706.69):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=179.32):
            with Note(default_x=16.16, default_y=-706.69):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='22', width=158.08):
            with Note(default_x=12.94, default_y=-721.69):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='23', width=188.06):
            with Note(default_x=16.16, default_y=-721.69):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='24', width=142.02):
            with Note(default_x=15.8, default_y=-706.69):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.82, default_y=-721.69):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=87.83, default_y=-741.69):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='25', width=254.87):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.68)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=108.92, default_y=-946.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=180.46):
            with Note(default_x=15.8, default_y=-946.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=158.88):
            with Note(default_x=12.94, default_y=-946.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='28', width=180.46):
            with Note(default_x=15.8, default_y=-946.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='29', width=169.93):
            with Note(default_x=12.94, default_y=-961.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='30', width=169.93):
            with Note(default_x=12.94, default_y=-946.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='31', width=170.85):
            with Note(default_x=16.16, default_y=-961.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='32', width=149.65):
            with Note(default_x=15.8, default_y=-946.53):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.08, default_y=-961.53):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.36, default_y=-981.53):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='33', width=319.91):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.71)
            with Attributes():
                with Key():
                    Fifths(0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=89.6, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.62, default_y=-461.71):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=271.88, default_y=-456.71):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.15, default_y=-451.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='34', width=166.38):
            with Note(default_x=15.8, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=246.11):
            with Note(default_x=15.8, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=174.81, default_y=-461.71):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=198.08, default_y=-456.71):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.35, default_y=-451.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='36', width=166.38):
            with Note(default_x=15.8, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=212.23):
            with Note(default_x=15.8, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=140.93, default_y=-461.71):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=164.2, default_y=-456.71):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.46, default_y=-451.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='38', width=166.38):
            with Note(default_x=15.8, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.37, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=111.57, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=157.64):
            with Note(default_x=15.8, default_y=-446.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.87, default_y=-411.71):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=105.95, default_y=-426.71):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='40', width=248.02):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.17, default_y=-655.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.79, default_y=-645.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='41', width=197.62):
            with Note(default_x=15.8, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=101.41, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=127.29, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=140.34):
            with Note(default_x=12.0, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=48.03, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.54, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.06, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.58, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='43', width=193.82):
            with Note(default_x=12.0, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=97.61, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.49, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='44', width=140.34):
            with Note(default_x=12.0, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=48.03, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.54, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=93.06, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=115.58, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='45', width=193.82):
            with Note(default_x=12.0, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=97.61, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.49, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='46', width=158.36):
            with Note(default_x=12.0, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.13, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=60.25, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.38, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=108.5, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=132.63, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='47', width=162.73):
            with Note(default_x=12.0, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.85, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=61.71, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.56, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=111.42, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.27, default_y=-635.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='48', width=229.99):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=111.86, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=135.16, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.47, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=181.77, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=205.08, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='49', width=99.9):
            with Note(default_x=15.8, default_y=-867.48):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='50', width=95.74):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='51', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='52', width=108.33):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='53', width=145.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=16.16, default_y=-852.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='54', width=118.34):
            with Note(default_x=12.94, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='55', width=140.66):
            with Note(default_x=16.16, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='56', width=125.58):
            with Note(default_x=15.8, default_y=-817.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='57', width=144.78):
            with Note(default_x=16.16, default_y=-817.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='58', width=118.34):
            with Note(default_x=12.94, default_y=-832.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='59', width=208.7):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=88.55, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='60', width=142.63):
            with Note(default_x=15.8, default_y=-1204.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='61', width=140.08):
            with Note(default_x=15.8, default_y=-1169.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='62', width=145.93):
            with Note(default_x=15.8, default_y=-1204.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='63', width=140.08):
            with Note(default_x=15.8, default_y=-1169.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='64', width=116.86):
            with Note(default_x=15.8, default_y=-1204.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='65', width=111.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=111.95):
            with Note(default_x=15.8, default_y=-1169.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.32, default_y=-1169.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=78.84, default_y=-1169.9):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='67', width=192.22):
            with Note(default_x=15.8, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=56.15, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=114.84, default_y=-1184.9):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=124.62):
            with Note(default_x=15.8, default_y=-1204.9):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='69', width=219.47):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.37)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=88.55, default_y=-1175.27):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='70', width=152.57):
            with Note(default_x=15.8, default_y=-1210.27):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='71', width=146.72):
            with Note(default_x=15.8, default_y=-1175.27):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='72', width=123.5):
            with Note(default_x=15.8, default_y=-1210.27):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='73', width=118.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-1190.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-1190.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-1190.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='74', width=118.6):
            with Note(default_x=15.8, default_y=-1175.27):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=49.53, default_y=-1175.27):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=83.27, default_y=-1175.27):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='75', width=198.87):
            with Note(default_x=15.8, default_y=-1190.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.24, default_y=-1190.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=119.97, default_y=-1190.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='76', width=102.2):
            with Note(default_x=15.8, default_y=-1210.27):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='77', width=99.33):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=69.47, default_y=-1190.27):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='78', width=155.17):
            with Note(default_x=15.8, default_y=-1210.27):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=243.64):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=190.88, default_y=-1093.74):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='80', width=153.95):
            with Note(default_x=15.8, default_y=-1113.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='81', width=153.95):
            with Note(default_x=15.8, default_y=-1113.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='82', width=180.17):
            with Note(default_x=15.8, default_y=-1113.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
        with Measure(number='83', width=181.94):
            with Note(default_x=15.8, default_y=-1113.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.51, default_y=-1113.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.21, default_y=-1113.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='84', width=145.18):
            with Note(default_x=15.8, default_y=-1113.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
        with Measure(number='85', width=140.66):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='86', width=113.41):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
        with Measure(number='87', width=122.12):
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')