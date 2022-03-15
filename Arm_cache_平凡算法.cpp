#include<iostream>
#include <sys/time.h>
#include<time.h>
#include<stdlib.h>
using  namespace std;


int main(){
  for(int k=1;k<=100;k=k+10){
  struct timeval start;
  struct timeval end;

  const int N=k;
  double b[N][N],a[N],sum[N]={0};
  for(int i=0;i<N;i++){
      for(int j=0;j<N;j++){
         b[i][j]=i+j;
    }
    a[i]=i;
    }

  gettimeofday(&start,NULL);
  for(int test=0;test<100;test++){
    for(int i=0;i<N;i++){
      for(int j=0;j<N;j++){
            
        sum[i]=sum[i]+a[j]*b[j][i];
       }
  }
  }
  gettimeofday(&end,NULL);
  cout<<((long long)end.tv_sec-(long long)start.tv_sec)*1000000+((long long)end.tv_usec-(long long)start.tv_usec)<<endl;

}

}