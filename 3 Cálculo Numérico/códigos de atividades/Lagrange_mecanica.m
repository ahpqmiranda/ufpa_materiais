%Polinômio Interpolador de Lagrange

x=[3 4 5];%input('Digite os pontos')
y=[0.3333 0.25 0.2];
xx=4.5;
M=length(x);
P=0;

for i=1:M
    L=1;
    for j=1:M
        if j~=i
            L=L*(xx-x(j))/(x(i)-x(j));
        end
    end
    %L
    P=P+L*y(i);
end
P