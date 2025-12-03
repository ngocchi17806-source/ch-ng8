print('nguyen ngoc chi mssv 245752021610164')
import turtle    #Nhap thu vien Turtle
#Tao cua so ve va thiet lap mau nen
window = turtle .Screen()
window.bgcolor("lightgreen")
#Tao doi tuong rua va thiet lap cac thuoc tinh
painter = turtle.Turtle()
painter.fillcolor('blue')  #Mau dổ đầy
painter.pencolor('blue')    #Màu bú
painter.pensize(3)

def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1,50):
    painter.left(18)
    drawsq(painter, 200)
