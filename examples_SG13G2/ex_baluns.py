# Single ended inductor example
from pclab import *

tech = Technology("SG13G2.tech")

r_outer = 300.0
w = 8.0
s = 2.0
nturns = 3.0
sig_lay = "TopMetal2"
underpass_lay = "TopMetal1"
secondary_lay= "Metal5"
ind_geom = "octagon" # valid choices: "rect", "octagon"

# Generate balun 4x3
balun = balun4x3(tech)
balun.setupGeometry(r_outer, w, s, sig_lay, underpass_lay, ind_geom)
balun_name = "balun4x3_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) +  "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)


# Generate balun 2x2
balun = balun2x2(tech)
balun.setupGeometry(r_outer, w, s, sig_lay, underpass_lay, ind_geom)
balun_name = "balun2x2_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) +  "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)

# Generate balun 6x3
balun = balun6x3(tech)
balun.setupGeometry(r_outer, w, s, sig_lay, underpass_lay, ind_geom)
balun_name = "balun6x3_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) +  "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)

# Generate balun 2x1 edge coupled
balun = balun2x1_edgecoupled(tech)
balun.setupGeometry(r_outer, w, s, sig_lay, underpass_lay, ind_geom)
balun_name = "balun2x1_edgecoupled_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)

# Generate balun 2x1 broad side
balun = balun2x1_broadsidecoupled(tech)
balun.setupGeometry(r_outer, w, w, 0.0, sig_lay, underpass_lay, secondary_lay, s)
balun_name = "balun2x1_broadsidecoupled_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)


# Generate balun 1x1 broad side
balun = balun1x1_broadsidecoupled(tech)
balun.setupGeometry(r_outer, w, w, 0, sig_lay, underpass_lay)
balun_name = "balun1x1_broadsidecoupled_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)
