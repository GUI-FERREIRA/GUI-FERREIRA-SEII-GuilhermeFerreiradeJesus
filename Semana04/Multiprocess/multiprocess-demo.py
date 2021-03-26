#queremos usar multiprocessamento sempre que for para acelerar significativamente nosso programa,
#agora a aceleração vem de diferentes tarefas executadas em paralelo
import concurrent.futures
import time

#inicio marcador do tempo
start = time.perf_counter()


#função responsável pelo delay
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


#responsável por criar uma pilha de executor de processos, para utilizar a função map
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs) #explicado no exercício de threads

    for result in results:
        print(result)

#fim marcador do tempo
finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')