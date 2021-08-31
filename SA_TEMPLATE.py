import pygame
import time
pygame.init() 

def image_load(location,length,width):
    img=pygame.image.load(location).convert_alpha()
    img_scaled=pygame.transform.smoothscale(img,(length,width))
    return img_scaled
def coin_display():
  x=0
  for i in coins:
    screen.blit(i,(50*(x+1)+50,240))
    x+=1
    
def collection(char_rect):
  x=0
  for i in coins:
    coin_rect=i.get_rect(topleft=(50*(x+1)+50,240))
    x+=1
    if coin_rect.collidepoint(char_rect.x,char_rect.y):
      coins.remove(i)
      return True
      
#Create  text display function here










size = (400, 400)
screen = pygame.display.set_mode(size)
bg=image_load("Assets/bg.png",800,400)
char=image_load("Assets/character.png",40,60)
coin= image_load("Assets/coin.png",30,30)
coins=[coin for i in range(6)]
bgx=0
charx,chary=10,240
money=0
total_time=300


carryOn = True
t1=time.time()
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False  
  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_RIGHT:
      charx+=1
      bgx-=1
  if charx>=350:
    charx=10
    bgx=0
    coins=[coin for i in range(6)]

  screen.blit(bg,(bgx,0))
  screen.blit(char,(charx,chary))
  coin_display()

  char_rect=char.get_rect(topleft=(charx,chary))
  collected=collection(char_rect)
  if collected==True:
    money+=1000
    
  #Display money here 
 
  
  
  t2=time.time()
  time_elapsed=t2-t1
  time_left=round((total_time-time_elapsed)/60,2)
  text_display(24,"Time left: "+str(time_left)+"min",255,0,255,260,10)
 
  if time_elapsed>=300:
    pygame.time.wait(2000)
     # Complete closing the game here
    
    
    
    
    
    
    

  pygame.display.flip()
pygame.quit()
