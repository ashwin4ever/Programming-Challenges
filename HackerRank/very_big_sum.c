//Very Big Sum


   #include<stdio.h>
   #include<ctype.h>
   #include<stdlib.h>
   #include<limits.h>

   int main(){


      int n;


      scanf("%d" , &n);

      unsigned long long int arr[n];
      int i;

      long long int sum = 0;

      for(i = 0; i < n; i++)
         scanf("%llu" , &arr[i]);


      for(i = 0; i < n; i++)
         sum += arr[i];

      printf("\n%lld" , sum);


      return 0;
   }//end of main
