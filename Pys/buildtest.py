import random
import sys
from subprocess import Popen, PIPE, STDOUT, TimeoutExpired

def execute(cmd):
    with Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT) as process:
        try:
            stdout, stderr = process.communicate(timeout=60)
        except TimeoutExpired:
            process.kill()

word=random.randint(64,200)
txt = open("test.txt", "w")
txt.write(str(word))
txt.close()

execute("python3 rsa.py -g")
execute("python3 rsa.py -e -f test.txt -k keypair.txt")
execute("rm test.txt")
execute("python3 rsa.py -d -f test.txt.enc -k keypair.txt")

txt = open("test.txt", "r")
res=txt.readline().strip()
txt.close()
execute("rm *.enc")
execute("rm *.txt")

if word==int(res):
    sys.exit(0)
else:
    sys.exit(1)
