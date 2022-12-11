"""
CIS 1415 Final Project
Shannon Mattila
"""

from tkinter import *
from tkinter.filedialog import asksaveasfile
import pygame
from pygame.locals import *
from assets import button



# Hints dictionary
hints = open("assets/Clues.txt", "r", encoding='utf-8')
hint = {}
for (i, line) in enumerate(hints):
    hint[i] = line

root = Tk()

# Game play
def game():
    root.quit()
    pygame.init()
    
    # Display attributes
    pygame.display.set_caption('Escape Room')
    screen = pygame.display.set_mode((1220,680), 0)
    clock = pygame.time.Clock()
    fontMain = pygame.font.Font('assets/helvetica.otf', 18)
    
    # Transparent images on alpha channel
    bg = pygame.image.load('assets/morgue.png').convert_alpha()
    escimg = pygame.image.load('assets/Escape.png').convert_alpha()
    coordsH = pygame.image.load('assets/transparentH.png').convert_alpha()
    coordsV = pygame.image.load('assets/transparentV.png').convert_alpha()

    # Selectable coordinates/Buttons
    coordsTagPoe = button.Button(220, 187, coordsH, 0.45)
    coordsTagLovecraft = button.Button(327, 275, coordsH, 0.45)
    coordsJars = button.Button(160, 320, coordsH, 0.18)
    coordsJournal = button.Button(140, 360, coordsH, 0.27)
    coordsBag = button.Button(110, 413, coordsH, 0.22)
    coordsCrack = button.Button(570, 93, coordsH, 0.3)
    coordsEnscript = button.Button(530, 270, coordsV, 0.3)
    coordsCertificate = button.Button(600, 373, coordsH, 0.22)
    coordsFootnote = button.Button(600, 500, coordsH, 0.3)
    escbtn = button.Button(1030,500, escimg, 0.45)
    
    # Combination lock simulation display
    combofont = pygame.font.Font('assets/helvetica.otf', 32)
    combo1box = pygame.Rect(980, 100, 140, 32)
    combo2box = pygame.Rect(980, 100, 140, 32)
    combo3box = pygame.Rect(980, 100, 140, 32)
    combo4box = pygame.Rect(980, 100, 140, 32)
    color_active = pygame.Color('green')
    color_inactive = pygame.Color('darkgreen')
    colorbox1 = color_inactive
    colorbox2 = color_inactive
    colorbox3 = color_inactive
    colorbox4 = color_inactive
    active1 = False
    active2 = False
    active3 = False
    active4 = False
    textbox1 = ''
    textbox2 = ''
    textbox3 = ''
    textbox4 = ''

    # Outer bounds 
    font = pygame.font.Font('assets/fizzyblood.otf', 40)
    text = font.render('CLICK ITEMS TO SOLVE RIDDLES AND COLLECT CLUES', True, "crimson", "white")
    textRect = text.get_rect()
    textRect.center = (460, 650)
    

    # Combination lock simulation events
    colorbox1 = color_active if active1 else color_inactive
    colorbox2 = color_active if active2 else color_inactive
    colorbox3 = color_active if active3 else color_inactive
    colorbox4 = color_active if active4 else color_inactive
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If combination lock input selected, turn active color, else, leave as is
                if combo1box.collidepoint(event.pos):
                    active1 = not active1
                else:
                    active = False

                if combo2box.collidepoint(event.pos):
                    active2 = not active2
                else:
                    active2 = False

                if combo3box.collidepoint(event.pos):
                    active3 = not active3
                else:
                    active3 = False

                if combo4box.collidepoint(event.pos):
                    active4 = not active4
                else:
                    active4 = False


            # Enter text in the combination lock simulation
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        print(textbox1)
                    if event.key == pygame.K_BACKSPACE:
                        textbox1 = textbox1[:-1]
                    else:
                        textbox1 += event.unicode
                        
                if active2:
                    if event.key == pygame.K_RETURN:
                        print(textbox2)
                    if event.key == pygame.K_BACKSPACE:
                        textbox2 = textbox2[:-1]
                    else:
                        textbox2 += event.unicode
                        
                if active3:
                    if event.key == pygame.K_RETURN:
                        print(textbox3)
                    if event.key == pygame.K_BACKSPACE:
                        textbox3 = textbox3[:-1]
                    else:
                        textbox3 += event.unicode
                        
                if active4:
                    if event.key == pygame.K_RETURN:
                        print(textbox4)
                    if event.key == pygame.K_BACKSPACE:
                        textbox4 = textbox4[:-1]
                    else:
                        textbox4 += event.unicode

        # Outer bounds and background image attributes
        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))

        # Selectable areas
        if coordsTagPoe.draw(screen):
            tagPoe()
        if coordsTagLovecraft.draw(screen):
            tagLovecraft()
        if coordsJars.draw(screen):
            jars()
        if coordsJournal.draw(screen):
            journal()
        if coordsBag.draw(screen):
            bag()
        if coordsCrack.draw(screen):
            crack()
        if coordsEnscript.draw(screen):
            enscription()
        if coordsCertificate.draw(screen):
            certificate()
        if coordsFootnote.draw(screen):
            footnote()
        if escbtn.draw(screen):
            userInput = [textbox1, textbox2, textbox3, textbox4]
            answer = ["012", "456", "789", "234"]
            if (userInput == answer):
                win()
                return
            else:
                textbox1 = ""
                textbox2 = ""
                textbox3 = ""
                textbox4 = ""

        
        # Combination lock box text boxes
        inptxt1 = fontMain.render(textbox1, True, colorbox1)
        inptxt2 = fontMain.render(textbox2, True, colorbox2)
        inptxt3 = fontMain.render(textbox3, True, colorbox3)
        inptxt4 = fontMain.render(textbox4, True, colorbox4)

        # Resize text box if the text is too long.
        inpwidth1 = max(200, inptxt1.get_width()+10)
        inpwidth2 = max(200, inptxt2.get_width()+10)
        inpwidth3 = max(200, inptxt3.get_width()+10)
        inpwidth4 = max(200, inptxt4.get_width()+10)
        combo1box.w = inpwidth1
        combo2box.w = inpwidth2
        combo3box.w = inpwidth3
        combo4box.w = inpwidth4

        # Blit the text.
        screen.blit(inptxt1, (combo1box.x+5, combo1box.y+5))
        screen.blit(inptxt2, (combo2box.x+5, combo2box.y+5))
        screen.blit(inptxt3, (combo3box.x+5, combo3box.y+5))
        screen.blit(inptxt4, (combo4box.x+5, combo4box.y+5))

        # Blit the input_box rect.
        pygame.draw.rect(screen, colorbox1, combo1box, 2)
        pygame.draw.rect(screen, colorbox2, combo2box, 2)
        pygame.draw.rect(screen, colorbox3, combo3box, 2)
        pygame.draw.rect(screen, colorbox4, combo4box, 2)

        pygame.display.flip()
        
        # Throttle framerate to 60FPS
        clock.tick(60)

        

