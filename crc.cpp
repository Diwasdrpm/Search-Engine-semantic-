 #include<stdio.h>
 #include<conio.h>
 #include<string.h>
 int main()
 {
 int i,j,x,y;
 char input[20],key[20],temp[20],quot[20],rem[20],key1[20];
 printf("Enter Data : ");
 gets(input);
 printf("Enter Key : ");
 gets(key);
 x=strlen(key);
 y=strlen(input);
 strcpy(key1,key);
 for(i=0;i<x-1;i++)
 {
 input[y+i]='0';
 }
 for(i=0;i<x;i++)
 temp[i]=input[i];
 for(i=0;i<y;i++)
 {
 quot[i]=temp[0];
 if(quot[i]=='0')
 for(j=0;j<x;j++)
 key[j]='0';
 else
 for(j=0;j<x;j++)
 key[j]=key1[j];
 for(j=x-1;j>0;j--)
 {
 if(temp[j]==key[j])
 rem[j-1]='0';
 else
 rem[j-1]='1';
 }
 rem[x-1]=input[i+x];
 strcpy(temp,rem);
 }
 strcpy(rem,temp);
 printf("\nQuotient is: ");
 for(i=0;i<y;i++)
 printf("%c",quot[i]);
 printf("\nRemainder is: ");
 for(i=0;i<x-1;i++)
 printf("%c",rem[i]);
 printf("\nFinal data is: ");
 for(i=0;i<y;i++)
 printf("%c",input[i]);
 for(i=0;i<x-1;i++)
 printf("%c",rem[i]);
 getch();
 }

