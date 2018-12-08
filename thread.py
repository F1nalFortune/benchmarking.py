import threading
import time

answer = input('Float or Integer:\n')
thread_size = input('Thread size:\n')

def start():
  class myThread(threading.Thread):
    def __init__(self,name,delay):
      threading.Thread.__init__(self)
      self.name=name
      self.__delay=delay
    def run(self):
      if(answer.lower() =='float'):
        count=0.0
        stop=time.time() + 60
        print("Thread "+self.name+"\n")
        time.sleep(self.__delay)
        while time.time() < stop:
          count+=1.0
        print(str(count)+"Exit Thread "+self.name+"\n")
      elif (answer.lower()=='integer'):
        count=0
        stop=time.time() + 60
        print("Thread "+self.name+"\n")
        time.sleep(self.__delay)
        while time.time() < stop:
          count+=1
        print(str(count)+"Exit Thread "+self.name+"\n")
      else:
        print("invalid entry")
  myThreadList = []
  for i in range(int(thread_size)):
    thread1=myThread(str(i+1), 3)
    myThreadList.append(thread1)
    thread1.start()

  def combine():
    print("Combine file!\n")

  for item in myThreadList:
    # waits for thread to complete before it exicutes
    item.join()

  combine()
  #threadFunction1()
  print("\n---------------------------------------------- \n\
    Round "+ str(x+1) + "! \n")
for x in range(3):
    start()
