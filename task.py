import datetime
import contextlib


def factorial_calc():
    factorial = 1
    for x in range(1, 101):
        factorial = factorial * x
        print(f'{x}! = {factorial}')
    return


@contextlib.contextmanager
def run_time():
    start_time = datetime.datetime.now()
    yield  # код из блока with выполнится тут
    end_time = datetime.datetime.now()
    code_time = end_time - start_time
    print(f'Время запуска кода {start_time} \nВремя окончания кода {end_time} \nВремя выполнения кода {code_time}')


with run_time():
    factorial_calc()
