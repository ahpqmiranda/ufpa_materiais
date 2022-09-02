# Libraries used in this script
import cv2
import numpy as np
import RPi.GPIO as GPIO

LimiarB = 125
area_contorno = 5000

# GPIOs utilizados:
GPIOMotor1 = 18  # Broadcom pi2067n 18 (P1 pin 12)
GPIOMotor2 = 17  # Broadcom pin 17 (P1 pin 11)

# Setup dos GPIOs:
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIOMotor1, GPIO.OUT)
GPIO.setup(GPIOMotor2, GPIO.OUT)
GPIO.output(GPIOMotor1, GPIO.LOW)
GPIO.output(GPIOMotor2, GPIO.LOW)

camera = cv2.VideoCapture(0)
camera.set(3, 320)
camera.set(4, 240)


def TrataImagem(img):
    # obtencao das dimensoes da imagem
    height = np.size(img, 0)
    width = np.size(img, 1)
    QtdeContornos = 0
    DirecaoASerTomada = 0

    # tratamento da imagem
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    FrameBinarizado = cv2.threshold(gray, LimiarB, 255, cv2.THRESH_BINARY)[1]
    FrameBinarizado = cv2.dilate(FrameBinarizado, None, iterations=2)
    FrameBinarizado = cv2.bitwise_not(FrameBinarizado)

    # descomente as linhas abaixo se quiser ver o frame apos binarizacao, dilatacao e inversao de cores
    cv2.imshow('F.B.', FrameBinarizado)
    cv2.waitKey(10)

    _, cnts, _ = cv2.findContours(FrameBinarizado.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, cnts, -1, (255, 0, 255), 3)

    for c in cnts:
        # se a area do contorno capturado for pequena, nada acontece
        if cv2.contourArea(c) < area_contorno:
            continue

            QtdeContornos = QtdeContornos + 1

        # obtem coordenadas do contorno (na verdade, de um retangulo que consegue abrangir todo ocontorno) e
        # realca o contorno com um retangulo.
        (x, y, w, h) = cv2.boundingRect(c)  # x e y: coordenadas do vertice superior esquerdo
        # w e h: respectivamente largura e altura do retangulo

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # determina o ponto central do contorno e desenha um circulo para indicar
    CoordenadaXCentroContorno = (x + x + w) / 2
    CoordenadaYCentroContorno = (y + y + h) / 2
    PontoCentralContorno = (CoordenadaXCentroContorno, CoordenadaYCentroContorno)
    cv2.circle(img, PontoCentralContorno, 1, (0, 0, 0), 5)

    DirecaoASerTomada = CoordenadaXCentroContorno - (width / 2)  # em relacao a linha central

    # output da imagem
    # linha em azul: linha central / referencia
    # linha em verde: linha que mostra distancia entre linha e a referencia
    cv2.line(img, (width / 2, 0), (width / 2, height), (255, 0, 0), 2)

    if QtdeContornos > 0:
        cv2.line(img, PontoCentralContorno, (width / 2, CoordenadaYCentroContorno), (0, 255, 0), 1)

    cv2.imshow('Analise de rota', img)
    cv2.waitKey(10)
    return DirecaoASerTomada, QtdeContornos


def main():
    # tempo de adaptar a câmera
    for i in range(0, 20):
        (grabbed, Frame) = camera.read()

    # loop principal
    while True:
        try:
            grabbed, Frame = camera.read()

            if grabbed:
                Direcao, QtdeLinhas = TrataImagem(Frame)
                if QtdeLinhas == 0:
                    print("Nenhuma linha encontrada")
                    GPIO.output(GPIOMotor1, GPIO.LOW)
                    GPIO.output(GPIOMotor2, GPIO.LOW)
                    continue

                if Direcao > 0:
                    print("Distancia da linha de referencia: " + str(abs(Direcao)) + " pixels a direita")
                    GPIO.output(GPIOMotor1, GPIO.HIGH)
                    GPIO.output(GPIOMotor2, GPIO.LOW)
                if Direcao < 0:
                    print("Distancia da linha de referencia: " + str(abs(Direcao)) + " pixels a esquerda")
                    GPIO.output(GPIOMotor1, GPIO.LOW)
                    GPIO.output(GPIOMotor2, GPIO.HIGH)
                if Direcao == 0:
                    print("Exatamente na linha de referencia!")
                    GPIO.output(GPIOMotor1, GPIO.HIGH)
                    GPIO.output(GPIOMotor2, GPIO.HIGH)
        except KeyboardInterrupt:
            GPIO.output(GPIOMotor1, GPIO.LOW)
            GPIO.output(GPIOMotor2, GPIO.LOW)

        finally:
            GPIO.cleanup()
            exit(1)

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
