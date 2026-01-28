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

r_outer = 400.0
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
balun.setupGeometry(r_outer, w, w, 0.0, sig_lay, underpass_lay, "M3", s)
balun_name = "balun2x1_broadsidecoupled_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)

# Generate balun 1x1 broad side
balun = balun1x1_broadsidecoupled(tech)
balun.setupGeometry(r_outer, w, w, 0, sig_lay, underpass_lay)
balun_name = "balun1x1_broadsidecoupled_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_s" + str(s)
balun.genGeometry()
balun.genGDSII(balun_name + '.gds', structName = balun_name)
