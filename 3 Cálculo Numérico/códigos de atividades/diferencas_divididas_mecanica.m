
x=[3 4 5];%input('Digite os pontos')
y=[0.3333 0.25 0.2];
xx=4.5;
M=length(x);

A=y';

for j=2:M
    for i=j:M
        A(i,j)=(A(i,j-1)-A(i-1,j-1))/(x(i)-x(i-j+1));
    end
end

L=1;
P=A(1,1);

for i=1:M-1
    L=L*(xx-x(i));
    P=P+L*A(i+1,i+1);
end
P