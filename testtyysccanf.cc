#include <string.h>
#include<stdlib.h>
#include<stdio.h>





void _testyysscanf(char *filename, const char *me)

{


    int  alpha, sd,   droneId ; 


    sscanf(me, "[ alpha :%d ]  {sd>> :%d }  [ droneId : { %d }  -- %d]" ,  &alpha , &sd ,  &droneId , &sd );


    printf("%d %d %d " ,  alpha , sd , droneId);

     printf("%s" , filename);
    
}

int main(int argc  , const char *argv[])
{
   
    _testyysscanf("testy.txt"  , "[ alpha :18 ]  {sd>> :25 }  [ droneId : { 147 }  -- 200]") ;

 

    return EXIT_SUCCESS;
}