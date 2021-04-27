//ANS5 - Submitted by Tatwamasi Mishra, UCSE20040

//this program implements graph traversal by the method of DFS

#include <stdio.h>


int  M[10][10];
int visited[10], n;

/*function to traverse depth first through the graph*/
void DFS(int i)
{
    int j;
	printf("%d\t",i+1);
    visited[i]=1;
	
	for(j=0;j<n;j++)
       if( !visited[j] && M[i][j]==1 )
            DFS(j);
}

int main() {
	
	int i, j;
	
	printf("HELPFUL GUIDE: An example adjacency matrix:\n");
	printf("{0, 1, 1, 1, 0}\n");
	printf("{1, 0, 0, 0, 1}\n");
	printf("{1, 0, 0, 0, 1}\n");
	printf("{1, 0, 0, 0, 1}\n");
	printf("{0, 1, 1, 1, 0}\n");
	
	/*graph used in the example:
				1
			   /|\
			  / | \
			 /  |  \
			 2  3  4
			 \  |  /
			  \ | /
			   \|/
			    5
	*/
	
	printf("\nEnter number of vertices (if you wish to refer to given example, enter 5): ");
	scanf("%d",&n);
	
	//reading the adjacency matrix
	printf("\nEnter adjacency matrix of the graph in 1's and 0's (you may use the given example):\n");   
	for(i = 0; i < n; ++i)
       for(j = 0; j < n; ++j){
       	printf("M[%d][%d] = ", i, j);
       	scanf("%d", &M[i][j]);
	   }
	
	//intializing visited[] to 0
   for(i=0;i<n;++i)
        visited[i]=0;
	
	printf("\nVertices are visited in the following order:\n");
	DFS(0);
	   
   return 0;
}
