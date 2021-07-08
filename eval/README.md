# BabyFST evaluation (Transducer version: August 2020)

Evaluation data for BabyFST (contained in ```eval-output.7z```). 

### Evaluation metrics:
* Coverage :: percentage of inputs that returned non-empty analysis
* Recall :: percetage of inputs that returned at least one correct analysis (lemma and POS-tag)
* Precision :: percentage of correct analyses over all returned analyses
* Ambiguity :: average number of lemmata returned analyses per input
* Count :: number of inputs

### Abbreviations:
* OB :: Old Babylonian (akk-x-oldbab)
* MB :: Middle-Babylonian and Middle-Babylonian peripheral (akk-x-mbperi, akk-x-midbab)
* SB :: Standard Babylonian (akk-x-stdbab)
* NB :: Neo-Babylonian (akk-x-neobab)
* LB :: Late Babylonian (akk-x-ltebab)
* COMB :: represents results over all the data combined

Note that MB and NB also contain Oracc words labeled as "akk" in text from the Middle and Neo-Babylonian periods, not only the words tagged as akk-x-midbab/mbperi/neobab.

## OVERALL EVALUATION

### Babylonian tokens
| Dataset | Cov | Rec | Prec | Amb | Count | 
| :--- | ---: | ---: | ---: | ---: | ---: |
| OB | 0.96 | 0.926 | 0.366 | 5.665 | 57737 |
| MB | 0.982 | 0.944 | 0.308 | 7.234 | 17122 |
| SB | 0.981 | 0.962 | 0.303 | 6.997 | 189851 |
| NB | 0.963 | 0.937 | 0.33 | 6.672 | 137113 |
| LB | 0.988 | 0.978 | 0.337 | 6.099 | 103923 |
| COMB | 0.975 | 0.954 | 0.323 | 6.58 | 505746 |

### Babylonian types
| Dataset | Cov | Rec | Prec | Amb | Count | 
| :--- | ---: | ---: | ---: | ---: | ---: |
| OB | 0.917 | 0.868 | 0.41 | 5.422 | 10749 |
| MB | 0.959 | 0.91 | 0.316 | 7.063 | 5380 |
| SB | 0.946 | 0.896 | 0.355 | 6.489 | 28017 |
| NB | 0.905 | 0.846 | 0.4 | 6.079 | 17764 |
| LB | 0.868 | 0.832 | 0.498 | 4.577 | 3511 |
| COMB | 0.927 | 0.875 | 0.377 | 6.14 | 65421 |


## BY PART-OF-SPEECH

Note that the latest version of the trasducer has some issues with the verbs.

### Recall by Babylonian tokens
| POS | OB | MB | SB | NB | LB | COMB |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| AJ | 0.978 | 0.860 | 0.694 | 0.869 | 0.991 | 0.875 |
| AV | 0.933 | 0.927 | 0.957 | 0.920 | 0.888 | 0.918 |
| N | 0.974 | 0.976 | 0.973 | 0.966 | 0.992 | 0.980 |
| NAME | 0.820 | 0.834 | 0.931 | 0.888 | 0.959 | 0.877 |
| PRON | 0.779 | 0.934 | 0.981 | 0.922 | 0.990 | 0.955 |
| V | 0.884 | 0.872 | 0.915 | 0.849 | 0.776 | 0.844 |
| MISC | 0.974 | 0.937 | 0.911 | 0.907 | 0.999 | 0.945 |

### Recall by Babylonian types
| POS | OB | MB | SB | NB | LB | COMB |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
|  AJ | 0.973 | 0.901 | 0.841 | 0.846 | 0.942 | 0.900 |
|  AV | 0.863 | 0.893 | 0.914 | 0.875 | 0.819 | 0.870 |
|  N | 0.943 | 0.957 | 0.941 | 0.929 | 0.934 | 0.938 |
|  NAME | 0.773 | 0.829 | 0.854 | 0.802 | 0.889 | 0.788 |
|  PRON | 0.817 | 0.88# | 0.956 | 0.756 | 0.919 | 0.815 |
|  V | 0.786 | 0.822 | 0.829 | 0.775 | 0.638 | 0.770 |
|  MISC | 0.825 | 0.853 | 0.941 | 0.775 | 0.985 | 0.867 |

