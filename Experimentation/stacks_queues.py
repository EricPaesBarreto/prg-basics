import queue as q

people = ['marcus', 'eric', 'amir', 'oleks', 'marta', 'dawid']

mcdonalds_queue = q.Queue()
mcdonalds_stack = q.LifoQueue()
for person in people:
    mcdonalds_queue.put(person)
    mcdonalds_stack.put(person)

print("QUEUE:")
while not mcdonalds_queue.empty():
    print(mcdonalds_queue.get())

print("STACK:")
while not mcdonalds_stack.empty():
    print(mcdonalds_stack.get())
