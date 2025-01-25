import os
import logging
from os import close
import sys
import json
import time


from subprocess import call
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
variable = os.environ.get('GROUP_NUMBER')      
print("Valor de GROUP_NUMBER:", variable)

fin = open("/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/index.html", 'r') 

fout = open("/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/index2.html", 'w')

for line in fin:
  if "{% block title %}Simple Bookstore App{% endblock %}" in line :
   fout.write("{% block title %}"+"Simple Bookstore App {}".format(variable) + "{% endblock %}")
  else:
   fout.write(line)
fin.close()
fout.close()


call(["cp","/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/index2.html","/home/practica_creativa2/bookinfo/src/productpage/templates/index.html"])
call(["rm","/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/index2.html"])


fin = open("/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r') 

fout = open("/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html", 'w') 

for line in fin:
  if "{% block title %}Simple Bookstore App{% endblock %}" in line :
   fout.write("{% block title %}"+"Simple Bookstore App {}".format(variable) + "{% endblock %}")
  else:
   fout.write(line)
fin.close()
fout.close()


call(["cp","/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html","/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/productpage.html"])
call(["rm","/home/parte1/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html"])


os.system('sudo apt-get update')
os.system('sudo apt-get install  python3-pip')
os.system('pip3 install -r /home/parte1/practica_creativa2/bookinfo/src/productpage/requirements.txt')
os.system(' python3 /home/parte1/practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 8080')


















