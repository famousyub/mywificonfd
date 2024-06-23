def find_pattern(string, pattern, start=0, end=None):
    if end is None:
        end = len(string)
    return string.find(pattern, start, end)


def copy_string(destination, dest_start, source, source_start, length):
    destination[dest_start:dest_start+length] = source[source_start:source_start+length]
 
def replace_tag(string, old_tag, new_tag):
    return string.replace(old_tag, new_tag)
 
def process_line(chLine, chCode, chTAG1, chTAG2):
    lenchLine = len(chLine)
 
    if lenchLine > 3:
        Status = 0
        status2 = 0
        Status1 = 0
        Status2 = 0
        status3 = 0
 
        Status = find_pattern(chLine, "_____", 0, 0)
        if Status > 0:
            copy_string(chCode, 0, chLine, 0, Status)
            chLine = ['\0'] * len(chLine)
            print(chLine)
 
            Status1 = find_pattern(chCode, chTAG1, 0, 0)
            if Status1 > 0:
                chcode2 = chCode[38:Status]
                print(chcode2)
                chcodenum = chCode[0:Status1]
                nom = f"{chcodenum}_TX_{chcode2}"
 
                status2 = find_pattern(nom, "HT_", 0, 0)
                if status2 > 0:
                    nom = nom[0:status2-1]
                    status3 = find_pattern(chCode, "HT_", 0, 0)
                    if status3 > 0:
                        chcode2 = chCode[status3+6:Status]
                        nom = f"{nom}_{chcode2}"
                # Add similar processing for other conditions...
 
            Status2 = find_pattern(chCode, chTAG2, 0, 0)
            if Status2 > 0:
                chcode2 = chCode[19:Status]
                chcodenum = chCode[0:Status2]
                nom = f"{chcodenum}_RX_{chcode2}"
                # Add similar processing for other conditions...
 
            if chCode:
                ptr_1 = chLine.find(find_1)
                ptr_2 = chLine.find(find_2)
                ptr_3 = chLine.find(find_3)
 
                if ptr_1 != -1 and ptr_2 != -1 and ptr_3 != -1:
                    index_1 = ptr_1 - 7
                    index_2 = ptr_2
                    index_3 = ptr_3
                    index_4 = index_2 - index_1
                    index_5 = index_2 - index_3
 
                    tag = chLine[index_1:index_1+7]
                    len_tag = len(tag)
                    a = len("       ")
 
                    ret = "       " not in tag
                    if ret:
                        if 5 <= index_4 < 13 and index_5 < 8:
                            libelle = chLine.split()[2]
                            mesure = chLine.split()[4]
                            dmesure = float(mesure)
                            unite = chLine.split()[6]
                            space = chLine.split()[8]
 
                            if space == "(,":
                                limiteInferieure = "0"
                                dlimiteInferieure = 0.0
                                limiteSuperieure = chLine.split()[10].rstrip(')')
                                dlimiteSuperieure = float(limiteSuperieure)
                            else:
                                limiteInferieure = chLine.split()[10].rstrip(',')
                                dlimiteInferieure = float(limiteInferieure)
                                limiteSuperieure = chLine.split()[12].rstrip(')')
                                dlimiteSuperieure = float(limiteSuperieure)
 
                            if dlimiteInferieure < dmesure < dlimiteSuperieure:
                                status = "0"
                            else:
                                status = "1"
 
                            
 
# Usage Example:
# You need to define the find_1, find_2, find_3, and other required variables before using this code.
 
# Example:
# find_1 = "find_1"
# find_2 = "find_2"
# find_3 = "find_3"
# chLine = "your_input_line"
# chCode = "your_initial_chCode"
# chTAG1 = "your_chTAG1"
# chTAG2 = "your_chTAG2"
# process_line(chLine, chCode, chTAG1, chTAG2)