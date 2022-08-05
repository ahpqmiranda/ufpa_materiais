import random as rd

def questions(n_questions):
    answers = []
    print("\\begin{enumerate}[a) ]")
    for j in range(0, n_questions):
        soma = 0
        n = rd.randint(1, 10)
        print("\item $", end="")

        for i in range(n):
            a = rd.randint(-20, 20)
            soma = soma + a
            if a > 0:
                print("+", a, end="")
            else:
                print(a, end="")

        print("$\n")
        answers.append(soma)
    print("\\end{enumerate}")
    return answers

if __name__ == '__main__':
    answers = questions(10)
    print("\\newpage \par respostas \\begin{enumerate} [a) ] ")
    for i in range(len(answers)):
        print("\\item $", answers[i], "$")

    print("\\end{enumerate}")
