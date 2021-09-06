import pygame

pygame.init()
class Casa:
	def __init__(self,traco,ref_x,ref_y, tela):
		self.tela = tela
		self.ref_x = ref_x
		self.ref_y = ref_y
		self.traco = traco
		self.vel_x = 1
		self.vel_y = 1
		
	def desenha(self):		
					
		#Desenhar trangulo
		pygame.draw.polygon(self.tela,(255,255,0),[(self.ref_x,self.ref_y),(self.ref_x+ self.traco,self.ref_y),(self.ref_x+self.traco/2,self.ref_y-self.traco)],5)
			
			#Desenhar frente
		pygame.draw.rect(self.tela,(255,255,0),(self.ref_x+self.traco,self.ref_y,self.traco,self.traco),5)
			
			#Desenhar lado
		pygame.draw.rect(self.tela,(255,255,0),(self.ref_x,self.ref_y,self.traco,self.traco),5)
			
			#Desenhar teto
		pygame.draw.polygon(self.tela,(255,255,0),[(self.ref_x+self.traco,self.ref_y),(self.ref_x+2*self.traco,self.ref_y),(self.ref_x+self.traco*1.55,self.ref_y-self.traco),(self.ref_x+ self.traco/2,self.ref_y-self.traco)],5)
		
		#Desenhar porta	
		pygame.draw.rect(self.tela,(255,255,0),(self.ref_x +self.traco/4,self.ref_y+self.traco/4,self.traco/4,self.traco*0.75),0)
		
		#Desenhar Janela	
		pygame.draw.rect(self.tela,(255,255,0),(self.ref_x +self.traco*1.25,self.ref_y+self.traco/4,self.traco/4,self.traco/4),0)
		
						
	def movimenta(self):				
		self.ref_x = self.ref_x +self.vel_x
		self.ref_y = self.ref_y + self.vel_y
			
		if self.ref_x + self.traco > 800:
			self.vel_x = -1
		if self.ref_x - self.traco < 0:
			self.vel_x= 1
				
		if self.ref_y - self.traco> 400:
			self.vel_y = -1
		
		if self.ref_y - self.traco< 0:
			self.vel_y= 1


#Loop do Jogo

#Inicializacao						
tela = pygame.display.set_mode((800,400),0)	
			
casa1 = Casa(100,50,100,tela)
casa2 = Casa(75,200,200,tela)
casa3 = Casa(50,300,300,tela)
casa4 = Casa(50,400,400,tela)
							
while True:
#Regras	
	casa1.movimenta()
	casa2.movimenta()
	casa3.movimenta()		
	casa4.movimenta()

#pinta na tela				
	tela.fill((0,0,0))
	casa1.desenha()
	casa2.desenha()
	casa3.desenha()	
	casa4.desenha()			
				
	pygame.display.update()

#					
		
#Finalizacao				
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()		