from time import sleep, time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f"Время выполнения без потоков: {end_time - start_time:.2f} секунд")

threads = []
start_time = time()
files_and_counts = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]
for count, filename in files_and_counts:
    thread = Thread(target=write_words, args=(count, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time()
print(f'Время выполнения с потоками: {end_time - start_time:.2f} секунд')
