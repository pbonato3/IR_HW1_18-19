# IR_HW1_18-19

This repository is about an homework of Information Retrieval course at University of Padua, Italy.

## Task

The task is to perform 50 given queries on TREC7 test collection with 4 different configurations using an IR system, and then to evaluate results.

The 4 retrieval configurations are:
* Run_0: BM25 model, Stoplist and PortStemmer
* Run_1: TF_IDF model, Stoplist and PortStemmer
* Run_2: BM25 model, NO Stoplist, PortStemmer
* Run_3: TF_IDF model, NO Stoplist and NO PortStemmer

## Repository structure

Terrier settings and results for the different runs can be found respectively in folders: 0,1,2,3.
In every folder you can find:
* ".properties" file used to configure Terrier
* ".res" and ".res.settings" output files relative to retrievals with and without query expansion option
* "eval_n.txt" file that contains trec_eval complete output and "eval_n_qe.txt" file for the query expansion version

Source of the program developed to perform analysis is in main.py file while Plots folder contains all the outputs of the program

### Softwares used

The chosen IR system is Terrier v 4.4, programming language Python v 2.7.12 with: matplotlib v 2.2.3, SciPy
v 1.1.0, statsmodels v 0.9.0.
