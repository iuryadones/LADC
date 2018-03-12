# -*- coding: utf-8 -*-

from __future__ import division, print_function
from vpython import *
from math import *


scene = canvas(title="Planetas orbitando o Sol",
               width=725, height=725,
               range=(25000,25000,25000))

scene.autoscale = True

sol = sphere(pos=vec(20,0,0),
             radius=200,
             color=color.yellow)

mercurio = sphere(pos=vec(500,0,0),
                  radius=20,
                  color=color.gray(.5))

venus = sphere(pos=vec(700,0,0),
               radius=35,
               color=color.orange)

terra = sphere(pos=vec(900,0,0),
               radius=39)

#lua = sphere(pos=vec(950,0,0),
#             radius=10,
#             color=color.white)

marte = sphere(pos=vec(1200,0,0),
               color=color.red,
               radius=29)

jupiter = sphere(pos=vec(1800,0,0),
                 color=color.orange,
                 radius=120)

saturno = sphere(pos=vec(2300,0,0),
                 color=color.yellow,
                 radius=100)

urano = sphere(pos=vec(2700,0,0),
               color=color.blue,
               radius=90)

netuno = sphere(pos=vec(3400,0,0),
                color=color.green,
                radius=85)

mercurio.velocidade = vec(0,-13,0)
venus.velocidade = vec(0,-12,0)
terra.velocidade = vec(0,-11,0)
#lua.velocidade = vec(0,-15,0)
marte.velocidade = vec(0,-10,0)
jupiter.velocidade = vec(0,-8,0)
saturno.velocidade = vec(0,-7,0)
urano.velocidade = vec(0,-5,0)
netuno.velocidade = vec(0,-4,0)

anel_kwargs = dict(pos=saturno.pos,
                  color=color.white,
                  thickness=1,
                  axis=vec(-1,1,0))

aneis_saturno = [ring(radius=(110+l), **anel_kwargs) for l in range(5,60)]

for i in range(len(aneis_saturno)):
    aneis_saturno[i].velocidade = saturno.velocidade

while True:

    rate(30)
    sol.rotate(angle=(radians(1)),axis=vec(0,1,0))

    Rm = sol.pos - mercurio.pos
    um = Rm/mag(Rm)
    Fm = 1.0e5*um/mag(Rm)**2
    mercurio.velocidade += Fm
    mercurio.pos += mercurio.velocidade
    mercurio.rotate(angle=(radians(10)),axis=vec(0,1,0))

    Rv = sol.pos - venus.pos
    uv = Rv/mag(Rv)
    Fv = 1.0e5*uv/mag(Rv)**2
    venus.velocidade += Fv
    venus.pos += venus.velocidade
    venus.rotate(angle=(radians(10)),axis=vec(0,1,0))

    Rt = sol.pos - terra.pos
    ut = Rt/mag(Rt)
    Ft = 1.0e5*ut/mag(Rt)**2
    terra.velocidade += Ft
    terra.pos += terra.velocidade
    terra.rotate(angle=(radians(10)),axis=vec(0,1,0))

#    Rl = terra.pos - lua.pos
#    ul = Rl/mag(Rl)
#    Fl = 1.2e3*ul/mag(Rl)**2
#    lua.velocidade += Fl
#    lua.pos += lua.velocidade
#    lua.rotate(angle=(radians(10)),axis=vec(0,1,0))
#    lua.trail.append(pos = lua.pos)

    Rma = sol.pos - marte.pos
    uma = Rma/mag(Rma)
    Fma = 1.0e5*uma/mag(Rma)**2
    marte.velocidade += Fma
    marte.pos += marte.velocidade
    marte.rotate(angle=(radians(10)),axis=vec(0,1,0))

    Rj = sol.pos - jupiter.pos
    uj = Rj/mag(Rj)
    Fj = 1.0e5*uj/mag(Rj)**2
    jupiter.velocidade += Fj
    jupiter.pos += jupiter.velocidade
    jupiter.rotate(angle=(radians(10)),axis=vec(0,1,0))

    Rs = sol.pos - saturno.pos
    us = Rs/mag(Rs)
    Fs = 1.0e5*us/mag(Rs)**2
    saturno.velocidade += Fs
    saturno.pos += saturno.velocidade
    saturno.rotate(angle=(radians(10)),axis=vec(0,1,0))

    for i in range(len(aneis_saturno)):
        aneis_saturno[i].pos = saturno.pos

    Ru = sol.pos - urano.pos
    uu = Ru/mag(Ru)
    Fu = 6e4*uu/mag(Ru)**2
    urano.velocidade += Fu
    urano.pos += urano.velocidade
    urano.rotate(angle=(radians(10)),axis=vec(0,1,0))

    Rn = sol.pos - netuno.pos
    un = Rn/mag(Rn)
    Fn = 5e4*un/mag(Rn)**2
    netuno.velocidade += Fn
    netuno.pos += netuno.velocidade
    netuno.rotate(angle=(radians(10)),axis=vec(0,1,0))

