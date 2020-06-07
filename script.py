from datetime import datetime
import time
import sys
counter_compare = 0
counter_replace = 0

server_file = sys.argv[1]

handle = open(server_file, "r")
shaker_array = handle.read()
handle.close()
print(shaker_array)
shaker_array = shaker_array.split(' ')
print(shaker_array)
for i in range(0, len(shaker_array)):
    shaker_array[i] = int(shaker_array[i])
print(type(shaker_array))
print(shaker_array)
print('Array before shaker', shaker_array)

index_start_R = 0
index_stop_R = len(shaker_array) - 1

start_time = datetime.now()
s = ''' '''
while True:
    print("index_start_R:",index_start_R)
    print("index_stop_R:",index_stop_R)
    if index_stop_R != index_start_R:
        ############################################################################
        step = 1
        for i in range(index_start_R, index_stop_R, step):
            counter_compare = counter_compare + 1
            if shaker_array[i] > shaker_array[i+step]:
                shaker_array[i], shaker_array[i+step] = shaker_array[i+step], shaker_array[i]
                counter_replace = counter_replace + 1

        index_stop_R = index_stop_R - 1
        ############################################################################
    else:
        break
    index_stop_L = index_start_R
    index_start_L = index_stop_R
    if index_stop_L != index_start_L:
        ############################################################################
        step = -1
        for i in range(index_start_L, index_stop_L, step):
            counter_compare = counter_compare + 1
            if shaker_array[i] < shaker_array[i+step]:
                shaker_array[i], shaker_array[i+step] = shaker_array[i+step], shaker_array[i]
                counter_replace = counter_replace + 1

        index_stop_L = index_stop_L + 1
        ############################################################################
    else:
        break

    index_start_R = index_stop_L
    index_stop_R = index_start_L
print('Array after shaker', shaker_array )
print("Compare:",counter_compare)
print("Replace:", counter_replace)
print(" Lenght:", len(shaker_array))
print("Time:")
print(datetime.now() - start_time)
for i in range(0, len(shaker_array)):
    shaker_array[i] = str(shaker_array[i])
result =  ' '.join(shaker_array)
handle = open("server_outcoming.txt", "w")
handle.write(result)
handle.close()
