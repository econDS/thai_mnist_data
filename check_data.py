import glob


def get_set(folder):
    paths = glob.glob(folder+'/*.jpg')
    filenames = [file.split("\\")[1] for file in paths]
    names = [name.split("_")[0] for name in filenames]
    names = set(names)
    return names

aum1 = get_set("อั้ม/handwriting_aumm_v1") # 72
aum2 = get_set("อั้ม/handwriting_aumm_v2") # 72
aum3 = get_set("อั้ม/handwriting_aumm_font_jpeg") # 44

bo1 = get_set("โบ้/BoC") #44
bo2 = get_set("โบ้/BoV") #12
bo12 = bo1.union(bo2) #66

pap1 = get_set("แปป/Thai Handwriting thana") # 44

print("aum - bo")
print(aum1.difference(bo12))
print("bo - aum")
print(bo12.difference(aum1))
print("aum - pap")
print(aum1.difference(pap1))
