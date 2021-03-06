# Pharmacy Counting Project

Extrct data from log file, compute total cost and number of unique prescriber, then load into new log file.

### Environment
python 3.6.5

### Packages
re == 2.2.1

### File structure
Raw data stored in *input* file and ETL result in *output* file, ETL scripts are in *src* file, including *pharmacy_counting* as main script, *help_functions* and *read_process_write* as defined function module.

### Summary of approaches
Firstly the solution read data from log file, clean string with comma in quotes and split every single line with comma seperator safely. Then the solution create a dict {drug_name: [total_cost, set(doctor_name)]} and update it for every single line. Finally reload data into text file with required format.

### Running ETL script
Use following command in Linux/Mac OS to run bash script to start data processing.

```
pharmacy_counting_by_Tao~$ ./run.sh
```

### Running the tests

Use following command inLinux/Mac OS to run bash script in *insight_testsuite* to start automatic unit testing.

```
insight_testsuite~$ ./run_tests.sh
```

### Future work
If having extra time, the scripts could be optimized by adding logging and instruments and adding more data quality check statements to improve robustness.

### Authors

* **Tao Songn** - *Initial work* - [waveambi](https://github.com/waveambi)

