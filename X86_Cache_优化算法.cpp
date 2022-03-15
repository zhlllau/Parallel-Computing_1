#include<iostream>
#include<windows.h>
#include<stdlib.h>
using  namespace std;


const int N=10000;
double b[N][N],a[N],sum[N]={0};
void Init(int N){
    for(int i=0;i<N;i++){
      for(int j=0;j<N;j++){
         b[i][j]=i+j;
    }
    a[i]=i;
    }
 }



int main(){
  long long head, tail , freq ;
  Init(N);
  QueryPerformanceFrequency((LARGE_INTEGER *)&freq );
  QueryPerformanceCounter((LARGE_INTEGER *)&head);// timers

  for(int test=0;test<1;test++){
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            sum[j]=sum[j]+a[i]*b[i][j];
          }
      }
  }

  QueryPerformanceCounter((LARGE_INTEGER *)&tail );
  cout<<"Time: "<<(tail - head)*1000.0/freq<<"ms"<<endl;

}