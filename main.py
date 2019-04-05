import pygame
import random

pygame.init();

width = 800;
height = 600;
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()



G_constant = 10
particle_id_couter = 0
class particles:
    def __init__(self,x,y,mass,force_x,force_y):
        global particle_id_couter
        self.posx = x
        self.posy = y
        self.mass = mass
        self.force_x = force_x
        self.force_y = force_y
        particle_id_couter += 1
        self.particle_id= particle_id_couter
        
class universe:
    def __init__(self):
        self.particle_array = []
    def next_tick(self):
        
        self.s.fill((0,0,0))
        particle_index = 0
        self.s_pixel_array = pygame.PixelArray(self.s);
        for particle_c in self.particle_array:
            
            for particle_e in self.particle_array:
                if((particle_c.particle_id != particle_e.particle_id)&(particle_c.posx != particle_e.posx)&(particle_c.posy != particle_e.posy)):
                    r_x = particle_c.posx - particle_e.posx
                    r_y = particle_c.posy - particle_e.posy
                    R_MAG_s = (r_x*r_x+r_y*r_y)
                    F_MAG_x = -1*(G_constant*(particle_c.mass*particle_e.mass)/R_MAG_s)*r_x
                    F_MAG_y = -1*(G_constant*(particle_c.mass*particle_e.mass)/R_MAG_s)*r_y
                    particle_c.force_x += F_MAG_x
                    particle_c.force_y += F_MAG_y
            
            self.particle_array[(particle_index)].posx += 0.5*particle_c.force_x/particle_c.mass*0.01
            self.particle_array[(particle_index)].posy += 0.5*particle_c.force_y/particle_c.mass*0.01
            try:
                self.s_pixel_array[int(self.particle_array[(particle_index)].posx),int(self.particle_array[(particle_index)].posy)] = (255,255,255)
            except:
                self.particle_array.pop(particle_index)
                
        
            particle_index += 1
        self.s_pixel_array.close()
    def create_particle_array(self):


        colors = [(0,0,0),(255,255,255)]
        self.s = pygame.Surface((width,height));
        self.s_pixel_array = pygame.PixelArray(self.s);
        i = 0
        while i<width:
            j = 0
            while j<height:
                exist = random.randint(0,5000)
                if exist <1:
                    mass = random.randint(1,20000)
                    self.particle_array.append(particles(i,j,1,0,0))
                j = j + 1
            i = i + 1
        self.s_pixel_array.close()
    def particle_array_to_pixel_array(self):
        self.s_pixel_array = pygame.PixelArray(self.s);
        for particle in self.particle_array:

            self.s_pixel_array[int(particle.posx),int(particle.posy)] = (255,255,255)
        self.s_pixel_array.close()
u1 = universe()
u1.create_particle_array()
u1.particle_array_to_pixel_array()
screen.fill((255,255,255))
clock = pygame.time.Clock()
u1.particle_array.append(particles(400,300,100,0,0))
u1.particle_array.append(particles(350,300,1,0,0))
u1.particle_array.append(particles(550,300,1,0,0))
u1.particle_array.append(particles(250,300,1,0,0))
##u1.particle_array.append(particles(270,300,0.1,0,-50))
##u1.particle_array.append(particles(280,300,0.1,0,-50))
##u1.particle_array.append(particles(290,300,0.1,0,-50))
##u1.particle_array.append(particles(300,300,0.1,0,-50))

while 1:
    pygame.event.get()
    screen.blit(u1.s, (0, 0))
    pygame.display.flip() 
    clock.tick(100)
    u1.next_tick()
    screen.fill((0,0,0))
