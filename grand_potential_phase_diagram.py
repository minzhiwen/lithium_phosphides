# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:37:43 2020

@author: 86159
"""
from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter, GrandPotentialPhaseDiagram
from pymatgen import Composition,Element,MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility


vasprun = Vasprun(r"...\vasprun.xml")

entry = vasprun.get_computed_entry(inc_structure=True)

a = MPRester('API KEY')

element_list= [i.symbol for i in list(set(entry.structure.species))]
mp_entries = a.get_entries_in_chemsys([element_list], compatible_only=(False))

compatibility = MaterialsProjectCompatibility()
entry = compatibility.process_entry(entry)
entries = compatibility.process_entries([entry] + mp_entries)

pd = PhaseDiagram(entries)

grand = True
if grand:
    open_el = 'Li'
    relative_mu = -0.15  

if grand:
    mu = pd.get_transition_chempots(Element(open_el))[0]
    chempots = {open_el: relative_mu + mu}
    gpd = GrandPotentialPhaseDiagram(entries, chempots)
plotter = PDPlotter(gpd, show_unstable=True) 
plotter.show()

