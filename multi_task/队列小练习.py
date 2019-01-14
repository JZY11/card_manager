import multiprocessing

q = multiprocessing.Queue(3)
q.put("111")
q.put(222)
print(q.empty())

q.put([11, 22, 33])
print(q.full())

print(q.get())
print(q.get())
print(q.get())