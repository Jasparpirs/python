import turtle

#Jaspar pirs
#harjutus 1.1
#04.10.2024

#muudan asukohta
turtle.penup()
turtle.goto(-400, 200)
turtle.pendown()
#tõstsin pliiatsi lasin minna õigesse kohta ja panin pliiatis maha
turtle.fd(200)
turtle.left(120)
turtle.fd(200)
turtle.left(120)
turtle.fd(200)
turtle.left(120)

#muudan asukohta
turtle.penup()
turtle.goto(-100, 200)
turtle.pendown()
#J-täht
turtle.penup()
turtle.goto(0, 0)  
turtle.pendown()

turtle.right(90)  
turtle.forward(100)  
turtle.right(90) 
turtle.circle(50, 180)  

# Lõpeta
turtle.penup()
turtle.hideturtle()  
turtle.done()  

#done et programm ei jookseks kokku
turtle.done()

#turtle.showturtle()
#turtle.hideturtle()