## How to rerun evaluation?
Extract evaluation data in ```data``` folder to get the input and gold standard files. Then run ```evaluate-data.sh``` e.g. ```sh evaluate-data.sh data/tokens-akk-x-oldbab``` for Old Babylonian tokens. This will create a file called ```tokens-akk-x-oldbab.eval``` containing the results. Remember to to change the transducer and Foma paths in the bash file! Also make sure that ```../oracc/oracc-lemmas.freqs``` is present.

Evaluation requires https://pypi.org/project/hfst/ to be installed. As Foma transducers are GZIPped by default, you will need to ```gunzip``` the transducer before using it through the HFST PyPI. This can be simply done by ```cp transducer.foma transducer.hfst.gz && gunzip transducer.hfst.gz```.

To explore the current evaluation results, extract ```eval-output.7z```.

# Errata for BabyFST evaluation (LREC 2020) 
Re-evaluation of the transducer (2019 version) used in LREC 2020 paper. In this evaluation, the data is strictly limited to the labeled dialects, and all unlabeled data is removed (i.e. words that were supposed to be of a certain dialect based on their time period: this caused some overlap in the dataset).

The errors in the dataset were generally detrimental to the evaluation results presented in Tables 5, 6 and 7 of the publication, but overall the changes are not significant, except for some individual POS classes in OB and LB.

Sections 4.1, 4.2 and 4.3 do not need revision.

## OVERALL EVALUATION

### Babylonian tokens (Table 5)
| Dataset | Cov | Rec | Prec | Count |
| :--- | ---: | ---: | ---: | ---: |
| OB | 0.954 | 0.907 | 0.442  | 57737 |
| MB | 0.97 | 0.899 | 0.396 | 17122 |
| SB | 0.985 | 0.961 | 0.415 | 189851 |
| NB | 0.962 | 0.919 | 0.406 | 137113 |
| LB | 0.988 | 0.97 | 0.435 | 103923 |
| COMB | 0.975 | 0.943 | 0.418 | 505746 |

### Babylonian tokens (changes)
This table summarizes how much the results improve (+) or decrease (-) when the errors in the LREC evaluation data are fixed.
| Dataset | Cov | Rec | Prec | 
| :--- | ---: | ---: | ---: |
| OB | -0.006 | -0.003 | +0.023 |
| MB | +0.012 | +0.004 | -0.01 |
| SB | +0.011 | +0.024 | +0.004 |
| LB | +0.002 | +0.009 | +0.003 |
| NB | +0.017 | +0.039 | +0.016 |

### Babylonian types (Table 6)
| Dataset | Cov | Rec | Prec | Count |
| :--- | ---: | ---: | ---: | ---: |
| OB | 0.906 | 0.827 | 0.481 | 10749 |
| MB | 0.939 | 0.836 | 0.405 | 5380 |
| SB | 0.959 | 0.892 | 0.446 | 28017 |
| NB | 0.897 | 0.798 | 0.446 | 17764 |
| LB | 0.874 | 0.842 | 0.594 | 3511 |
| COMB | 0.927 | 0.848 | 0.455 | 65421 |

### Babylonian types (changes)
This table summarizes how much the results improve (+) or decrease (-) when the errors in the LREC evaluation data are fixed.
| Dataset | Cov | Rec | Prec | 
| :--- | ---: | ---: | ---: |
| OB | +0.006 | +0.022 | +0.015 |
| MB | +0.048 | +0.054 | -0.042 |
| SB | +0.033 | +0.056 | -0.004 |
| NB | +0.014 | +0.024 | 0.0 |
| LB | -0.011 | +0.056 | +0.12 |

## BY PART-OF-SPEECH
### Recall by Babylonian tokens (Table 7)
| POS | OB | MB | SB | NB | LB |
| :--- | ---: | ---: | ---: | ---: | ---: |
| AJ | 0.931 | 0.76 | 0.647 | 0.805 | 0.99 |
| AV | 0.854 | 0.753 | 0.96 | 0.79 | 0.887 |
| N | 0.941 | 0.931 | 0.98 | 0.937 | 0.971 |
| NAME | 0.82 | 0.828 | 0.935 | 0.888 | 0.959 |
| PRON | 0.778 | 0.934 | 0.981 | 0.921 | 0.99 |
| V | 0.885 | 0.882 | 0.925 | 0.885 | 0.783 |
| MISC | 0.974 | 0.919 | 0.91 | 0.906 | 1.0 |

