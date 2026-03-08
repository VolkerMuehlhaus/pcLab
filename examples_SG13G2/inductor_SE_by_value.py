# Single ended inductor example

from pclab import *


################# create inductor ###############


tech = Technology("SG13G2.tech")

ind = inductorSE(tech)

sig_lay = "TopMetal2"
underpass_lay = "TopMetal1"

ind_geom = "octagon" # valid choices: "rect", "octagon"

if False:

    # CREATE MINIMUM DIAMETER INDUCTOR FOR GIVEN W,S,NTURNS
    w = 5.0
    s = 2.0
    nturns = 3.75

    d_outer = 0 # start from a diameter that is too small
    ind.setupGeometry(d_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)

    valid = ind.setupGeometry(d_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
    if not valid:
        print(f"Specified d_outer {d_outer} is too small, change to minimum possible diameter")
        d_outer = ind.get_min_diameter() # we can only call this *AFTER* setupGeometry()
        print(f"d_outer min={d_outer}")
        ind.setupGeometry(d_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)

    ind_name = "inductorSE_" + ind_geom + "_d_outer" + str(d_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
    ind.genGeometry()
    ind.genGDSII(ind_name + '.gds', structName = ind_name)

else:
    # CREATE INDUCTOR WITH TARGET VALUE
    Ltarget = 1000e-12
    w = 5.0
    s = 2.0
    nturns = 2

    d_outer = calculate_octa_diameter (nturns, w, s, Ltarget) 
    d_outer = math.ceil(d_outer*100)/100

    print(f"Target inductance {Ltarget*1e9} nH at N={nturns} w={w} s={s} => outer diameter {d_outer}")
    valid = ind.setupGeometry(d_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
    if valid:
        ind_name = "inductorSE_" + ind_geom + "_d_outer" + str(d_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
        ind.genGeometry()
        ind.genGDSII(ind_name + '.gds', structName = ind_name)
        print(f"Created output file {ind_name}.gds")
    else:
        d_outer_min = ind.get_min_diameter()
        print(f"Could not create layout, required d_outer {d_outer} is smaller than minimum possible value {d_outer_min}")

