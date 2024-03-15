from typing import List, Callable

#exemplo de função lambda
add_one = lambda x: x + 1

#exemplo de uma list comprehension
squares = [x**2 for x in range(1, 6)]

#exemplo de função de continuação
def delayed_execution(func: Callable[[], None], delay: int):
    import time
    time.sleep(delay)
    func()

#exemplo de closure
def make_incrementer(start: int):
    def incrementer():
        nonlocal start
        start += 1
        return start
    return incrementer

#exemplo de uma função de alta ordem
def apply_function_to_list(func: Callable[[int], int], lst: List[int]) -> List[int]:
    return [func(x) for x in lst]

#exemplo de um monad
def add_ten(value: int) -> int:
    return value + 10

#imprimindo os exemplos acima
print("Lambda:", add_one(5))
print("List Comprehension:", squares)
delayed_execution(lambda: print("Continuation: Executou após delay!",), 2)
incrementer = make_incrementer(0)
print("Closure:", incrementer())
print("High Order Function:", apply_function_to_list(add_one, [1, 2, 3, 4, 5]))
print("Monad:", add_ten(5))
