#include<iostream>
#include<windows.h>
using namespace std;

int main(){

   for(int k=2;k<=2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2;k=k*2){
   long long head, tail , freq ;
   QueryPerformanceFrequency((LARGE_INTEGER *)&freq );
   const int n=k;

   QueryPerformanceCounter((LARGE_INTEGER *)&head);
   for(int test=0;test<1000;test++)
   {
      int a[n];
      int i;
      int sum=0;
   for(i=0;i<n;i++)
	   a[i]=i;
   for (i = 0; i < n; i++)
       sum += a[i];
   }
   QueryPerformanceCounter((LARGE_INTEGER *)&tail );
   cout<<"Time: "<<(tail - head)*1000.0/freq<<"ms"<<endl;
    }
return 0;
}