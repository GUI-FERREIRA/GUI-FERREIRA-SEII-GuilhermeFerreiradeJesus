import concurrent.futures
import time
import threading

start = time.perf_counter()

#função resposável por coloar um delay
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

##usando a biblioteca threading
# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])    ##inicia a função do_something com o parametro.
#     t.start() ##inicia a atividade da thread
#     threads.append(t)    ##add o retorno da função na lista threads
#
# for thread in threads:
#     thread.join() #espera cada thread terminar os processos

##usando a biblioteca concurrent
with concurrent.futures.ThreadPoolExecutor() as executor:
    # results = [executor.submit(do_something, 1) for _ in range(10)]  #retorna um objeto futuro que representa a execução do chamado.
    secs = [5, 4, 3, 2, 1]
    ##os iteráveis são coletados imediatamente, ao em vez de pausadamente;
    ##A função é executada de forma assíncrona e várias chamadas para a funcão podem ser feitas simultaneamente.
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')