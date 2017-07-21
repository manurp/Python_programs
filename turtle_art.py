import turtle
def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')

	brad = turtle.Turtle()
	brad.color('#','blue')
	brad.shape('turtle')
	brad.speed(20)
	brad.left(10)

	for _ in range(36):
		brad.right(10)
		for i in range(4):
			brad.forward(100)
			brad.right(90)

	window.exitonclick()
draw_art()