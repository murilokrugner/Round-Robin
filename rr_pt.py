# Programa Python3 para implementação de
# Agendamento de RR
# Função para encontrar o tempo de espera
# para todos os processos  

def findWaitingTime(processes, n, bt,  
                         wt, quantum):  
    rem_bt = [0] * n 
  
    # Copie o tempo de rajada para rt  
    for i in range(n):  
        rem_bt[i] = bt[i] 
    t = 0 # Hora atual 
  
    # Manter processos de travessia na rodada
    # modo robin até que todos estejam
    # não realizado
    while(1): 
        done = True
  
        # Atravessar todos os processos, um por
        # um repetidamente  
        for i in range(n): 
              
            # Se o tempo de burst de um processo for maior
            # than 0 então só precisa processar mais  
            if (rem_bt[i] > 0) : 
                done = False # Há um processo pendente
                  
                if (rem_bt[i] > quantum) : 
                  
                   # Aumentar o valor de t, ou seja, mostra
                   # quanto tempo um processo foi processado
                    t += quantum  
  
                    # Diminuir o melhor tempo do processo atual 
                    # pelo quantum  
                    rem_bt[i] -= quantum  
                  
                # Se o tempo de burst for menor ou igual a
                # para quantum. Último ciclo para este processo  
                else: 
                  
                    # Aumentar o valor de t, ou seja, mostra
                    # quanto tempo um processo foi processado  
                    t = t + rem_bt[i]  
  
                    # O tempo de espera é o tempo atual menos
                    # tempo usado por este processo  
                    wt[i] = t - bt[i]  
  
                   # À medida que o processo é totalmente executado
                   # faça seu tempo de burst restante   
                    rem_bt[i] = 0
                  
        # Se todos os processos forem feitos  
        if (done == True): 
            break
              
# Função para calcular o tempo de retorno  
def findTurnAroundTime(processes, n, bt, wt, tat): 
      
    # Calcular o tempo de retorno  
    for i in range(n): 
        tat[i] = bt[i] + wt[i]  
  
  
#Função para calcular a espera média
# e tempos de resposta. 
def findavgTime(processes, n, bt, quantum):  
    wt = [0] * n 
    tat = [0] * n  
  
    # Função para encontrar o tempo de espera
    # de todos os processos  
    findWaitingTime(processes, n, bt,  
                         wt, quantum)  
  
    # Função para encontrar o tempo de volta
    # para todos os processos 
    findTurnAroundTime(processes, n, bt, 
                                wt, tat)  
  
    # Exibir processos junto com todos os detalhes  
    print("Processes    Burst Time     Waiting",  
                     "Time    Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", i + 1, "\t\t", bt[i],  
              "\t\t", wt[i], "\t\t", tat[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
    print("Average turn around time = %.5f "% (total_tat / n))  
      
# Driver code  
if __name__ =="__main__": 
      
    # Process id's  
    proc = [1, 2, 3] 
    n = 3
  
    #Tempo de ruptura de todos os processos 
    burst_time = [10, 5, 8]  
  
    # Time quantum  
    quantum = 2;  
    findavgTime(proc, n, burst_time, quantum) 
  
# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 