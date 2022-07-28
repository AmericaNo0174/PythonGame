import turtle
import math
import random
import tkinter
import pygame

#pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
pygame.mixer.music.load("Sunflower.wav")
pygame.mixer.music.play(-1)

screen = turtle.Screen()
screen.bgpic("play.gif")

#Setup the screen ตั้งค่า พื้นหลัง
turtle.setup(700,700)

def enter():
    screen.clearscreen()
    main()
turtle.listen()
turtle.onkey(enter,"space")

def main():
    screen.bgcolor("black")
    screen.title("Kop Ma Jak Net")
    screen.bgpic("screen.gif")
    

    

   

    #Set up photo  ใส่รูปลงในเกม
    turtle.register_shape("james.gif")
    turtle.register_shape("F.gif")
    turtle.register_shape("A.gif")




    #Draw border ตั้งค่าเส้นขอบ
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("White")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()


    #Set score to 0 สร้างสกอร์ให้เป็น 0
    score = 0


    #Add to score สร้างตัวสกอร์ขึ้นมา
    Yellow = (252, 255, 0 )
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("Yellow")
    score_pen.penup()
    score_pen.setposition(-290,280)
    scorestring = "สกอร์น๊ะจ๊ะ: %s" %score
    score_pen.write(scorestring,False,align = "left",font = ("Arial",14,"normal"))
    score_pen.hideturtle()

    #Create the Gu ให้กำเนิดกรูขึ้นมา
    Gu = turtle.Turtle()
    Gu.color("blue")
    Gu.shape("james.gif")
    Gu.penup()
    Gu.speed(0)
    Gu.setposition(0,-250)
    Gu.setheading(90)

    Guspeed = 20

    #Create the Mung ให้กำเนิดมุงขึ้นมาหลายๆตัว
    number_of_Mungs = 5
    #Create an empty list of Mungs
    Mungs = []

    #Add Mungs to the list
    for i in range(number_of_Mungs):
        #ให้กำเนิดมุงขึ้นมา
        Mungs.append(turtle.Turtle())
        

    for Mung in Mungs:
        Mung.color("red") 
        Mung.shape("F.gif")
        Mung.penup()
        Mung.speed(0)
        x = random.randint(-200,200)
        y = random.randint(100,250)
        Mung.setposition(x,y)

    Mungspeed = 5  


    #Create the Gu's bullet สร้างความสามารถของตัวกรูขึ้นมา
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("A.gif")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5,0.5)
    bullet.hideturtle()

    bulletspeed = 29

    #Define bullet stateกำหนดหัวข้อย่อยของกระสุน
    #ready - ready to fire เตรียมยิงดิรอไร
    #fire - bullet is firing กระสุนพุ้ง
    global bulletstate 
    bulletstate = "ready"


    #Move the Gu left and right หัดให้กรูขยับซ้ายขวาได้
    def move_left():
        x = Gu.xcor()
        x -= Guspeed
        if x <-480:
            x = -480
        Gu.setx(x)


    def move_right():
        x = Gu.xcor()
        x += Guspeed
        if x >480:
            x = 480
        Gu.setx(x)


    def fire_bullet():
        #Declare bulletstate as a global if it needs changed ประกาศ bulletstate as เป็น global ถ้าหากจะแก้ไขอะไรๆ
        global bulletstate
        if bulletstate == "ready":
           
            bulletstate = "fire"

            #   Move the bullet to the just above the Gu ยิงกระสุนออกไปจากตัวกรูเอง
            x = Gu.xcor()
            y = Gu.ycor() +10
            bullet.setposition(x,y)
            
            bullet.showturtle()

    #Set function fighting Mung and Gu ฟังก์ชันการต่อสู้ของมุงและกรู
    def Fighting(t1,t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        #Distance of bullet ระยะของกระสุนที่โดนมุง
        if distance < 25:
            return True
        else:
            return False
        
    #Create keyboard bindings ตัวที่กำหนดให้กรูขยับได้
    turtle.listen()
    turtle.onkey(move_left,"Left")
    turtle.onkey(move_right,"Right")
    turtle.onkey(fire_bullet,"space")


    #Main game loop หัวใจในการทำงานของเกมนี้
    while True:
        for Mung in Mungs:
            #Move the Mung สอนให้มุงเดินได้
            x = Mung.xcor()
            x += Mungspeed
            Mung.setx(x)

            #Move the Mung back and down สอนให้มุงไปไหนมาไหนได้เอง
            if Mung.xcor() > 280:
                #Move the Mungs การเคลื่อนที่ลงไปของมุงทั้งหมด
                for M in Mungs:
                    y = M.ycor()
                    y -= 40
                    M.sety(y)
                #Move the Mung return เปลี่ยนทิศทางของมุงทั้งหมด
                Mungspeed *= -1   
                    
            if Mung.xcor() < -280:
                #Move the Mung down การเคลื่อนลงไปของมุงทั้งหมด
                for M in Mungs:
                    y = M.ycor()
                    y -= 40
                    M.sety(y)
                #Move the Mung return เปลี่ยนทิศทางของมุงทั้งหมด
                Mungspeed *= -1

            #Check for a collision between the bullet and the Mung ตรวจสอบว่ากระสุนไปโดนตัวมุงหรือป่าว??
            if Fighting(bullet, Mung):
                #Reset the bullet เอากระสุนออกไปสะ!!
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)
                #Reset the Mung เอามุงออกไปสะ!! จุดเกิดของมุง
                x = random.randint(-200,200)
                y = random.randint(100,250)
                Mung.setposition(x,y)
                #Get points ได้คะแนนละนะ
                score += 555
                scorestring = "สกอร์น๊ะจ๊ะ: %s" %score
                score_pen.clear()
                score_pen.write(scorestring,False,align = "left",font = ("Arial",14,"normal"))
            #Hide Gu and Mung     
            if Mung.ycor() <= -250 :
                
                Gu.hideturtle()
                Mung.hideturtle()
                screen.clearscreen()
                end = turtle.Screen()
                end.bgpic("end.gif")
                pen = turtle.Turtle()
                pen.color("Green")
                pen.write("Score "+str(score),align="center",font=("arial", 70,"bold"))
                pen.hideturtle()
                pen.penup()
                pen.goto(7,6)

                def btnclick(x,y):
                    if x < -61 and x > -271 and y < -21 and y > -80:
                        end.clearscreen()
                        main()
                    if x < 271 and x > 60 and y < -21 and y > -80:
                        quit()

                turtle.onscreenclick(btnclick,1)
                turtle.listen()
                
                turtle.done()
                break
        if Mung.ycor() <= -250 :
            break



        #Move the bullet การเดินทางของกระสุน
        if bulletstate == "fire": #ถ้าอยากให้กระสุนยิงรัวให้ใส่ # ตรงนี้นะๆๆๆ
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        #Check to see if the bullet has gone to the top ดูว่ากระสุนออกไปด้านบนถึงตรงที่กำหนดรึป่าว??
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

        

        
   


