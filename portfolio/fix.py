import codecs
with codecs.open('index.html', 'r', 'utf-8') as f:
    lines = f.readlines()
s = next(i for i, l in enumerate(lines) if '<style>' in l)
e = next(i for i, l in enumerate(lines) if '</style>' in l)
with codecs.open('style.css', 'w', 'utf-8') as f:
    f.writelines(lines[s+1:e])
with codecs.open('index.html', 'w', 'utf-8') as f:
    f.writelines(lines[:s] + ['<link rel="stylesheet" href="style.css">\n'] + lines[e+1:])
