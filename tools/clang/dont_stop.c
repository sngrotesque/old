#include<stdio.h>
#include<unistd.h>

int main(void)
{
  //Don't Stop
  int i=0,j=1;
  
  while(i<5)
  {
	  printf("%d.%d \t %d \t %d\n",j,i,i+i,i+i+i);
	  sleep(1);
	  i=i-1;
	  j=j+1;
  }
  
  return 0;
}
