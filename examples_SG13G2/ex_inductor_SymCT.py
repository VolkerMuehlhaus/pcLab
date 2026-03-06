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

tech = Technology("SG13G2.tech")

ind = inductorSymCT(tech)

r_outer = 200.0
w = 8.0
s = 2.0
nturns = 2.0
sig_lay = "TopMetal2"
underpass_lay = "TopMetal1"
ind_geom = "octagon" # valid choices: "rect", "octagon"


ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, underpass_lay, ind_geom)
ind_name = "inductorSymCT_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

