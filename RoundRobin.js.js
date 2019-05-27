//Varios erros ainda para corrigir...

// Conversão de código Python3 para Javascript(Node)

function findWaitingTime( processes, n, bt, wt, quantum) {
    var rem_bt = [0] * n

    for(var i of Range(n)){
        rem_bt = [i] = bt[i]
    }

    var t = 0

    while(1){
        var done = true

        for(i of Range(n)) {
            if(rem_bt[i] > 0) {
                done = false

                if(rem_bt[i] > quantum) {
                    t = t + quantum

                    rem_bt[i] = rem_bt[i] - quantum
                } else {
                    t = t + rem_bt[i]

                    wt[i] = t - bt[i]

                    rem_bt[i] = 0
                }
            }
            if(done === true) {
                break
            }
        }
    }
}

function findTurnAroundTime(processes, n, bt, wt, tat) {
    for(var i of Range(n)) {
        tat[i] = bt[i] + wt[i]
    }
}

function findavgTime(processes, n, bt, quantum) {
    var wt = [0] * n
    var tat = [0] * n

    function indWaitingTime (processes, n, bt, wt, quantum) {

    }

    function findTurnAroundTime(processes, n, bt, wt, tat) {

    }
    
    console.log("Processes Burst Time Waiting," + "Time Turn-Around Time")

    var total_wt = 0
    var total_tat = 0

    for(var i of Range(n)) {
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        console.log(" " + i + 1 + " " +  bt[i] +
            " " +  wt[i] + " " + tat[i])  
    }

    console.log("Average waiting time = %.5f " % (total_wt / n))
    console.log("Average turn around time = %.5f " % (total_tat / n))
}


// Pendecia, converter para javascript
/*if(__name=="__main__"){
    var proc = [1, 2, 3]
    var n = 3

   
    var burst_time = [10, 5, 8]

   
    var quantum = 2;
    function findavgTime(proc, n, burst_time, quantum){

    }
}*/



