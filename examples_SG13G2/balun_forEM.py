# Single ended inductor example

from pclab import *
import math

tech = Technology("SG13G2.tech")

w = 4.0
s = 2.0
nturns = 3.0
sig_lay = "TopMetal1"
underpass_lay = "Metal5"
secondary_lay= "TopMetal2"
ind_geom = "octagon" # valid choices: "rect", "octagon"


d_outer = 0 # start from a diameter that is too small

# Generate balun 
balun = balun2x1_broadsidecoupled(tech)
# valid = balun.setupGeometry(d_outer, w, s, sig_lay, underpass_lay, ind_geom)
valid = balun.setupGeometry(d_outer, w, w, 0.0, sig_lay, underpass_lay, secondary_lay, s, ind_geom)
                            
if not valid:
    print(f"Specified d_outer {d_outer} is too small, change to minimum possible diameter")
    d_outer = balun.get_min_diameter()
    print(f"=> changed to d_outer min={d_outer}")
    #balun.setupGeometry(d_outer, w, s, sig_lay, underpass_lay, ind_geom)
    valid = balun.setupGeometry(d_outer, w, w, 0.0, sig_lay, underpass_lay, secondary_lay, s, ind_geom)

balun_name = f"{type(balun).__name__}_{ind_geom}_do{d_outer}_w{w}_s{s}"
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)
print('Created file ',balun_name + '.gds')




