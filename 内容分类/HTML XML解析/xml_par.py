# xml_par.py
import xml.etree.ElementTree as et
tree = et.parse("./root.xml")
r = tree.getroot()
print(r.tag)
for i in r:
    print(i.tag)
    for j in i:
        print(i.tag)
