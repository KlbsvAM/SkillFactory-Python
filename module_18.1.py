from test import Rectangle,Square,Circle,Treug
rect_1=Rectangle(5,18)
rect_2=Rectangle(7,5)
square_1=Square(66)
square_2=Square(33)
circle_1=Circle(5)
circle_2=Circle(10)
treug_1=Treug(5,10)
treug_2=Treug(12,43)
figures=[rect_1,rect_2,square_1,square_2,circle_1,circle_2,treug_1,treug_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    if isinstance(figure,Rectangle):
        print(figure.get_area())
    if isinstance(figure,Circle):
        print(figure.get_area_circle())
    if isinstance(figure,Treug):
        print(figure.get_area_treug())
        print(figure.__str__())
