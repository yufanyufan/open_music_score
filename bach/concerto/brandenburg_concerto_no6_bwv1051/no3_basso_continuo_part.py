with ScorePartwise(version='3.1'):
    with Identification():
        Rights('Edited and figured by Mauro Cazzaniga\nFrom the Dover (Bach-Gesellschaft Ausgabe) edition')
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
        CreditWords('Brandenburg Concerto 6', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_family='Augustus', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 1051, mvt. 3', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_family='Constantia', font_size='16')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_family='Dearest Open', font_size='14')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Edited and figured by Mauro Cazzaniga\nFrom the Dover (Bach-Gesellschaft Ausgabe) edition', default_x=595.44, default_y=113.386, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Continuo.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Violoncello')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(7)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=141.91):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(103.6)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('12')
                    BeatType('8')
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegro', default_x=-39.49, default_y=15.4, relative_y=20.0, font_weight='bold', font_family='Constantia', font_size='12')
                Sound(tempo=132.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=264.66):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=74.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=137.53, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=200.3, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='2', width=285.58):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.48, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=142.95, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=183.24, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=208.43, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=233.61, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=258.79, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=281.75):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=80.54, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note(default_x=147.08, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note(default_x=213.61, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='4', width=406.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=85.78, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2614 2')
            with Note(default_x=127.91, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=188.51, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2616')
            with Note(default_x=230.64, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=257.42, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=299.55, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=326.33, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=352.66, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=378.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=221.51):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=14.5, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=64.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7 \ue2605')
            with Note(default_x=115.31, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=165.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='6', width=218.57):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.95, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=62.29, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=112.58, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.52, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=162.86, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='7', width=230.49):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=62.93, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=113.85, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=164.78, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.11, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=348.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Note(default_x=85.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.85, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=148.62, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=184.69, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=211.47, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=234.01, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=256.55, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=279.1, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=301.64, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=324.18, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=109.88):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
        with Measure(number='10', width=0.0):
            with Attributes():
                with MeasureStyle():
                    MultipleRest(3)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='11', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='12', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='13', width=217.77):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=64.93, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=113.9, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=162.87, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='14', width=200.7):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=60.71, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=109.41, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=145.96, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
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
                Type('eighth')
        with Measure(number='15', width=0.0):
            with Attributes():
                with MeasureStyle():
                    MultipleRest(4)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='16', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='17', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='18', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='19', width=280.4):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(583.04)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=85.78, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=132.76, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=179.74, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=226.72, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='20', width=105.55):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
        with Measure(number='21', width=238.73):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=63.03, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
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
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=204.36, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='22', width=253.39):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.52, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=73.29, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=107.81, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=129.39, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=150.96, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.54, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=194.11, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='23', width=199.41):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
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
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=118.49, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=145.27, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='24', width=262.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
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
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=183.83, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=210.6, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='25', width=223.11):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=74.17, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=111.97, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
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
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=188.73, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='26', width=208.14):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=14.5, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
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
            with Note(default_x=91.3, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=118.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='27', width=195.63):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=56.01, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=100.02, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=144.02, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='28', width=188.42):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
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
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=110.05, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=136.83, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='29', width=267.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
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
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=188.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=214.85, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='30', width=213.86):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=60.14, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=114.57, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=160.7, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='31', width=203.48):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=14.5, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=59.92, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=105.34, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.76, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='32', width=0.0):
            with Attributes():
                with MeasureStyle():
                    MultipleRest(2)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='33', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='34', width=203.62):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=14.5, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=59.96, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=105.42, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=150.88, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='35', width=100.19):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
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
        with Measure(number='36', width=298.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Note(default_x=85.78, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=137.72, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=189.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=241.62, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='37', width=82.51):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='38', width=224.43):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=63.91, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=115.81, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=167.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='39', width=245.34):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=67.34, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=122.67, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=156.73, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=178.01, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=199.29, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=220.58, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='40', width=226.86):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=66.03, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=118.05, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=170.08, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='41', width=406.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=85.78, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2614 2')
            with Note(default_x=127.91, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=188.51, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2616')
            with Note(default_x=230.64, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=257.42, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=299.55, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=326.33, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=352.66, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=378.99, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='42', width=221.51):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=14.5, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=64.91, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7 \ue2605')
            with Note(default_x=115.31, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=165.72, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='43', width=218.57):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=42.95, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=62.29, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=93.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=112.58, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=143.52, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=162.86, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=193.81, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='44', width=230.49):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=62.93, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=113.85, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=164.78, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=196.11, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='45', width=322.72):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(72.12)
            with Note(default_x=85.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.05, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=142.83, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=173.1, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=199.87, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=218.79, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=239.76, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note(default_x=258.68, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='46', width=265.08):
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=53.6, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='idem...')
            with Note(default_x=91.4, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.44, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=148.34, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=205.27, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=240.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='47', width=218.47):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.43, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=65.23, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=114.65, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=144.28, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=164.08, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='48', width=0.0):
            with Attributes():
                with MeasureStyle():
                    MultipleRest(4)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='49', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='50', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='51', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='52', width=191.6):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='2')
            with Note(default_x=55.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=98.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=141.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='53', width=278.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Note(default_x=85.78, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue262')
            with Note(default_x=132.11, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7')
            with Note(default_x=178.45, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 5')
            with Note(default_x=206.96, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=224.78, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='54', width=174.88):
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
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2615 \ue262')
            with Note(default_x=97.89, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.66, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='55', width=174.88):
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
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=97.89, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.66, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='56', width=225.4):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=95.14, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=123.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
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
            with Note(default_x=200.63, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='57', width=224.28):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
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
            with Note(default_x=96.35, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 \ue261')
            with Note(default_x=127.75, default_y=-25.0):
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
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='58', width=365.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Note(default_x=85.78, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2615 \ue262')
            with Note(default_x=155.32, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note(default_x=224.86, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2615 \ue262')
            with Note(default_x=294.4, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='59', width=272.69):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='7 \ue2615 \ue262')
            with Note(default_x=76.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=141.54, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2615 \ue262')
            with Note(default_x=206.32, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='60', width=0.0):
            with Attributes():
                with MeasureStyle():
                    MultipleRest(4)
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='61', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='62', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='63', width=0.0):
            with Note():
                Rest(measure='yes')
                Duration(12.0)
                Voice('1')
        with Measure(number='64', width=274.26):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=77.17, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=142.33, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 4')
            with Note(default_x=207.5, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=247.6, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='65', width=1077.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(72.12)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue261')
            with Note(default_x=85.78, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=231.63, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2615 \ue262')
            with Note(default_x=322.79, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6 \ue261')
            with Note(default_x=468.65, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=559.8, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='6')
            with Note(default_x=650.96, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='\ue2615 \ue262')
            with Note(default_x=742.12, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Harmony(print_frame='no'):
                with Root():
                    RootStep('C', text='')
                Kind('none', text='')
            with Note(default_x=833.28, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.S. al Fine', relative_x=181.13, relative_y=37.25)
                Sound(dalsegno='segno')
            with Barline(location='right'):
                BarStyle('light-light')