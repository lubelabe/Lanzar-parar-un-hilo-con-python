# import subprocess
# import time
# import psutil

# pids = list()
# process = list()

# for i in range(3):
#     pro = subprocess.Popen('PruebaOne.DetectionFace', shell=True, stderr=subprocess.STDOUT)
#     pid = pro.pid
#     process.append(pro)
#     pids.append(pid)

# time.sleep(15)

# process[1] = psutil.Process(pids[1])
# for proc in process[1].children(recursive=True):
#     proc.kill()
# process[1].kill()

#Arriba no funcional, abajo funcional

from multiprocessing import Process
import PruebaOne, time, psutil

pids = list()

def startProcess():
    for i in range(3):
        p = Process(target=PruebaOne.DetectionFace)
        p.start()
        pids.append(p.pid)

def KillProcess(posProcess):
    p = psutil.Process(posProcess)
    for proc in p.children(recursive=True):
        proc.kill()
    p.kill()

if __name__ == '__main__':
    startProcess()
    time.sleep(10)
    KillProcess(pids[1])