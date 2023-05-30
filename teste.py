import schedule
import time

def Tarefa():
    print('Rodando tarefa')

schedule.every(10).seconds.do(Tarefa)

while 1:
    schedule.run_pending()
    time.sleep(1)