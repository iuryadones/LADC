# -*- coding: utf-8 -*-

#		Este programa simula o movimento dos planetas em torno do Sol.
#
#		Criado por: MSc. Thiago Freire de Oliveira
#
#		Data: 17/02/2018

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Importando as bibliotecas necessárias

from __future__ import division
from visual import *
from visual.graph import *
from math import *

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Criando o cenário

scene = display(title = "Planetas orbitando o Sol", width = 725, height = 725,range=(25000,25000,25000),center=(100,100,100))
scene.autoscale = True

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Criando os planetas que vão orbitar o Sol

sol = sphere(pos=(20, 0, 0), radius = 200, color = color.yellow,material=materials.marble)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
mercurio = sphere(pos=(500, 0, 0), radius = 20, color = color.gray(.5), material = materials.marble)
mercurio.trail = curve(color = mercurio.color)
mercurio.velocidade = vector(0,-13,0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
venus = sphere(pos=(700, 0, 0), radius = 35, color = color.orange, material = materials.marble)
venus.trail = curve(color = venus.color)
venus.velocidade = vector(0,-12,0)
#----------------------------------------------------------------------------------------------------------------------------------------------------
terra = sphere(pos=(900, 0, 0), radius = 39, material = materials.earth)
terra.trail = curve(color = terra.color)
terra.velocidade = vector(0,-11,0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#lua = sphere(pos=(950, 0, 0), radius = 10, color = color.white, material = materials.marble)
#lua.trail = curve(color = lua.color)
#lua.velocidade = vector(0,-15,0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
marte = sphere(pos=(1200, 0, 0), color = color.red, radius = 29, material = materials.marble)
marte.trail = curve(color = marte.color)
marte.velocidade = vector(0,-10,0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
jupiter = sphere(pos=(1800, 0, 0), color = color.orange, radius = 120, material = materials.marble)
jupiter.trail = curve(color = jupiter.color)
jupiter.velocidade = vector(0,-8,0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
saturno = sphere(pos=(2300, 0, 0), color = color.yellow, radius = 100, material = materials.marble)
saturno.trail = curve(color = saturno.color)
saturno.velocidade = vector(0,-7,0)

anel1 = ring(pos=saturno.pos, color=color.white, radius = 110, thickness = 1,axis = (-1,1,0))
anel1.velocidade = saturno.velocidade
anel2 = ring(pos=saturno.pos, color=color.white, radius = 115, thickness = 1,axis = (-1,1,0))
anel2.velocidade = saturno.velocidade
anel3 = ring(pos=saturno.pos, color=color.white, radius = 120, thickness = 1,axis = (-1,1,0))
anel3.velocidade = saturno.velocidade
anel4 = ring(pos=saturno.pos, color=color.white, radius = 125, thickness = 1,axis = (-1,1,0))
anel4.velocidade = saturno.velocidade
anel5 = ring(pos=saturno.pos, color=color.white, radius = 130, thickness = 1,axis = (-1,1,0))
anel5.velocidade = saturno.velocidade
anel6 = ring(pos=saturno.pos, color=color.white, radius = 135, thickness = 1,axis = (-1,1,0))
anel6.velocidade = saturno.velocidade
anel7 = ring(pos=saturno.pos, color=color.white, radius = 140, thickness = 1,axis = (-1,1,0))
anel7.velocidade = saturno.velocidade
anel8 = ring(pos=saturno.pos, color=color.white, radius = 145, thickness = 1,axis = (-1,1,0))
anel8.velocidade = saturno.velocidade
anel9 = ring(pos=saturno.pos, color=color.white, radius = 150, thickness = 1,axis = (-1,1,0))
anel9.velocidade = saturno.velocidade
anel10 = ring(pos=saturno.pos, color=color.white, radius = 155, thickness = 1,axis = (-1,1,0))
anel10.velocidade = saturno.velocidade
#-----------------------------------------------------------------------------------------------------------------------------------------------------
urano = sphere(pos=(2700, 0, 0), color = color.blue, radius = 90, material = materials.marble)
urano.trail = curve(color = urano.color)
urano.velocidade = vector(0,-5,0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
netuno = sphere(pos=(3400, 0, 0), color = color.green, radius = 85, material = materials.marble)
netuno.trail = curve(color = netuno.color)
netuno.velocidade = vector(0,-4,0)
#------------------------------------

while(True):

# Definições dos movimentos planetários

	rate(30)
#-----------------------------------------------------------------------------------------------------------------------------------------------------	
#	sol.rotate(angle=(radians(1)),axis=(0,1,0))
#-----------------------------------------------------------------------------------------------------------------------------------------------------	
	Rm = sol.pos - mercurio.pos
	um = Rm/mag(Rm)
	Fm = 1.0e5*um/mag(Rm)**2
	mercurio.velocidade += Fm
	mercurio.pos += mercurio.velocidade
	mercurio.rotate(angle=(radians(10)),axis=(0,0,1))
	mercurio.trail.append(pos = mercurio.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------	
	Rv = sol.pos - venus.pos
	uv = Rv/mag(Rv)
	Fv = 1.0e5*uv/mag(Rv)**2
	venus.velocidade += Fv
	venus.pos += venus.velocidade
	venus.rotate(angle=(radians(10)),axis=(0,0,1))
	venus.trail.append(pos = venus.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
	Rt = sol.pos - terra.pos
	ut = Rt/mag(Rt)
	Ft = 1.0e5*ut/mag(Rt)**2
	terra.velocidade += Ft
	terra.pos += terra.velocidade
	terra.rotate(angle=(radians(10)))
	terra.trail.append(pos = terra.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------	
#	Rl = terra.pos - lua.pos
#	ul = Rl/mag(Rl)
#	Fl = 1.2e3*ul/mag(Rl)**2
#	lua.velocidade += Fl
#	lua.pos += lua.velocidade
#	lua.rotate(angle=(radians(10)),axis=(0,1,0))
#	lua.trail.append(pos = lua.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------	
	Rma = sol.pos - marte.pos
	uma = Rma/mag(Rma)
	Fma = 1.0e5*uma/mag(Rma)**2
	marte.velocidade += Fma
	marte.pos += marte.velocidade
	marte.rotate(angle=(radians(10)),axis=(0,0,1))
	marte.trail.append(pos = marte.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
	Rj = sol.pos - jupiter.pos
	uj = Rj/mag(Rj)
	Fj = 1.0e5*uj/mag(Rj)**2
	jupiter.velocidade += Fj
	jupiter.pos += jupiter.velocidade
	jupiter.rotate(angle=(radians(10)),axis=(0,0,1))
	jupiter.trail.append(pos = jupiter.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
	Rs = sol.pos - saturno.pos
	us = Rs/mag(Rs)
	Fs = 1.0e5*us/mag(Rs)**2
	saturno.velocidade += Fs
	saturno.pos += saturno.velocidade
	saturno.rotate(angle=(radians(10)),axis=(0,0,1))
	saturno.trail.append(pos = saturno.pos)
	
	for i in [anel1,anel2,anel3,anel4,anel5,anel6,anel7,anel8,anel9,anel10]:
		i.pos = saturno.pos
#-----------------------------------------------------------------------------------------------------------------------------------------------------
	Ru = sol.pos - urano.pos
	uu = Ru/mag(Ru)
	Fu = 6e4*uu/mag(Ru)**2
	urano.velocidade += Fu
	urano.pos += urano.velocidade
	urano.rotate(angle=(radians(10)),axis=(0,0,1))
	urano.trail.append(pos = urano.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
	Rn = sol.pos - netuno.pos
	un = Rn/mag(Rn)
	Fn = 5e4*un/mag(Rn)**2
	netuno.velocidade += Fn
	netuno.pos += netuno.velocidade
	netuno.rotate(angle=(radians(10)),axis=(0,0,1))
	netuno.trail.append(pos = netuno.pos)
#-----------------------------------------------------------------------------------------------------------------------------------------------------




















