def find_amide_N(atom_list):
    amide_nitrogens = []
    amide_nitrogens_temp = []
    for atom_object in atom_list:
        if atom_object.element == ' C' and atom_object.hetatm_flag == True: # Make sure the C atom is on ligand
            N_count = 0
            O_count = 0
            C_count = 0
            for conected_atom in atom_object.conect:
                if conected_atom.hetatm_flag == True: # Make sure the conected atom is on ligand
                    if conected_atom.element == ' N':
                        N_count += 1
                        amide_nitrogens_temp.append(conected_atom)
                    if conected_atom.element == ' O':
                        O_count += 1
                    if conected_atom.element == ' C':
                        C_count += 1
            if N_count == 1 and O_count == 1 and C_count == 1:
                amide_nitrogens += amide_nitrogens_temp
            amide_nitrogens_temp = []
    return amide_nitrogens

def find_atoms_around(center_atoms, distance, atom_list):
    atoms_around = []
    for center_atom in center_atoms:
        for atom_object in atom_list:
            if (atom_object.x - center_atom.x)**2 + (atom_object.y - center_atom.y)**2 + (atom_object.z - center_atom.z)**2 <= distance**2:
                atoms_around.append(atom_object)
    return atoms_around

def glucarboxy_near_amide(atoms_around):
    for atom_around in atoms_around:
        if atom_around.residue == 'GLU': 
            if atom_around.name == ' OE1' or atom_around.name == ' OE2':
                return (True, atom_around)
    return (False, None)

def aspcarboxy_near_amide(atoms_around):
    for atom_around in atoms_around:
        if atom_around.residue == 'ASP':
            if atom_around.name == ' OD1' or atom_around.name == ' OD2':
                return (True, atom_around)
    return (False, None)