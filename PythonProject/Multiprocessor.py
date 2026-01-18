from multiprocessing import Process

def print_function(number):
    print("Printing for process ",number)

if __name__ == '__main__' :
    process_list = []
    for i in range(20):

        p = Process(target=print_function, args=(i,))
        process_list.append(p)

    for p in process_list:
        p.start()