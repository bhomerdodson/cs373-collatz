#include <stdlib.h>
#include <time.h>
#include <stdio.h>


int main () {
   using namespace std;
   srand ( time (NULL) );
   for(int a = 0; a < 1000; a++) {
      int i = rand() % 1000000 + 1;
      int j = 0;
      bool change = false;
      if(i == 999999) {
         j = rand() % 1000000 + 1;
         change = true;
      }
      else {
         while(j < i) {
            j = rand() % 1000000 + 1;
         }
      }

      if(change) {
         cout << j << " " << i << endl;
      }
      else
         cout << i << " " << j << endl;
   }
   
}
