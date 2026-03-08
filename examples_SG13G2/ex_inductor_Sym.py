# Symmetric ended inductor example
from pclab import *


tech = Technology("SG13G2.tech")

ind = inductorSym(tech)

r_outer = 200.0
w = 8.0
s = 2.0
nturns = 2.0
sig_lay = "TopMetal2"
underpass_lay = "TopMetal1"
ind_geom = "octagon" # valid choices: "rect", "octagon"

subRingSpace = 20.0
subRingW = 6.0
diffLayer = "Activ"
implantLayer = "pimpl"

# Generate regular layout
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
ind_name = "inductorSym_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)


# Now generate layout with merged vias for faster EM simulation    
ind.setEmVias(True)
ind_name = "inductorSym_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s) + "_emvias"
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

# Generate new square inductor
ind_geom = "rect" # valid choices: "rect", "octagon"
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
ind_name = "inductorSym_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

# Generate new inductor with diffusion ring
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom, subRingSpace = subRingSpace, subRingW = subRingW, diffLayer = diffLayer, implantLayer = implantLayer)
ind_name = "inductorSym_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s) + "_subring"
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)


