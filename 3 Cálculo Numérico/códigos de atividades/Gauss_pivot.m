clear all; close all;
C = input('Entre com a matriz dos coeficientes: ');
b = input('Entre com a matriz coluna dos termos independentes: ');
[N,M] = size(C); %Encontra a ordem da matriz
A = [C,b]
%Triangularização do sistema
for j = 1:(M-1)
    [Y,I] = max(abs(C(j:N,j))); %Encontra o maximo Y e o indice I do maximo
    k = I+j-1; %Indice do pivo
    C([j k],:) = C([k j],:); %Troca de linhas
    b([j k]) = b([k j]);
    for i = (j+1):N
        m = C(i,j)/C(j,j); %Multiplicador
        C(i,:) = C(i,:) - m*C(j,:); %Anula o elemento i da j-esima coluna
        b(i) = b(i) - m*b(j);
    end
    A = [C,b]
end
%Cálculo das raízes
for i = N:-1:1
    x(i) = b(i)/C(i,i);
    for j = i+1:M
        x(i) = x(i) - C(i,j)*x(j)/C(i,i);
    end
end
Sol = x'