import pygame
import os
import math
import random
pygame.init()
W = 800
H =500
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("The Hangman Game")

def draw():
    win.fill((255,255,255))
    text=LETTER_FONT.render("HANGMAN",1,BLACK)
    win.blit(text, (W/2-text.get_width()/2,20))
    display_word=""
    for letter in word:
        if letter in guessed:
            display_word+=letter + " "

        else: 
            display_word+=" _"

    text=LETTER_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))


    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text=LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

    win.blit(images[hangman_status],(150,100))
    pygame.display.update()
#load images
RADIUS = 20
GAP = 15
A=65
BLACK=(0,0,0)
letters = []
startx = round((W - (RADIUS*2+GAP)*13)/2)
starty = 400

#fonts
LETTER_FONT=pygame.font.SysFont('comicsans',40)

for i in range(26):
    x=startx+GAP*2+((RADIUS*2+GAP)*(i%13))
    y=starty + ((i//13)*(GAP + RADIUS*2))
    letters.append([x,y, chr(A+i), True])

images = []
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".jpg")
    images.append(image)
print(images)
#hangman_status
hangman_status=0
words=["CIDMOOSA","KOCHIRAJAVU","EZRA","NIZHAL"]
word=random.choice(words)
guessed =[]


# SETUP game loop
FPS=60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type ==pygame.MOUSEBUTTONDOWN:
            m_x,m_y=pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible=letter
                if visible:
                    dis=math.sqrt((x-m_x)**2+(y-m_y)**2) #pythagoras therorem
                    if dis<RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
  
    won=True
    draw()
    for letter in word:
        if letter not in guessed:
            won=False
            break
    if won:
        win.fill((255,255,255))
        text=LETTER_FONT.render("YOU WON",1,BLACK)
        win.blit(text, (W/2-text.get_width()/2,H/2-text.get_height()/2))
        pygame.display.update()
        pygame.delay.time(3000)
        break
    if hangman_status==6:
        win.fill((255,255,255))
        text=LETTER_FONT.render("YOU LOST",1,BLACK)
        win.blit(text, (W/2-text.get_width()/2,H/2-text.get_height()/2))
        pygame.display.update()
        pygame.delay.time(3000)
        break

pygame.quit()

