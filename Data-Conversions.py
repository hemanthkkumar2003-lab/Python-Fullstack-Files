Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
int(8)
8
int(7.9)
7
int('string')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int('string')
ValueError: invalid literal for int() with base 10: 'string'

int(4+99j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(4+99j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

int(True)
1



float(8)
8.0
float(8.889)
8.889
float('float')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float('float')
ValueError: could not convert string to float: 'float'
float(94+33j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(94+33j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(False)
0.0
>>> 
>>> 
>>> 
>>> str(1)
'1'
>>> str(12345.5678)
'12345.5678'
>>> str('string')
'string'
>>> str(543+234j)
'(543+234j)'
>>> str(False)
'False'
>>> str(True)
'True'
>>> 
>>> 
>>> 
>>> complex(11)
(11+0j)
>>> complex(121.321)
(121.321+0j)
>>> complex('complex')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex('complex')
ValueError: complex() arg is a malformed string
>>> complex(79j+998)
(998+79j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> 
>>> 
>>> bool(109)
True
>>> bool(99.99)
True
>>> bool('boolean')
True
>>> bool(765j)
True
>>> bool(True)
True
>>> bool(False)
False
