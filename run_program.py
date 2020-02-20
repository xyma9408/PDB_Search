from pdb_processing import *
import find_amide as fa
from download import *
import os
import datetime

"""
def run_find_atoms_around_amide(path):
    distance = int(input('input the distance:'))
    atom_list = create_atom_list(path)
    amide_nitrogens = fa.find_amide_N(atom_list)
    atoms_around = fa.find_atoms_around(amide_nitrogens, distance, atom_list)
    for atom_around in atoms_around:
        atom_around.print_atom()

def run_find_amide_N(path):
    atom_list = create_atom_list(path)
    amide_nitrogens = fa.find_amide_N(atom_list)
    for amide_nitrogen in amide_nitrogens:
        amide_nitrogen.print_atom()

def run_program():
    while True:
        sele = input('Choose what to do: \n' + '1. Find atoms around amide nitrogens\n' + '2. Find amide nitrogens\n' + '3. Quit\n' )
        if sele == '3':
            break
        elif sele == '1':
            path = input('input path of PDB file here: ')
            run_find_atoms_around_amide(path)
        elif sele == '2':
            path = input('input path of PDB file here: ')
            run_find_amide_N(path)

run_program()
"""

def run_program():
    starttime = datetime.datetime.now()
    distance = 4 #This is the distance within which Glu or Asp should be around amide
    num = int(input("Input number of inqueries: "))
    initial_id = input("Input starting PDB id: ")
    dir = input("Input the directory to save result: ")
    with open(dir + '/Results.txt', 'w+') as result_file:
        pdb_ids = create_pdb_ids(num, initial_id)
        for pdb_id in pdb_ids:
            #download a PDB file
            url = 'https://files.rcsb.org/download/' + pdb_id + '.pdb'
            path = dir + '/' + pdb_id + '.pdb'
            status = download_pdb(url, path)
            if status == 'ERROR':
                continue
            #Process it
            atom_list = create_atom_list(path)
            amide_nitrogens = fa.find_amide_N(atom_list)
            atoms_around = fa.find_atoms_around(amide_nitrogens, distance, atom_list)
            glu_check = fa.glucarboxy_near_amide(atoms_around)
            asp_check = fa.aspcarboxy_near_amide(atoms_around)
            if glu_check[0] or asp_check[0]:
                #Record information of hits
                result_file.write(pdb_id + ':\n')
                if glu_check[0]:
                    result_file.write('\t' + glu_check[1].output_atom())
                if asp_check[0]:
                    result_file.write('\t' + asp_check[1].output_atom())
            else:
                os.remove(path)
        endtime = datetime.datetime.now()
        result_file.write('runtime = ' + str(endtime-starttime) + '\n')
        result_file.write('last searched PDB file = ' + pdb_ids[-1])
run_program()