def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              import  numpy as np
              a=np.array(a)
              b=np.array(b)
              if len(a[0])!=len(b):
                return -1  
              c=np.dot(a, b)
              return c


