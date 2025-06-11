# Open Music Sheet

Open Music Sheet is a repoistoy of copyright free open source music sheet for public domain music work.

All the music sheet can be viewed at https://open-music-sheet.streamlit.app/

Its data come from collabrative editing of music sheet in MusicPy language. 
[MusicPy](https://github.com/yufanyufan/musicpy) is losslessly convertable between MusicXML, designed for collaborative editing.

The scores are oranized by `composer/genre/work/piece`, eg: `/chopin/preludes/op28/no15_prelude_in_db_major_raindrop.py`

## Contribution Guide
Some sheet is missing and you like to contribute? Send us a pull request!

The music work must be under [public domain](https://creativecommons.org/publicdomain/mark/1.0/).

If your orignal sheet is in MusicXML format, it can be converted to MusicPy using [xml_to_py.py](https://github.com/yufanyufan/musicpy/blob/main/xml_to_py.py) converter.

No PDF/MIDI is accepted. Other sheet format must be converted into MusicXML first.

For security reason, MusicPy in this repository does not permit to import **any** module or use any function call. Only vallila MusicPy is allowed.

Help are needed in these area:

* Adding new pieces!
* Fix error in metadata (naming, orgnization), or sheet itself.
* Improve sheet page layout and engraving
* Improve annotation: expression， articulation, fingering
