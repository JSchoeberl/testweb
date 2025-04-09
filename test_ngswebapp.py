from webapp_client.app import App
from webapp_client.components import *
from webapp_client.qcomponents import *
from webapp_client.visualization import WebguiComponent

import micropip
await micropip.install("ngsolve")
import ngsolve as ngs
import ngsolve.webgui

gui = WebguiComponent(id="webgui")
gui2 = WebguiComponent(id="webgui2")

mesh = ngs.Mesh(ngs.unit_square.GenerateMesh(maxh=0.05))
f = ngs.Parameter(1)

def increment():
    f.Set(f.Get()+1)
    draw()

def draw():
    gui.draw(ngs.sin(2*ngs.pi*f*ngs.x), mesh, deformation=True, scale=0.3, redraw=True)
    gui2.draw(ngs.sin(2*ngs.pi*f*ngs.y), mesh, deformation=True, scale=0.3, redraw=True)    

gui.on_mounted(draw)

label = QBar("Joachim's first app")
b1 = QBtn("Inc Button", ui_outline=True).on_click(increment)

component = Centered(Row(label, b1), Row(gui, gui2) )
App(component)
