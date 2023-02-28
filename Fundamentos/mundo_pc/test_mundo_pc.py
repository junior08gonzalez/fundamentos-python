from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

teclado_hp = Teclado("hp","usb")
raton_hp = Raton("hp","usb")
monitor_hp = Monitor("hp","15 pulgadas")
computadora_hp = Computadora("hp", monitor_hp, teclado_hp, raton_hp)

computadoras1 = [computadora_hp]
orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadora(computadora_hp)