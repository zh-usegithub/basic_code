from multiprocessing import Pool

def task_function(name):
    print('执行',name)
if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['1','2','3','4','5']
    for task_new in tasks:
        pool.apply_async(task_function,args=(task_new,))
    pool.close()
    pool.join()
    print('over')

