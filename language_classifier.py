'Goal:  Build a language recognizer using a naive bayesian classifier'

# Make a 50 language reconizer trained on 10 books per language at:
# http://www.gutenberg.org/browse/languages/en
# http://www.gutenberg.org/files/1342/1342-0.txt

from reverend.thomas import Bayes

# Train the classifier
language_sniffer = Bayes()
for lang in ['en', 'es', 'fr', 'de', 'it']:
    filename = 'notes/proverbs_%s.txt' % lang
    with open(filename) as f:
        data = f.read().decode('utf-8')
        language_sniffer.train(lang, data)
    
# Apply the classifier
phrases = u'''\
All the leaves are brown and the sky is gray.  I've been for a walk on a winter's day.
De colores, todos los colores. De colores se visten los campos en la primavera.
Jingle bells, jingle all the way. Oh what fun it is to ride in a one horse open sleigh.
Casca belles, hoy es navidad.  Es un dia, de allegria y felicidad.
'''.splitlines()

for phrase in phrases:
    best_guess = language_sniffer.guess(phrase)[0][0]
    print best_guess, '<--', phrase[:30]


