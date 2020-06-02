#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
//Define Gaussian:
float f(float x)
{
	float gauss;
	gauss=exp(-x*x);
	return(gauss);
}

int main(void)
{
	int N=250,i;
	float xvals[N],yvals[N];
	float a=-50, b=50, del_x=(b-a)/(N-1), xarr[N], k, aft_real, aft_imag, aft_abs;
	fftw_complex w_p[N], dft[N];
	fftw_plan p;
	
	for(i=0; i<N; i++)
	{
		xarr[i]=a+i*del_x;
		w_p[i][0]=f(xarr[i]); w_p[i][1]=0.0;
	}	

	p=fftw_plan_dft_1d(N, w_p, dft, FFTW_FORWARD, FFTW_ESTIMATE);	
	fftw_execute(p);
	
	FILE *bb;
	bb=fopen("data4.txt", "w");
	
	for(i=0; i<N; i++)
	{
		if(i<=(N/2-1))
		{
			k=i/(N*del_x);
			k=2*M_PI*k;
		}
		else
		{
			k=(i-N)/(N*del_x);
			k=2*M_PI*k;
		}
		aft_real=del_x*sqrt(1/(2*M_PI))*(cos(k*a)*dft[i][0]+sin(k*a)*dft[i][1]);
	   	aft_imag= del_x*sqrt(1/(2*M_PI))*(cos(k*a)*dft[i][1]-sin(k*a)*dft[i][0]);
		aft_abs=sqrt(pow(aft_real,2)+pow(aft_imag,2));	
		fprintf(bb,"%f\t%f\n",k,aft_real);
		xvals[i]=k;
		yvals[i]=aft_real;
	}
	
	fclose(bb);	

	fftw_destroy_plan(p);
	system("python plotter4.py");
}
