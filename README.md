# `olefile` for ImageJ / Jython :coffee: :snake: :microscope:

[![Travis CI](https://travis-ci.com/imcf/jython-olefile.svg?branch=master)](https://travis-ci.com/imcf/jython-olefile)

A mavenized package of [Philippe Lagadec][gh_decalage2]'s
[`olefile`][gh_olefile] Python module to be used in [ImageJ][imagej].

## Example Usage

The code snippet below demonstrates how to read an Olympus `.oib` image file
using `olefile` and print some of the contained metadata.

```python
import olefile
import codecs

ole = olefile.OleFileIO('/data/fluoview/oib/Slide1sec001/Slide1sec001_01.oib')

stream = ole.openstream(['OibInfo.txt'])
conv = codecs.decode(stream.read(), 'utf16')
print conv

stream = ole.openstream(['Storage00001', 'Stream00060'])
conv = codecs.decode(stream.read(), 'utf16')
print conv
```

## Packaging

The `pom.xml` is based on the [imagej-jython-package][gh_ij_jy] repository from
[Michael Entrup][gh_m-entrup] with adaptations to make it work with the original
structure of the upstream `olefile` package.


[gh_decalage2]: https://github.com/decalage2
[gh_olefile]: https://github.com/decalage2/olefile
[imagej]: https://imagej.net
[gh_m-entrup]: https://github.com/m-entrup
[gh_ij_jy]: https://github.com/m-entrup/imagej-jython-package
