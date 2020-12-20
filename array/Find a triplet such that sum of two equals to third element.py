def findTriplet(arr, n): 
      
    # sort the array 
    arr.sort() 
   
    # for every element in arr 
    # check if a pair exist(in array) whose 
    # sum is equal to arr element 
    i = n - 1
    while(i >= 0): 
        j = 0
        k = i - 1
        while (j < k): 
            if (arr[i] == arr[j] + arr[k]): 
                 
                # pair found 
                print "numbers are ", arr[i], arr[j], arr[k] 
                return
            elif (arr[i] > arr[j] + arr[k]): 
                j += 1
            else: 
                k -= 1
        i -= 1
          
    # no such triplet is found in array 
    print "No such triplet exists"
