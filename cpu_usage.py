import psutil
CPU = psutil.cpu_count()
print(CPU)
while True:
    Cpu_Precent=psutil.cpu_percent(1)
    print(Cpu_Precent)
