# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:12:57 2021

@author: 86159
"""

from pymatgen import MPRester, Composition, Element
from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import PhaseDiagram, CompoundPhaseDiagram
from pymatgen.analysis.phase_diagram import PDPlotter
from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.util.plotting import pretty_plot 
import json
import re
import palettable
import matplotlib as mpl
import json
import re
import palettable

vasprun = Vasprun(r"...\vasprun.xml")

entry = vasprun.get_computed_entry(inc_structure=True)  
rester = MPRester('API KEY')

element_list= [i.symbol for i in list(set(entry.structure.species))]
mp_entries = a.get_entries_in_chemsys([element_list], compatible_only=(False))

compatibility = MaterialsProjectCompatibility()
entry = compatibility.process_entry(entry)
entries = compatibility.process_entries([entry] + mp_entries)
    
    
pd = PhaseDiagram(entries)


# electrochemical stability
li_entries = [e for e in entries if e.composition.reduced_formula == "Li"]
uli0 = min(li_entries, key=lambda e: e.energy_per_atom).energy_per_atom
el_profile = pd.get_element_profile(Element("Li"), entry.composition)
for i, d in enumerate(el_profile):
    voltage = -(d["chempot"] - uli0)
    print("Voltage: %s V" % voltage)
    print(d["reaction"])
    print("")


# using matplotlib to plot the profile
mpl.rcParams['axes.linewidth']=3
mpl.rcParams['lines.markeredgewidth']=4
mpl.rcParams['lines.linewidth']=3
mpl.rcParams['lines.markersize']=15
mpl.rcParams['xtick.major.width']=3
mpl.rcParams['xtick.major.size']=8
mpl.rcParams['xtick.minor.width']=3
mpl.rcParams['xtick.minor.size']=4
mpl.rcParams['ytick.major.width']=3
mpl.rcParams['ytick.major.size']=8
mpl.rcParams['ytick.minor.width']=3
mpl.rcParams['ytick.minor.size']=4


colors = palettable.colorbrewer.qualitative.Set1_9.mpl_colors
plt = pretty_plot(12, 8) 

for i, d in enumerate(el_profile):
    v = - (d["chempot"] - uli0)
    if i != 0:
        plt.plot([x2, x2], [y1, d["evolution"] / 4.0], 'k', linewidth=3)
    x1 = v
    y1 = d["evolution"] / 4.0
    if i != len(el_profile) - 1:
        x2 = - (el_profile[i + 1]["chempot"] - uli0)
    else:
        x2 = 5.0
        
    if i in [0, 4, 5, 7]:
        products = [re.sub(r"(\d+)", r"$_{\1}$", p.reduced_formula)                     
                    for p in d["reaction"].products if p.reduced_formula != "Li"]

        if i == 5: # For font-height adjustment.
            xy = (v + 0.04, y1 + 0.5)
        else:
            xy = (v + 0.04, y1 + 0.5)
        plt.annotate(", ".join(products), xy, 
                     fontsize=25, family = 'Arial', color=colors[0])
        
        plt.plot([x1, x2], [y1, y1], color=colors[0], linewidth=3)
    else:
        plt.plot([x1, x2], [y1, y1], 'k', linewidth=3)  

plt.xlim((0, 2.0)) 
plt.ylim((-20, 15))

plt.xlabel("Voltage (V)",font1)
plt.ylabel("Li consumption (/f.u.)",font1)

plt.tight_layout() 

