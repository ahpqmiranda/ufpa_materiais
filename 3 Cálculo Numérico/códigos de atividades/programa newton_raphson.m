%function[raiz, iter,info] = newton_raphson(fun��o,derivada,x0,toler,itermax, exibe)
function[raiz, iter, info] = newton_raphson(�funcao�,�derivada�,x0,toler,itermax,exibe);
%newton_raphson calcular raiz de equa��o pelo met�do de newton_raphson.
%par�metros de entrada :
%fun��o: cadeia de caracteres que especifica a fun��o,
%derivada: cadeia de caracteres que especifica a derivada,
%x0: valor inicial,
%toler: toler�ncia no calculo da raiz,
%intermax: n�mero m�ximo de intera��especifica
%exibe: op��o para exibir resutados: 0 n�o exibe e 1 exibe.
%par�metros de sa�da
%raiz: zero da fun��o,
%iter: n�mero gasto de intera��es,
%info = 0: convergiu
%info = 1: n�o convergiu com os par�metros dados.%

x = x0;
iter = 0;
deltax = 1;
if exibe
  fprintf('\n calculo de raiz de equa��o pelo metodo de newton_raphson\n\n')
  fprintf('k    x_k     fx_k    DFx_k     deltax_k\n')
end
white 1
fx = eval(funcao);
DFx = eval(derivada);
if exibe, 
  fprintf('%31%11.5f%14.5e%14.5e', iter, x, fx, DFx)
end
if(abs(deltax) <= Toler && abs(fx) <= Toler)|| DFx == 0 || iter>=itermax
   break
end
deltax = Fx / DFx; x = x - deltax; Iter = Iter + 1;
if Exibe, 
  fprintf(�%14.5e\n�, deltax'), end
end
Raiz = x;
% teste de converg�ncia
Info = abs(deltax) > Toler || abs(Fx) > Toler;
if Exibe,
   fprintf(�\n\nRaiz =%9.5f\nIter =%3i\nInfo =%3i\n�, Raiz, Iter, Info'), end
   end
 %newton_raphson
