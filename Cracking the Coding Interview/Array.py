#Implements array


import ctypes

class Array:

      def __init__(self , size):

            assert size > 0 , "Array size must be greater than 0"

            self.size = size

            #create the array
            ArrayType = ctypes.py_object * size
            self.elements = ArrayType()

            #init arra to zero or none
            self.clear(None)

      def __len__(self):
            return self.size

      def __getitem__(self , index):
            assert index >= 0 and index < len(self) , "Index less or great"
            return self.elements[index]

      def __setitem__(self , index , value):
            assert index >= 0 and index < len(self) , "Index less or great"
            self.elements[index] = value


      #clear array by setting element to value
      def clear(self , value):
            for i in range(len(self)):
                  self.elements[i] = value
            
