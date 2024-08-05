# group_files_by_date

helper script to group files into folders based on their last modified date.

## usage

### setup

- move files into ./input, as in:

    ```txt
    D:.
    │  .gitignore
    │  file_operations.py
    │  LICENSE
    │  README.md
    │  
    └─input
            sample_0
            SecondtoTime.h
            what_happens_during_function_call.cpp
    ```

- run file_operations.py, which results in:

    ```txt
        D:.
    │  .gitignore
    │  file_operations.py
    │  LICENSE
    │  README.md
    │
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
