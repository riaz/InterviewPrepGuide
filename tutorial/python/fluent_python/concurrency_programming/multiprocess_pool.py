# importing library 
import multiprocessing 
  
# define function 
def twos_multiple(y): 
      
    # get current process 
    print(multiprocessing.current_process()) 
      
    return y * 2
  
pro = multiprocessing.Pool() 
  
print(pro.map(twos_multiple, range(10)))