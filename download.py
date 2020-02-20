import urllib.request

def download_pdb(url, path):
    status = 'NORMAL'
    try:
        urllib.request.urlretrieve(url, path)
        print("File downloaded")
    except urllib.request.URLError:
        print("URL error")
        status = 'ERROR'
    except ValueError:
        print("Value error")
        status = 'ERROR'
    except urllib.request.HTTPError:
        print("HTTP error")
        status = 'ERROR'
    return status

def create_pdb_ids(num, initial_id):
    figures = ['1','2','3','4','5','6','7','8','9']
    alphabets = list(map(chr, list(range(65,91))))
    pdb_ids = []
    for char1 in figures:
        pdb_id = char1
        for char2 in alphabets:
            pdb_id = pdb_id[0] + char2
            for char3 in figures + alphabets:
                pdb_id = pdb_id[0:2] + char3
                for char4 in figures + alphabets:
                    pdb_id = pdb_id[0:3] + char4
                    if len(pdb_ids) < num:
                        if pdb_id >= initial_id:
                            pdb_ids.append(pdb_id)
                    else:
                        return pdb_ids