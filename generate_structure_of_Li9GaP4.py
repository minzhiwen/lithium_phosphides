# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:00:02 2021

@author: 86159
"""

from pymatgen import Structure,Lattice
from pymatgen.transformations.standard_transformations import OrderDisorderedStructureTransformation
from pymatgen.io.vasp.sets import batch_write_input, MPRelaxSet
from pymatgen.symmetry.groups import SpaceGroup
import pymatgen as mg

lattice = mg.Lattice.cubic(11.8624)
specie1 = {"Ga3+":1}
specie2 = {"Ga3+":1}
specie3 = {"P3-":1}
specie4 = {"P3-":1}
specie5 = {"Li+":1}  
specie6 = {"Li+":1}
specie7= {"Li+":2/3}
specie8 = {"Li+":1}
specie9 = {"Li+":1}
specie10 = {"Li+":25/36}
specie11 = {"Li+":0.25}

SpaceGroup.int_number = 218
structure = Structure.from_spacegroup(218,lattice, 
                                      [specie1,specie2,specie3,specie4,specie5,specie6,specie7,specie8,specie9,specie10,specie11], 
                                      [[0,0,0],[0.5,0.25,0],[0.11884,0.11884,0.11884],[0.37612,0.36764,0.11741],[0.5,0.5,0],[0.25,0.5,0],[0.2480,0.2480,0.2480],[0.2543,0,0],[0.4968,0.2609,0.2527],[0.3369,0.5830,0.0907],[0.343,0.343,0.343]])


