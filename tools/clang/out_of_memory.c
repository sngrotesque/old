#include<stdio.h>

int main(void)
{
  //out of memory - Vulnerability improvement
  //内存溢出 - 漏洞修复
  int j;
  char i[5];
  
  printf("Please enter: ");
  scanf("%5c",i);   //这里需为字符型，不然会再次导致内存溢出
  
  for(j=0;j<5;j++)
  {
    printf("%c",i[j]);
  }
  
  return 0;
}
