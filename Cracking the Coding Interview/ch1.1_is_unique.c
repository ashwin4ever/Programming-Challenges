//Is Unique: Implement an algorithm to determine
//if a string has all unique characters. What if you
//cannot use additional data structures?
// s1 = 'aabcd'
// s2 = 'abcd'

   #include<stdio.h>
   #include<stdlib.h>
   #include<ctype.h>


   void isUnique(char s[] , int l);

   int main(){



      char s[] = "abcd";
      //printf("%d" , s[0]);

      printf("Original char: %s\n" , s);

      isUnique(s , sizeof(s) / sizeof(s[0]));


      return 0;
   }//end of main

   void isUnique(char s[] , int l){

      int i , j;
      int flag = 0;

      //O(n^2)
      for(i = 0; i < l; i++){

         for(j = i + 1; j < l; j++){

            if(s[i] == s[j]){
               flag = 1;
               break;
            }



         }//end of for j

      }//end of for i

      if(flag)
         printf("\nNot unique");
      else
         printf("\nUnique");


   }//end of is unique



