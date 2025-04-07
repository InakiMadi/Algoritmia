# Exercise

Suppose we have two files with relative information to numeric ranges of values:

### FileX
000|030|X-A|

040|045|X-B|

046|060|X-C|

065|090|X-D|

### FileY
010|015|Y-A|

025|050|Y-B|

070|095|Y-C|

We wish to generate one unique file with the information of both files:

### FileMix

r1_start|r1_end|X1|Y1|

r2_start|r2_end||Y2|

r3_start|r3_end|X2||

...

Ranges must not overlap. First column is data from FileX, and second column is data from FileY. Some positions of a data column might be empty, but not both.