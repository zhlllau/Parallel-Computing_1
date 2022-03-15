#include<iostream>
#include <sys/time.h>
#include<time.h>
using namespace std;


int main(){

   for(int k=2;k<=2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2;k=k*2){

   const int n=k;


    struct timeval start;
    struct timeval end;
    gettimeofday(&start,NULL);

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

    gettimeofday(&end,NULL);
    cout<<((long long)end.tv_sec-(long long)start.tv_sec)*1000000+((long long)end.tv_usec-(long long)start.tv_usec)<<endl;//微秒

}
return 0;
}