# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:57:31 2021

@author: 86159
"""

from pymatgen.ext.matproj import MPRester
from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen import Composition
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
vasprun = Vasprun(r"...\vasprun.xml")

entry = vasprun.get_computed_entry(inc_structure=True)

a = MPRester('API KEY')


element_list= [i.symbol for i in list(set(entry.structure.species))]
mp_entries = a.get_entries_in_chemsys([element_list], compatible_only=(False))


compatibility = MaterialsProjectCompatibility()
entry = compatibility.process_entry(entry)
entries = compatibility.process_entries([entry] + mp_entries)

# phase diagram  
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd, show_unstable=True)
plotter.show()


# Ehull
ehull = pd.get_e_above_hull(entry)
print("The energy above hull is %.3f eV/atom." % ehull)


