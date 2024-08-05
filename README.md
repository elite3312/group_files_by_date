# group_files_by_date

A small helper script that groups files into folders based on their last modified month.

## usage, basic

- move files into ./input, as in:

    ```txt
    └─input
            sample_0
            SecondtoTime.h
            what_happens_during_function_call.cpp
    ```

- run file_operations.py, which results in:

    ```txt
    ├─2024_1
    │      what_happens_during_function_call.cpp
    │
    ├─2024_3
    │      SecondtoTime.h
    │
    ├─2024_8
    │      sample_0
    │
    └─input
    ```

## usage, -o

- checks the folders 20xx_x/ for missplaced files. By missplace I mean the last update time does not match the name of the folder it is in.
- make sure you have run file_operations.py without arguments at least once to have a folder strcute like the following:

    ```txt
    ├─2024_1
    │      what_happens_during_function_call.cpp
    │
    ├─2024_3
    │      ascii.txt
    │      SecondtoTime.h
    │
    ├─2024_8
    │      sample_0
    │
    └─input
    ```

  - in this exmample, ascii.txt has last update date 2024/1, which does not match the given rule.

- run file_operations.py -o, which results in:

    ```txt
    ├─2024_1
    │      ascii.txt
    │      what_happens_during_function_call.cpp
    │
    ├─2024_3
    │      SecondtoTime.h
    │
    ├─2024_8
    │      sample_0
    ```
