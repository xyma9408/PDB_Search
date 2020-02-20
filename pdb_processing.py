class ATOM():
    # define a class called atom
    # attributes include coordinates, element, serial numbers, conectivity, residue it belongs
    def __init__(self, x, y, z, element, name, id, residue, resseq, hetatm_flag):
        self.x = x
        self.y = y
        self.z = z
        self.element = element
        self.id = id
        self.residue = residue
        self.conect = []
        self.name = name
        self.resseq = resseq
        self.hetatm_flag = hetatm_flag

    def print_atom(self):
        print(self.id.strip() + ' ' + self.element.strip() + ' ' + self.residue.strip() + ' ' + self.resseq.strip() + ' ' + self.name.strip() + '\n')

    def output_atom(self):
        return self.id.strip() + ' ' + self.element.strip() + ' ' + self.residue.strip() + ' ' + self.resseq.strip() + ' ' + self.name.strip() + '\n'

def read_pdb_file(path):
    atoms = []
    conects = []
    hetatms = []
    with open(path, 'r') as file_name:
        for line in file_name:
            if line[0:6] == 'ATOM  ':
                atoms.append(line)
            if line[0:6] == 'CONECT':
                conects.append(line)
            if line[0:6] == 'HETATM':
                hetatms.append(line)
    return atoms, conects, hetatms

def create_atom_list(path):
    """Combine the ATOM and CONECT information of a PDB file in a list"""
    """Each element in the list is an instance of ATOM class"""
    atom_list = []
    pdbfile = read_pdb_file(path)
    atoms = pdbfile[0]
    conects = pdbfile[1]
    hetatms = pdbfile[2]
    for atom in atoms:
        x = float(atom[30:38])
        y = float(atom[38:46])
        z = float(atom[46:54])
        element = atom[76:78]
        name = atom[12:16]
        id = atom[6:11]
        residue = atom[17:20]
        resseq = atom[22:26]
        atom_list.append(ATOM(x, y, z, element, name, id, residue, resseq, False))
    for hetatm in hetatms:
        x = float(hetatm[30:38])
        y = float(hetatm[38:46])
        z = float(hetatm[46:54])
        element = hetatm[76:78]
        name = hetatm[12:16]
        id = hetatm[6:11]
        residue = hetatm[17:20]
        resseq = hetatm[22:26]
        atom_list.append(ATOM(x, y, z, element, name, id, residue, resseq, True))
    for conect in conects:
        for atom_object in atom_list:
            if atom_object.id == conect[6:11]:#Conect line of target atom located
                for atom_object2 in atom_list:
                    if atom_object2.id.strip() in conect.split()[2:]:
                        atom_object.conect.append(atom_object2)
    return atom_list

