//Is Unique: Implement an algorithm to determine
//if a string has all unique characters. What if you
//cannot use additional data structures?
// s1 = 'aabcd'
// s2 = 'abcd'


   #include<Stdio.h>
   #include<stdlib.h>
   #include<ctype.h>

   #define LEN 128


   void isUnique(char s[] , int len);

   int main(){


      char str[LEN + 1];

      printf("\nEnter a string: ");
      scanf("%s" , str);

      isUnique(str , LEN + 1);

      return 0;

   }//end of main

   void isUnique(char s[] , int l){

      int i , j;

      int isSeen[LEN] = {0};

      if(sizeof(s) / sizeof(s[0]) > l){
         printf("\nInvalid");

      }
      else{

         for(i = 0; s[i] != '\0'; i++){

            int ch = s[i];
            printf("\n%d" , ch);
            if(isSeen[ch]){
               printf("\nNot Unique");
               break;
            }

            isSeen[ch] = 1;

         }//end of for i

      }//end of else


   }//end of isUnique
