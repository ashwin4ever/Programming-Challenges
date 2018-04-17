//Check if a string is a permutation of another string


   #include<stdio.h>
   #include<stdlib.h>
   #include<ctype.h>
   #include<string.h>

   #define LEN 127

   void is_permute(char s1[] , char s2[] , int l);

   int main(){


      char s1[] = "abc";

      char s2[] = "cbcabdabcdabcbca";

      int src_len = sizeof(s1) / sizeof(s1[0]);

      printf("String 1: %s , String 2 : %s" , s1 , s2);

      int i , j ;
      j  = 0;

      for(i = 0; i < sizeof(s2) / sizeof(s2[0]); i++){

         char temp[src_len + 1];
         //memcpy(temp , &s2[i + 2] ,

         temp[j] = s2[i];
         printf("\n%c" , temp[j]);

         if((i + 1) % 3 == 0){
            temp[j] = '\0';
            printf("\n%s" , temp);
            is_permute(s1 , temp, src_len);
            j = 0;
         }
         j++;
      }//end of for


      return 0;
   }//end of main

   void is_permute(char s1[] , char s2[] , int l){

      printf("\ns1: %s , s2: %s" , s1 , s2);

      int letters[LEN + 1] = {0};

      int i , j;

      for(i = 0; i < l; i++){

         int val = s1[i];

         letters[val]++;

      }//end of for i



      for(j = 0; j < l; j++){


         int val = s2[j];

         if(letters[val])
            letters[val]--;

         if(letters[val] < 0){
            printf("\nNot a permutation");
            break;
         }

      }//end of for j


      printf("\nIs permutation");


   }//end of is permute


