# This program was written to simulate the mandelbrot plot. 

from numpy import abs,linspace, meshgrid,zeros
from pylab import imshow

def mandel(n=50000,domain=[-2,-2,2,2],n_iter=10):
    x=linspace(domain[0],domain[2],n)
    y=linspace(domain[1],domain[3],n)
    z=zeros((n,n),complex)
    z.real,z.imag=meshgrid(x,y)
    img=z.real
    
    for row,i in enumerate(z):
        for col,j in enumerate(i):
            a=0
            count=0
            while (count<n_iter):
                a=a**2+j
                if abs(a)>2:
                    img[row,col]=1
                    break
                else:
                    count+=1
                    pass
    imshow(img)
    return img

                
                
