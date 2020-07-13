import re 

p = re.compile(r'\[[^\s]+\)', re.IGNORECASE)
s = 'CSS is a language that can be used to add style to an [HTML](/wiki/HTML) page.'
m = p.search(s)
s1 = m.group()
print(s1)
p1 = re.compile(r'\[[^\s]+\]')
m1 = p1.search(s1)
print(m1.group())
m2 = re.search(r'\([^\s]+\)', s1)
print(m2.group())