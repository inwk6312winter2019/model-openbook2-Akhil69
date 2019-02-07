import csv

fin = open("Bus_Stops.csv", 'r')
fin1 = open("Street_Centrelines.csv", 'r')
def test():
    st = []
    st1 = []
    for file in fin:
        stp = file.split(",")
        if stp[10] == "ARTERIAL":
            strt = stp[4].strip()
            if strt not in st:
                 st.append(strt)
    print(stp)
    res = []
    for s in st1:
        for i in fin1:
            j = d.split(",")
            if n[7] == "Accessible":
                rs = n[6].strip().lower()
                if rs.find(st) >= 0:
                     res.append(n[2])
    print(res)
test()
