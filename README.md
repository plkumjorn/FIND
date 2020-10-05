# FIND: Human-in-the-loop Debugging Deep Text Classifiers. EMNLP 2020

**_This README is now under construction and it will be ready around mid October 2020. Sorry for the inconvenience._**

**Authors**: [Piyawat Lertvittayakumjorn](https://www.doc.ic.ac.uk/~pl1515/), [Lucia Specia](http://www.imperial.ac.uk/people/l.specia), and [Francesca Toni](https://www.doc.ic.ac.uk/~ft/) (Department of Computing, Imperial College London)

**Paper links**: ACL Anthology (Available soon), ArXiv (Available soon)

**Contact**: Piyawat Lertvittayakumjorn (pl1515 [at] imperial [dot] ac [dot] uk)

## Description
TODO   

## How to use this repository
### Requirements
- tensorflow
- keras
- WordCloud
- iNNvestigate
- GloVe 300 dim

### Code organization
TODO

### Datasets
The datasets used in this paper can be downloaded [here](https://imperialcollegelondon.box.com/s/yph60lp41vxtr5bwea0pyfx2e65q8ked) as a single zip file. Some of the datasets are already in this github repository under the [`preprocessed_data`](https://github.com/plkumjorn/FIND/tree/master/preprocessed_data) folder with the data structure. For the other datasets, please download and extract the zip file and put them together in the `preprocessed_data` folder. 

|Experiment|Dataset|#Classes|Train / Dev / Test|
|-----|-----|-----|-----|
|1|Yelp|2|500 / 100 / 38000|
||Amazon Products|4|100 / 100 / 20000|
|2|Biosbias|2|3832 / 1277 / 1278|
||Waseem|2|10144 / 3381 / 3382|
||Wikitoxic|2|- / - / 18965|
|3|20Newsgroups|2|863 / 216 / 717|
||Religion|2| - / - / 1819|
||Amazon Clothes|2| 3000 / 300 / 10000|
||Amazon Music|2| - / - / 8302|
||Amazon Mixed|2| - / - / 100000|



## Paper
**Title**: FIND: Human-in-the-loop Debugging Deep Text Classifiers

**Authors**: Piyawat Lertvittayakumjorn, Lucia Specia, and Francesca Toni

**Venue**: [The 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020)](https://2020.emnlp.org/)

**Abstract**: Since obtaining a perfect training dataset (i.e., a dataset which is considerably large, unbiased, and well-representative of unseen cases) is hardly possible, many real-world text classifiers are trained on the available, yet imperfect, datasets. These classifiers are thus likely to have undesirable properties. For instance, they may have biases against some sub-populations or may not work effectively in the wild due to overfitting. In this paper, we propose **FIND** -- a framework which enables humans to debug deep learning text classifiers by disabling irrelevant hidden features. Experiments show that by using FIND, humans can improve CNN text classifiers which were trained under different types of imperfect datasets (including datasets with biases and datasets with dissimilar train-test distributions).

**Paper links**: ACL Anthology (Available soon), ArXiv (Available soon)

**Please cite**: TODO
	
