# obejects : pipe, sulley, ground  -> 3 classes 

import pygame
import neat
import time
import os
import random

# loading img,set dimention of the screen 
Win_width = 600
Win_height = 800

Sulley_imgs = [pygame.image.load(os.path.join('imgs', 'st.png')),pygame.image.load(os.path.join('imgs', 'fly.png'))]
Pip_img = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
Base_img = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
Bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))


class Sulley:
    """
    class for flying Sulley 
    """
    IMGS = Sulley_imgs
    # how much sulley will flappy. Since no bird img, it will be how much sulley shaking
    Max_rotation = 25
    Rot_vel = 20
    # speed of flappy
    Animation_time = 5

    def _init_(self,x,y):
        # position of bird
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel=0
        self.height = self.y
        self.img_count =0
        self.img = self.IMGS[0]

    def jump(self):
        """
        docstring
        """
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # based on the current velocity, how much we moving up and how much we r moving down
        d = self.vel * self.tick_count + 1.5*self.tick_count**2 
        
