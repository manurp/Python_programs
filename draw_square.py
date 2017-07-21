import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor('#123')

	draw = turtle.Turtle()
	draw.shape('turtle')
	draw.color('#fed')   #different color can be used
	draw.speed(2)
	for _ in range(4):
		draw.forward(200)
		draw.right(90)
	window.exitonclick()

draw_square()