def saveFile():
    f = asksavefile(initialfile = 'Notes.txt', defaultextension = ".txt", filetypes = [("All Files", "*.*"),
                                                                                       ("Text Documents", "*.txt")])

def jars():
    master = Tk()
    clue = hint[0]+hint[1]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    master.mainloop()


def journal():
    master = Tk()
    clue = hint[2]+hint[3]+hint[4]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    labeltxt = Label(master, text="You found a pen & medical journal in a smock pocket.\nMost pages have been removed.\nUse the blank pages to take notes.\n\nSave to Desktop?")
    labeltxt.pack()
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    savebtn = Button(master, text = 'Save', font = ('assets/helvetica.otf', 18), command=lambda:saveFile())
    savebtn.pack(padx = 10, pady = 10, side=LEFT)
    master.mainloop()


def crack():
    master = Tk()
    clue = hint[5]+hint[6]+hint[7]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    labeltxt = Label(master, text="Enter the answer: ")
    labeltxt.pack()
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())        
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    submitbtn = Button(master, text = 'Save', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())
    submitbtn.pack(padx = 10, pady = 10, side=LEFT)
    master.mainloop()

def bag():
    master = Tk()
    clue = hint[8]+hint[9]+hint[10]+hint[11]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    labeltxt = Label(master, text="Enter the answer: ")
    labeltxt.pack()
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())        
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    submitbtn = Button(master, text = 'Save', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())
    submitbtn.pack(padx = 10, pady = 10, side=LEFT)
    master.mainloop()  


def footnote():
    master = Tk()
    clue = hint[12]+hint[13]+hint[14]+hint[15]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    labeltxt = Label(master, text="Enter the answer: ")
    labeltxt.pack()
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())        
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    master.mainloop()

def tagPoe():
    master = Tk()
    clue = hint[16]+hint[17]+hint[18]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())        
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    master.mainloop()

def tagLovecraft():
    master = Tk()
    clue = hint[25]+hint[26]+hint[27]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())        
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    master.mainloop()

def enscription():
    master = Tk()
    clue = hint[12]+hint[13]+hint[14]+hint[15]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    labeltxt = Label(master, text="Enter the answer: ")
    labeltxt.pack()
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())        
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    master.mainloop() 

def certificate():
    master = Tk()
    clue = hint[19]+hint[20]+hint[21]+hint[22]+hint[23]+hint[24]
    label = Label(master, text = clue, font = ('assets/helvetica.otf', 18))
    label.pack(padx = 10, pady = 10)
    exitbtn = Button(master, text = 'Exit', font = ('assets/helvetica.otf', 18), command=lambda:master.destroy())        
    exitbtn.pack(padx = 10, pady = 10, side=RIGHT)
    master.mainloop()


    
def win():
    master = Tk
    winbg = PhotoImage(file = "assets/win.png")
    master.geometry("920x614")
    # Display image using a label option
    winlabel = Label(master, image = winbg)
    winlabel.place(x = 0, y = 0)
    master.mainloop()

  
# Main Menu
def menu():
    root.geometry("850x628")
    bg = PhotoImage(file=r"assets/hall.png")
    canvas = Canvas(root, width = 500, height = 400)
    canvas.pack(fill = "both", expand = True)
    # Display
    canvas.create_image(0, 0, image = bg, anchor = NW)
    premise = Label(root, text="You've been locked in a morge of an abandoned hospital. \nThe only way to survive this ordeal is to look for clues left\n behind by countless others... who may or may not \nhave survived. ", font=("Helvetica", 14, "bold"), bg = "white")
    premise.place(x = 50, y = 120)
    instruction = Label(root, text="You've discovered a door locked by a numberical \ncombination  padlock. Perhaps  this  door will lead you to\n your salvation! Collect clues to unlock all four 3-digit numbers.", font=("Helvetica", 14, "bold"), bg = "green")
    instruction.place(x = 50, y = 280)
    playbtn = Button(root, text = "Play", font=('assets/helvetica.otf', 20), padx= 20, command = game)
    playbtn.place(x = 700, y = 500)
    root.mainloop()  
menu()

