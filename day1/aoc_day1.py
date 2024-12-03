
#file = 'input.txt'
#data = open(file).read()

def loadData(file):
  data = open(file).read().splitlines()
  return data

def distanceLists(data):
  a_sort = sorted([int(d[:5]) for d in data])
  b_sort = sorted([int(d[8:]) for d in data])

  total = 0
  for i in range(len(a_sort)):
    diff = abs(b_sort[i] - a_sort[i])
    total += diff
  return total

def simScore(data):
  a_sort = sorted([int(d[:5]) for d in data])
  b_sort = sorted([int(d[8:]) for d in data])

  l_counter = []

  for i in a_sort:
      counter = 0
      for j in b_sort:
          if i == j:
              counter +=1
      l_counter.append(counter)

  s = 0
  for k in range(len(l_counter)):
      s += l_counter[k]*a_sort[k]
  return s


if __name__ == "__main__":

  data = loadData('input.txt')
  total = distanceLists(data)
  s = simScore(data)

  print(f"Distance Score: {total}")
  print(f"Similarity Score: {s}")

