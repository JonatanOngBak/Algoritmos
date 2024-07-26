from find_the_future import nextClosestData

def performQueries(arr, Q):
    for i in range(len(Q)):
        print(nextClosestData(arr, Q[i]))

arr = ["22/4/1233", "1/3/633", "23/5/56645", "4/12/233"]
Q = ["23/3/4345", "4/4/34234234", "12/3/2"]
performQueries(arr, Q)