
import turtle
def build_candle_body(x, open, close, color, open1, close1) -> None:
    turtle.fillcolor(color)
    turtle.pencolor('black')
    turtle.goto(x - 25, min(open, close) + d)
    turtle.begin_fill()
    turtle.goto(x - 25, max(open, close) + d)
    turtle.goto(x + 25, max(open, close) + d)
    turtle.write(max(open1, close1))
    turtle.goto(x + 25, min(open, close) + d)
    turtle.goto(x - 25, min(open, close) + d)
    turtle.write(min(open1, close1))
    turtle.end_fill()
    if color == 'black':
        turtle.pendown()
        turtle.goto(x + 25, open + d)
        turtle.penup()
    return

def build_candle(month, x) -> None:
    if month[0][0] - month[-1][-1] < -100:
        color = 'green'
    elif month[0][0] - month[-1][-1] > 100:
        color = 'red'
    else:
        color = 'black'
    build_candle_body(x, (month[0][0] - 1 * floor) / k * 301, (month[-1][-1] - 1 * floor) / k * 301, color, month[0][0],
                      month[-1][-1])
    turtle.pencolor('black')
    
    turtle.goto(x, (min(v[2] for v in month) - 1 * floor) / k * 301 - 10 + d)

    turtle.write(min(v[2] for v in month))
    turtle.goto(x, (min(v[2] for v in month) - 1 * floor) / k * 301 + d)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x, (max(v[1] for v in month) - 1 * floor) / k * 301 + d)
    turtle.penup()
    turtle.pencolor('black')
    turtle.write(max(v[1] for v in month))

    return

d = -150
with open("Доп.csv") as f:
    s = [v.split(';') for v in f.readlines()[1:]]
month1, month2, month3, month4 = [], [], [], []
for v in s:
    if v[2] == '27.09.2018':
        month1.append(list(map(int, v[4:8])))
    elif v[2] == '29.10.2018':
        month2.append(list(map(int, v[4:8])))
    elif v[2] == '27.11.2018':
        month3.append(list(map(int, v[4:8])))
    else:
        month4.append(list(map(int, v[4:8])))
ceiling = max(int(v[5]) for v in s) # * 1.25
floor = min(int(v[6]) for v in s) # * 0.75

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(3)
k = (ceiling - floor)

turtle.title(s[0][0])

turtle.penup()
turtle.pencolor('grey')
turtle.goto(-200, 0 + d)
turtle.pendown()
turtle.goto(200, 0 + d)
turtle.penup()


build_candle(month1, -150)
build_candle(month2, -50)
build_candle(month3, 50)
build_candle(month4, 150)

turtle.penup()

turtle.pencolor('grey')
for i in range(floor, ceiling, 1000):
    turtle.goto(-200, (i - floor) / k * 301 + d)
    turtle.pendown()
    turtle.write(i)
input('Press enter...')