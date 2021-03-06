import sys
import pygame
import random


pygame.init()
clock = pygame.time.Clock()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Color Cycle")

color=[pygame.Color(128,0,0),pygame.Color(139,0,0),pygame.Color(165,42,42),pygame.Color(178,34,34),pygame.Color(220,20,60),pygame.Color(255,0,0),pygame.Color(255,99,71),pygame.Color(255,127,80),pygame.Color(205,92,92),pygame.Color(240,128,128),pygame.Color(233,150,122),pygame.Color(250,128,114),pygame.Color(255,160,122),pygame.Color(255,69,0),pygame.Color(255,140,0),pygame.Color(255,165,0),pygame.Color(255,215,0),pygame.Color(184,134,11),pygame.Color(218,165,32),pygame.Color(238,232,170),pygame.Color(189,183,107),pygame.Color(240,230,140),pygame.Color(128,128,0),pygame.Color(255,255,0),pygame.Color(154,205,50),pygame.Color(85,107,47),pygame.Color(107,142,35),pygame.Color(124,252,0),pygame.Color(127,255,0),pygame.Color(173,255,47),pygame.Color(0,100,0),pygame.Color(0,128,0),pygame.Color(34,139,34),pygame.Color(0,255,0),pygame.Color(50,205,50),pygame.Color(144,238,144),pygame.Color(152,251,152),pygame.Color(143,188,143),pygame.Color(0,250,154),pygame.Color(0,255,127),pygame.Color(46,139,87),pygame.Color(102,205,170),pygame.Color(60,179,113),pygame.Color(32,178,170),pygame.Color(47,79,79),pygame.Color(0,128,128),pygame.Color(0,139,139),pygame.Color(0,255,255),pygame.Color(0,255,255),pygame.Color(224,255,255),pygame.Color(0,206,209),pygame.Color(64,224,208),pygame.Color(72,209,204),pygame.Color(175,238,238),pygame.Color(127,255,212),pygame.Color(176,224,230),pygame.Color(95,158,160),pygame.Color(70,130,180),pygame.Color(100,149,237),pygame.Color(0,191,255),pygame.Color(30,144,255),pygame.Color(173,216,230),pygame.Color(135,206,235),pygame.Color(135,206,250),pygame.Color(25,25,112),pygame.Color(0,0,128),pygame.Color(0,0,139),pygame.Color(0,0,205),pygame.Color(0,0,255),pygame.Color(65,105,225),pygame.Color(138,43,226),pygame.Color(75,0,130),pygame.Color(72,61,139),pygame.Color(106,90,205),pygame.Color(123,104,238),pygame.Color(147,112,219),pygame.Color(139,0,139),pygame.Color(148,0,211),pygame.Color(153,50,204),pygame.Color(186,85,211),pygame.Color(128,0,128),pygame.Color(216,191,216),pygame.Color(221,160,221),pygame.Color(238,130,238),pygame.Color(255,0,255),pygame.Color(218,112,214),pygame.Color(199,21,133),pygame.Color(219,112,147),pygame.Color(255,20,147),pygame.Color(255,105,180),pygame.Color(255,182,193),pygame.Color(255,192,203),pygame.Color(250,235,215),pygame.Color(245,245,220),pygame.Color(255,228,196),pygame.Color(255,235,205),pygame.Color(245,222,179),pygame.Color(255,248,220),pygame.Color(255,250,205),pygame.Color(250,250,210),pygame.Color(255,255,224),pygame.Color(139,69,19),pygame.Color(160,82,45),pygame.Color(210,105,30),pygame.Color(205,133,63),pygame.Color(244,164,96),pygame.Color(222,184,135),pygame.Color(210,180,140),pygame.Color(188,143,143),pygame.Color(255,228,181),pygame.Color(255,222,173),pygame.Color(255,218,185),pygame.Color(255,228,225),pygame.Color(255,240,245),pygame.Color(250,240,230),pygame.Color(253,245,230),pygame.Color(255,239,213),pygame.Color(255,245,238),pygame.Color(245,255,250),pygame.Color(112,128,144),pygame.Color(119,136,153),pygame.Color(176,196,222),pygame.Color(230,230,250),pygame.Color(255,250,240),pygame.Color(240,248,255),pygame.Color(248,248,255),pygame.Color(240,255,240),pygame.Color(255,255,240),pygame.Color(240,255,255),pygame.Color(255,250,250),pygame.Color(0,0,0),pygame.Color(105,105,105),pygame.Color(128,128,128),pygame.Color(169,169,169),pygame.Color(192,192,192),pygame.Color(211,211,211),pygame.Color(220,220,220),pygame.Color(245,245,245),pygame.Color(255,255,255)]


endCounter = len(color)
startCounter = 0

print(endCounter)
if __name__ == "__main__":
    while True:
        if startCounter==endCounter:
            startCounter = 0

        screen.fill(color[startCounter])

        startCounter+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        pygame.display.flip()
        clock.tick(5)
