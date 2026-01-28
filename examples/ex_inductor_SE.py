# Copyright 2026 Dušan Grujić (dusan.grujic@etf.bg.ac.rs)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Single ended inductor example
from pclab import *


tech = Technology("generic_5M.tech")

ind = inductorSE(tech)

r_outer = 200.0
w = 8.0
s = 2.0
nturns = 2.0
sig_lay = "M5"
underpass_lay = "M4"
ind_geom = "octagon" # valid choices: "rect", "octagon"

subRingSpace = 20.0
subRingW = 6.0
diffLayer = "diff"
implantLayer = "pimpl"

# Generate regular layout
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
ind_name = "inductorSE_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

# Now generate layout with merged vias for faster EM simulation    
ind.setEmVias(True)
ind_name = "inductorSE_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s) + "_emvias"
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

# Generate new inductor with diffusion ring
ind.setEmVias(False)
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom, subRingSpace = subRingSpace, subRingW = subRingW, diffLayer = diffLayer, implantLayer = implantLayer)
ind_name = "inductorSE_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s) + "_subring"
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

# Generate new square inductor
ind_geom = "rect" # valid choices: "rect", "octagon"
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
ind_name = "inductorSE_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

# Generate new inductor with diffusion ring
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom, subRingSpace = subRingSpace, subRingW = subRingW, diffLayer = diffLayer, implantLayer = implantLayer)
ind_name = "inductorSE_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s) + "_subring"
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)


