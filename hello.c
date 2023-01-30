#include <stdio.h>
              
               int main() {
              
                 int a = 2;
                 int b = 2;
                 int c = a + b;
              	 
		 char listOfUsers[3][10] = {"User1", "User2", 
		 "User3"};

		 
                 printf("C says: Hello, World!\n");
                 printf("%d + %d = %d\n",a,b,c);
                 for(int i = 0; i < 3; i++){
			printf("%s\n", listOfUsers[i]);
		}
                 return 0;
               }
