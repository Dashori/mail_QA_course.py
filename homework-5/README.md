# Домашнее задание №5

Скрипты `log.sh` и `log.py` анализируют информацию из файла `access.log` и выводят её в файлы `res_sh.txt` и `res_py.txt` соответственно.

- Для приложенного в задании access.log файла  собирается следующая информация:

  - Общее количество запросов 

  - Общее количество запросов по типу (GET, POST, PUT, HEAD)

  - Топ 10 самых частых запросов:

    ```
    выводится url
    выводится число запросов
    ```

  - Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:

    ```
    выводится url
    выводится статус код
    выводится размер запроса
    выводится ip адрес
    ```

  - Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:

    ```
    выводится ip адрес
    выводится количество запросов
    ```

Плюсы и минусы реализации данного скрипта на Python и Bash:

```
       |  Количество строк  |    Время

Bash   |          24        |   2 секунды

Python |         124        |   56 секунд
```
Таким образом мы видим, что Python проигрывает и по количеству строк, то есть по сложности написания скрипта и по времени. Python может быть полезен только тогда, когда нам нужно делать какие-то более сложные операции с нашими данными в самой питоновской программе.
