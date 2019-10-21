# FEATURE SELECTION FOR DIAGNOSING METASTATIC COLORECTAL CANCER
#### Repo: Colon_Cancer_Diagnosis
#### Index Terms - feature selection, biomarkers, colorectal cancer,diagnosis
### Abstract
The possibility of predicting clinical outcomes based on objective
and reproducible indications of medical condition is enticing. Effective, inexpensive, and noninvasive diagnosis of colorectal cancer (CRC) involve new signal processing technologies for the discovery and characterization of appropriate biomarkers. We offer a
methodology involving protein markers that can help discriminating
metastatic from non-metastatic patients. In particular, we propose
the use of sparsity promoting estimation algorithms, such as LASSO,
LAR, Elastic Net, and OMP, for selecting biomarkers and ranking
them for relevance. We used a data set of 2164 protein markers
from 51 patients diagnosed with CRC, 39 non-metastatic and 12
metastatic. The data set reveals a major difficulty, which is lack
of measurements and abundance of variables. Notwithstanding the
underdetermined system of equations and the heavily unbalanced labeled data, the results show good coherence among the results of the
different algorithms and good discriminating performance. In addition, the method does not map the variables to a different domain,
as is the case with, e.g., principle component analysis, or wavelet
transforms, therefore retaining their original clinical significance.

### Codes:
#### Libraries used: Sklearn, Pandas and Numpy
This repository contains some tools developed to assist in the search for the most relevant biomarkers and also to validate the algorithms used.
The notebooks folder contains a python notebook which demonstrates the use of the developed tools.
The utils folder has the classes and functions developed for analysis and validation.
