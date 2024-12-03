import pandas as pd

def loadData(file):
    data_arr = pd.read_csv(file, header=None)
    data = data_arr[0].to_list()
    data = [d.split() for d in data]
    data = [[int(i) for i in d] for d in data]
    return data

def checkSafe(d):
    flag = True
    check_list = []
    for i in range(1, len(d)):
        if flag:
            check_list.append(d[i]-d[i-1])
            if abs(d[i]-d[i-1]) > 3:
                flag=False
    if flag:
        if all(x < 0 for x in check_list) or all(x > 0 for x in check_list):
            return True
    else:
        return False
    
def checkDamp(unsafe):
    safe2=[]
    for item in unsafe:
        flag = True
        for i in range(len(item)):
            new_list = item[:i] + item[i+1:]
            check = checkSafe(new_list)
            if check:
                safe2.append(item)
                break
    return safe2


if __name__ == "__main__":
    data = loadData('test.txt')
    safe = [d for d in data if checkSafe(d)]
    unsafe = [d for d in data if not checkSafe(d)]

    safe2 = safe + checkDamp(unsafe)

    print(f"P1 Safe: {len(safe)}")
    print(f"P2 Safe: {safe2}")