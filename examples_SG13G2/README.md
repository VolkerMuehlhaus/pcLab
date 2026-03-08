# IHP SG13G2 technology for pcLab - Passive Component Lab
pcLab is a collection of Python classes that generate GDSII layouts of integrated passive structures such as inductors and baluns. It can be installed by running
`pip install .`
in the top level directory.

## Technology file

This directory contains the layout technology configuration file `SG13G2.tech` for IHP SG13G2:
- layer names and their GDSII layer numbers
- via dimensions (size, spacing, enclosure)

as described in the IHP process specification: https://github.com/IHP-GmbH/IHP-Open-PDK/blob/main/ihp-sg13g2/libs.doc/doc/SG13G2_os_process_spec.pdf

## Example for creating inductor layout

A small example on how to generate two inductor layouts:

``` python
# Symmetric octagon and square inductor example
from pclab import *

tech = Technology("SG13G2.tech")

ind = inductorSym(tech)

r_outer = 200.0
w = 8.0
s = 2.0
nturns = 2.0
sig_lay = "TopMetal2"
underpass_lay = "TopMetal1"

# Generate symmetric octagon inductor
ind_geom = "octagon" # valid choices: "rect", "octagon"
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
ind_name = "inductorSym_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)

# Generate symmetric square inductor
ind_geom = "rect" # valid choices: "rect", "octagon"
ind.setupGeometry(r_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
ind_name = "inductorSym_" + ind_geom + "_r_outer" + str(r_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
ind.genGeometry()
ind.genGDSII(ind_name + '.gds', structName = ind_name)
```
Other examples on supported layout generators are in the `examples_SG13G2` directory.

## Example for creating inductor layout by value

The original pclab library was created to draw geometries from specified width, spacing and diameter. 
By adding the `indcalc.py` functions, it is also possible to create an inductor shape for a given target value. 
To so so, the user specifies width, spacing, number of turns and a target value, and function

``` python
diameter = calculate_inductor_diameter (N, w, s, Ltarget, K1, K2, L0)
```

will return the required outer diameter. This can then be checked against the minimum possible diameter for the given inductor layout, and drawn if valid.

An example for such inductor design by target value can be found in SG13G2 examples `inductor_SE_by_value.py` and `inductor_Sym_by_value.py`


``` python
from pclab import *
import math


################# create inductor ###############

tech = Technology("SG13G2.tech")
ind = inductorSym(tech)

sig_lay = "TopMetal2"
underpass_lay = "TopMetal1"

# CREATE INDUCTOR WITH TARGET VALUE
Ltarget = 1000e-12
w = 5.0
s = 2.0
nturns = 2
ind_geom = "octagon" # valid choices: "rect", "octagon"

d_outer = calculate_octa_diameter (nturns, w, s, Ltarget) 
d_outer = math.ceil(d_outer*100)/100

print(f"Target inductance {Ltarget*1e9} nH at N={nturns} w={w} s={s} => outer diameter {d_outer}")
valid = ind.setupGeometry(d_outer, w, s, nturns, sig_lay, underpass_lay, ind_geom)
if valid:
    ind_name = "inductorSym_" + ind_geom + "_d_outer" + str(d_outer) + "_w" +  str(w) + "_n" + str(nturns) + "_s" + str(s)
    ind.genGeometry()
    ind.genGDSII(ind_name + '.gds', structName = ind_name)
    print(f"Created output file {ind_name}.gds")
else:
    d_outer_min = ind.get_min_diameter()
    print(f"Could not create layout, required d_outer {d_outer} is smaller than minimum possible value {d_outer_min}")

```