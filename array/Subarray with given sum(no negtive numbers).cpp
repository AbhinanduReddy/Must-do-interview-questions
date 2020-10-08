#include<bits/stdc++.h> 
using namespace std; 

int main() 

 {    
   #ifndef ONLINE_JUDGE 
   freopen("input.txt", "r", stdin);  
   freopen("output.txt", "w", stdout); 
   #endif 

   int n,sum;
   cin>>n>>sum;
   vector<int> v(n,0);
   for(auto &x:v)
   {
      cin>>x;
   }   
      int j=0;
       int s=v[0];
     for(int i=1;i<v.size();i++)
     {  cout<<s<<endl;
         while(s>sum) && j<i-1)

         {
            s=s-v[j];
            j++;
         }
         if(s==sum)
            {cout<<"Subarray at "<<j<<" to "<<i-1;
               return 0;}

          if(s<sum)
          {
            s=s+v[i];
            
          }     
     }

cout<<"not found";
}
