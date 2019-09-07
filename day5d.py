Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
en
es
fr
de
it
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
notes/proverbs_en.txt
notes/proverbs_es.txt
notes/proverbs_fr.txt
notes/proverbs_de.txt
notes/proverbs_it.txt
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
Eat, drink and be merry (for tomorrow we die).
Beggars can't be choosers.For a good appetite there is no hard bread.
Everyone gets his comeuppance in the end / just deserts sooner or later.
An apple a
A beber y a tragar, que el mundo se va a acabar.
A buen(a) hambre, no hay mal pan / pan duro, (ni falta salsa a ninguno)
      /no hace falta condimento.A mucha hambre, no hay pan duro.Al hambre de si
A qui la tête fait mal, souffre par tout le corps.
A tout pourquoi il y a (un) parce que.
A vrai dire peu de paroles.
Abondance de bien ne nuit pas.
Aide-toi et le ciel t'aidera.
Amour, toux et fumée 
Allein ist besser als mit Schlechten im Verein: mit Guten im Verein, ist besser als allein.
Aller guten Dinge sind drei.
Alles ist seinen Preis wert.
Alles zu seiner Zeit.
Alte Füchse gehen schwer in 
A cane scottato l 'acqua fredda pare calda.
A carne di lupo, zanne di cane.
A caval donato non si guarda in bocca.
A chi Dio vuol castigare leva il cervello.
A chi bene crede, Dio provvede.
A chi dai 
>>> type(data)
<type 'unicode'>
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/language_classifier.py", line 15, in <module>
    langauge_sniffer.train(lang, data)
NameError: name 'langauge_sniffer' is not defined
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
[('en', 0.6678411430723072), ('es', 0.09625592015932655), ('fr', 0.048827768936825056), ('it', 0.021533584560437025), ('de', 0.0068154980643711505)]
[('es', 0.668533869546023), ('fr', 0.1153337120432994), ('it', 0.05309888877311503)]
[('en', 0.7470716357451941), ('es', 0.08837703097403582), ('it', 0.05961247678270798), ('fr', 0.051457046907160686), ('de', 0.018139927955545643)]
[('es', 0.5394812937312652), ('it', 0.12791684628625483), ('fr', 0.1023693357791769), ('de', 0.09476310919401221)]
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
('en', 0.6678411430723072)
('es', 0.668533869546023)
('en', 0.7470716357451941)
('es', 0.5394812937312652)
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
en
es
en
es
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/army2/language_classifier.py ====
en <-- All the leaves are brown and t
es <-- De colores, todos los colores.
en <-- Jingle bells, jingle all the w
es <-- Casca belles, hoy es navidad. 
>>> 
>>> import cbitarray
>>> b = cbitarray.BitArray(20)
>>> b
BitArray('00000000000000000000')
>>> b[20] = 1

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b[20] = 1
  File "cbitarray.pyx", line 56, in cbitarray.BitArray.__setitem__
    index = self._check_and_adjust_index(index)
  File "cbitarray.pyx", line 39, in cbitarray.BitArray._check_and_adjust_index
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> b[17] = 1
>>> help(cbitarray)
Help on module cbitarray:

NAME
    cbitarray - Build a bitarray with an API similar to bytearray

FILE
    /Users/raymond/Dropbox/Public/army2/sandbox2/lib/python2.7/site-packages/cbitarray.so

DESCRIPTION
    List of techniques:
        - Pick out the n-th bit:           (x >> n) & 1
        - Set the n-th bit:                (1 << n) | x
        - Reset (unset) the n-th bit:      ~(1 << n) & x
        - Ceiling division:                -(n // -d)
        - Floor division and modulo:       divmod(n, d)
    
    Model of bitarray built on a bytearray
    
         0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23      <= i or index
         ------------------------------|-------------------------------|------------------------------
         0   0   0   0   0   0   0   0 | 1   1   1   1   1   1   1   1 | 2   2   2   2   2   2   2   2      <== i // 8
         0   1   2   3   4   5   6   7 | 0   1   2   3   4   5   6   7 | 0   1   2   3   4   5   6   7      <== i % 8

CLASSES
    BitArray
    
    class BitArray
     |  An array of bits models after the bytearray
     |  
     |  Methods defined here:
     |  
     |  __getitem__(...)
     |  
     |  __init__(...)
     |  
     |  __len__(...)
     |  
     |  __repr__(...)
     |  
     |  __setitem__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __qualname__ = 'BitArray'

FUNCTIONS
    ceiling_division(...)
        Return *n* divided by *d* but rounded up if there is a remainder
        
        To provision 16 eggs in cartons that hold 12 eggs,
        you need two cartons:
        
            >>> ceiling_division(16, 12)
            2

DATA
    __test__ = {u'ceiling_division (line 19)': u'Return *n* divided by *d*...


>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/bloomfilter.py ========
False
True
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
TestResults(failed=0, attempted=3)
0.0465240478516
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
0.617037057877
>>> 
