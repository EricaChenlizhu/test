import time
import os

print('Chen lizhu')
local='C:\\Users\\Administrator\\Desktop\\mail'
while True:
    file=open('%s\\log.txt'%local,'a')
    file.write(time.strftime('%y-%m-%d,%H:%M:%S',time.localtime())+'\n')
    file.close()

    os.system('%s\\NewCareerDream.py'%local)
    os.system('%s\\NewJournaEconomicPerspectives.py'%local)
    os.system('%s\\NewTianchi.py'%local)
    os.system('%s\\NewYuqing.py'%local)

    file=open('%s\\log.txt'%local,'a')
    file.write('sleeping...\n\n')
    file.close()

    time.sleep(1800)