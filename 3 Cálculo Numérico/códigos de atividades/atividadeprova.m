clear all
close all
clc
%QUADRO DE FUN��ES:

%prova de programa��o 3ava
k = menu('Selecione uma das quest�es:','Quest�o 1','Quest�o 2',...
'Quest�o 3', 'Quest�o 4', 'Quest�o 5', 'Quest�o 6');

switch (k)
  case 1
          x = 1:100;
          y = 5*x.^2-2*x;
          r = " Os cem (100) primeiros termos da sequ�ncia\n 5x�-2x s�o ";
          s = " a s�rie :\n";
          dlgtitle = 'Quest�o 1 - Expans�o de valores de 1 a 100';
          dims = [5 90];
          xtexto = num2str(x);
          ytexto = num2str(y);
          contatstrings3 = strcat(r,s,ytexto);
          opts.Interpreter = 'text';
          answer = questdlg(contatstrings3,dlgtitle,dims,opts);
  
  case 2
          m = menu('Selecione uma das quest�es:', 'Quest�o 2A',...
          'Quest�o 2B', 'Quest�o 2C', 'Quest�o 2D');
          switch (m)
            case 1
              clc
                  a=zeros(3,3);                  
                  % quest�o 2-A
                  for i=1:3
                    for j=1:3
                      a(i,j) = (i + j);
                    endfor                    
                  end
          r = " Quest�o 2-A:\n Matriz A(i,j) = i + j\n\n ";
          dlgtitle = 'Quest�o 2-A - Matriz A(i,j)';
          dims = [1 90];
          contatstrings3 = strcat(r,disp(a));
          opts.Interpreter = 'text';
          answer = questdlg(contatstrings3,dlgtitle,dims,opts);
            
          case 2
            clc
                  b = zeros(3,3);
                  % Quest�o 2-B
                  for i=1:3
                    for j=1:3
                      b(i,j) = (i+2) + j.^2;
                    endfor                    
                  end
          r = " Quest�o 2-B:\n Matriz B(i,j) = i + 2 + j�\n\n ";
          dlgtitle = 'Quest�o 2-B - Matriz B(i,j)';
          dims = [5 90];
          contatstrings4 = strcat(r,disp(b));
          opts.Interpreter = 'text';
          answer = questdlg(contatstrings4,dlgtitle,dims,opts);
            case 3
            clc
                  c = zeros(3,3);
                  %Quest�o 2 - C
                  for i=1:3
                    for j=1:3
                      c(i,j) = 3*sqrt(i)-i*j.^2;
                    endfor                    
                  end
            r = " Quest�o 2-C:\n Matriz C(i,j) = 3*sqrt(i)-i*j�\n\n ";
            dlgtitle = 'Quest�o 2-C - Matriz C(i,j)';
            dims = [5 90];
            contatstrings5 = strcat(r,disp(c));
            opts.Interpreter = 'text';
            answer = questdlg(contatstrings5,dlgtitle,dims,opts);           
                    
            case 4
                  clc
                   d = zeros(3,3);
                   % Quest�o 2 - D
                   for i=1:3
                      for j=1:3
                      d(i,j) = i.^2*sqrt(j)+i*(j-1);
                      endfor                    
                   end
          r = " Quest�o 2-D:\n Matriz D(i,j) = (i^2)*sqrt(j) + i*(j-1)\n\n ";
          dlgtitle = 'Quest�o 2-D - Matriz D(i,j)';
          dims = [5 90];
          contatstrings6 = strcat(r,disp(d));
          opts.Interpreter = 'text';
          answer = questdlg(contatstrings6,dlgtitle,dims,opts);                   
          endswitch

  case 3
          dlgtitle = 'Quest�o 3 - Valor do somat�rio.';
          answer = inputdlg('Temos a fun��o somat�rio de ((-1)^n)/(2*n+1))). Digite um valor para "m"',dlgtitle);   
          m = str2num(answer{1})
          r = 0;
          soma = 0;
          for n=1:m
           r = sum((-1).^n*(1./(2*n+1)));
           soma += r;               
          endfor
          r = " Termo n�mero: "
          s = " \n E serie n�mero: ";
          somatexto =  num2str(soma);
          mtexto  = num2str(m);
          dlgtitle = 'Quest�o 3 - Valor da fun��o.';
          dims = [1 150];
          contatstrings = strcat(r,mtexto,s,somatexto);
          opts.Interpreter = 'text';
          answer = questdlg(contatstrings,dlgtitle,dims,opts);
  case 4
          % Quest�o 4:
          i = 6*10^(-4);
          c = 2;
          E = 200*10^9;
          L = 3;
          P = 6*10^3;
          k = 2*P*L^3/E*I*pi^4;
          x = L/2;
          
          % fprintf("Valor da sequ�ncia para os 5 primeiros termos da s�rie\n")

          for n=1:5
            y(n) = k.*(1/n.^4).*sin((n.*pi/L).*c)*sin(n.*pi./L.*x);
          endfor
          
          r = 'Valor da sequ�ncia para os 5 primeiros termos da s�rie:';
          dlgtitle = 'Quest�o 4 - Primeiros 5 elementos: ';
          dims = [5 100];
          ytexto3 = num2str(y);
          contatstrings8 = strcat(r,ytexto3);   
          answer = questdlg(contatstrings8,dlgtitle,dims,optimset);

  case 5
          % Quest�o 5:
          %m = input("Digite o numero maior que zero para fibonacci a ser mostrada: ");
          dlgtitle = 'Quest�o 5 - Expans�o de Fibonacci.';
          answer = inputdlg('Digite o numero maior que zero para fibonacci a ser mostrada: ',dlgtitle);   
          m = str2num(answer{1});         
          
          switch(m)
            case(0)
               r = " termo n�:00 ";
               s = " e s�rie :00 ";
               dlgtitle = 'Quest�o 5 - Expans�o de Fibonacci.';
               dims = [1 100];
               contatstrings2 = strcat(r,s);
               opts.Interpreter = 'text';
               answer = questdlg(contatstrings2,dlgtitle,dims,optimset);
            case(1)
               r = " termo n�:01";
               s = " e s�rie :01";
               dlgtitle = 'Quest�o 5 - Expans�o de Fibonacci.';
               dims = [1 100];
               contatstrings2 = strcat(r,s);
               opts.Interpreter = 'text';
               answer = questdlg(contatstrings2,dlgtitle,dims,opts);
          otherwise
               fib1=0;
               fib=1;
               soma=0;
            for i=1:m
              soma = fib1+fib;
              fib1 = fib;
              fib = soma;
            endfor
               r = " termo n�:0 ";
               s = " e s�rie :0 ";
               itexto = num2str(i);
               fibtexto = num2str(fib);
               dlgtitle = 'Quest�o 5 - Expans�o de Fibonacci.';
               dims = [1 100];
               contatstrings2 = strcat(r,itexto,s,fibtexto);
               opts.Interpreter = 'text';
               answer = questdlg(contatstrings2,dlgtitle,dims,opts);
          endswitch
  case 6
          % Quest�o 6:
          G = 6.672*10.^(-11);
          MT = 5.98*10.^(24);
          RT = 4.216*10^(7);%38*10.^(6); tem que ser a dist�ncia da orbita ao centro de massa
          
          prompt = {"Digite a massa do corpo orbital em quilos:"};
          dlgtitle = 'Quest�o 6 - For�a de atra��o orbital';
          definput = {''};
          dims = [1 40];
          opts.Interpreter = 'text';
          mass = inputdlg(prompt,dlgtitle,dims,definput,opts);
          
          m1 = str2num(mass{1});
          F = G*MT*m1/(RT.^2) ;
          
          k = "A for�a de atra��o gravitacional na �rbita geoestacion�ria �\n de:";
          Ftexto =  num2str(F);
          concattexto = strcat(k,Ftexto," Newtons.");
          opts.Interpreter = 'text';
          opts.Default = 'Resultado esperado';
          answer = questdlg(concattexto,dlgtitle,dims,opts);
          % obs: a estrutura de janelas utilizadas nessa quest�o gerou bugs
          % horr�veis com as estruturas de loop for, do while e while

          
endswitch         