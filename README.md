## alignment_models

### Intro
This code is a development of the original word learning model [FAS10](https://github.com/aidanematzadeh/word_learning), which introduces several in-the-moment learning mechanisms. We formulate such mutual exclusivity biases brought by these mechanisms as word competitions, referent competitions and no competition.  

### SAMPLE RUN & replicate experiments
A script called `scripts/SAMPLE_RUN.sh` can be run and is a good starting point to get familiar with the program.

To fully replicate the experiment results mentioned in the paper Fig.2, you can run the `scripts/prepare_four_alignment.sh`. It automatically runs all 4 alignment methods with training time 20k, and generate all four learning curves in one graph. The graphs are under folder `plot/` when completed.

### Configuration Settings
Configuration settings such alignment method, training time, similarity measure can be adjusted in `config.ini`. 
It is worthy to mention that the most important parameter inside configuration file is`alignment-method` which controls the alignment mechanism. You can switch to different word-referent alignment model by inputting different integers to the variable. <br>
If it's 0, the word learning model aligns word and feature directly as in FAS10. <br>
If it's 1, the model runs referent competition (i.e. ref-comp) aligning each word with all the referents in the scene. <br>
If it's 2, the model swithes to word competition (i.e. word-comp), in other words all words are competing for a referent during the alignemnts. <br>
If it's 3, then then there's no competition among words or referents (i.e. no-comp). <br>

Training time is set to 20k by default since the learning curve stays robust afterwards.

### Training Data & Gold lexicon
Under `data/` folder, a list of training data as well as the gold lexicon used in the experiments are provided.
`data/all_features_included.all` is the gold lexicon. For a given word, the probability distribution of a set of semantic features representing its gold-standard meaning is uniform.

In each training data, every utterance is paired with a scene. The scene consists of a set of **ALL** meaning features for **ALL** words in the utterance. Different set of semantic features belonging to each word in the sentence are separated by semicolons.

`all_features_included.dev` is the training data to generate the overall learning performance (Fig.2 in paper).
`mlu_*.txt` are datas to test the effect of Mean Length of Utterance. In particular, `mlu_long.txt` only consists of utterances of length greater than 4 whereas `mul_short.txt` are made up by utterances of length less than 4. <br>

We also experimented on the effect of referential certainty, the datas are the following: `rw_one.txt`, `rw_two.txt`, `rw_three.txt`.

### Dependencies
[seaborn](http://seaborn.pydata.org/), [matplotlib](http://matplotlib.org/), 
[nltk](http://www.nltk.org/), [numpy](http://www.numpy.org/), [scipy](https://www.scipy.org/)


### Reference
http://www.cs.toronto.edu/~aida/papers/nematzadeh_etal_17_cogsci_alignments.pdf
