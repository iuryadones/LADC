# -*- coding: utf-8 -*-

#		Este programa simula o movimento do sistema Terra - Lua em torno do Sol.
#
#		Criado por: MSc. Thiago Freire de Oliveira
#
#		Data: 28/02/2018

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Importando as bibliotecas necessárias

from __future__ import division
from visual import *
from visual.graph import *
from math import *

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Criando o cenário

scene = display(title = "Planetas orbitando o Sol", width = 725, height = 725, range = (25000, 25000, 25000), center = (0, 0, 0))
scene.autoscale = True
marco = frame()

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Criando os planetas que vão orbitar o Sol

sol = sphere(pos=(0,0,0),radius=1e4,color = color.yellow, material = materials.marble)

terra = sphere(pos=(4e4,0,0),radius=2e3,material = materials.earth)
terra.trail=curve(color=terra.color)
terra.velocidade = vector(0,-10.,0)

lua = sphere(pos=(3e4+100,0,-100),radius=1e3,color=color.white)
lua.trail = curve(color=lua.color)
lua.velocidade = vector(0,-17,0)



while(True):

	rate(500)

	# Força gravitacional - SOL / TERRA

	Rst = sol.pos - terra.pos
	ust = Rst/mag(Rst)
	Fst = 3e6*ust/(mag(Rst)**2)
	terra.velocidade += Fst
	terra.pos += terra.velocidade
	terra.trail.append(terra.pos)
	
	# Força gravitacional - TERRA / LUA - SOL / LUA

	Rtl = terra.pos - lua.pos
	utl = Rtl/mag(Rtl)
	Ftl = 3.5e6*utl/(mag(Rtl)**2)

	Rsl = sol.pos - lua.pos
	usl = Rsl/mag(Rsl)
	Fsl = 9e2*usl/(mag(Rsl)**2)

	lua.velocidade += Fsl + Ftl
	lua.pos += lua.velocidade
	lua.trail.append(lua.pos)
	print(Fst,Ftl,Fsl)





