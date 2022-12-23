A=input('Entre com a matriz dos coeficientes: ');%[1 1 0 3; 2 1 -1 1; 3 -1 -1 2; -1 2 3 -1];
b=input('Entre com a matriz coluna dos termos independentes: ');%[4 1 -3 4]';

a=[A b]; %escreve a matriz aumentada
[N,M]=size(a); %encontra a ordem da matriz a

for j=1:N-1
    for i=j+1:N
        m(i,j)=a(i,j)/a(j,j);
        a(i,:)=a(i,:)-m(i,j)*a(j,:);
    end
    a
end

for i=N:-1:1
    x(i)=a(i,N+1)/a(i,i);
    for j=i+1:N
        x(i)=x(i)-a(i,j)*x(j)/a(i,i);
    end
end
x