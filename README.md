![alt text](https://www.mv.helsinki.fi/home/asahala/img/babyfst.png)

Babylonian Finite-State Morphology v. 2.0

# Requirements
For using the transducer you need Foma https://fomafst.github.io/. For evaluation you will need the HFST PyPi https://pypi.org/project/hfst/.

# Recompile
Use files in `src` folder.

# Todo
Disambiguation, unify similar verb classes, get rid of unnecessary meta-symbols, fix Assyrian vowel harmony, split lexicon into dialects 

# How to cite
If you use BabyFST, redistribute or modify it, cite the paper below.

```
@inproceedings{sahala-etal-2020-babyfst,
    title = "{B}aby{FST} - Towards a Finite-State Based Computational Model of Ancient Babylonian",
    author = "Sahala, Aleksi  and
      Silfverberg, Miikka  and
      Arppe, Antti  and
      Lind{\'e}n, Krister",
    booktitle = "Proceedings of the 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2020.lrec-1.479",
    pages = "3886--3894",
    abstract = "Akkadian is a fairly well resourced extinct language that does not yet have a comprehensive morphological analyzer available. In this paper we describe a general finite-state based morphological model for Babylonian, a southern dialect of the Akkadian language, that can achieve a coverage up to 97.3{\%} and recall up to 93.7{\%} on lemmatization and POS-tagging task on token level from a transcribed input. Since Akkadian word forms exhibit a high degree of morphological ambiguity, in that only 20.1{\%} of running word tokens receive a single unambiguous analysis, we attempt a first pass at weighting our finite-state transducer, using existing extensive Akkadian corpora which have been partially validated for their lemmas and parts-of-speech but not the entire morphological analyses. The resultant weighted finite-state transducer yields a moderate improvement so that for 57.4{\%} of the word tokens the highest ranked analysis is the correct one. We conclude with a short discussion on how morphological ambiguity in the analysis of Akkadian could be further reduced with improvements in the training data used in weighting the finite-state transducer as well as through other, context-based techniques.",
    language = "English",
    ISBN = "979-10-95546-34-4",
}
```
# Errata for the publication

In Section 2.4, the paper should read: 1.4 million words occurring in texts labeled to contain Akkadian have been lemmatized or POS-tagged. Thus this figure also contains languages other than Akkadian in multilingual texts, and words that have not been given a lemma because they are too broken, numbers, etc. In reality about 1.3 million words in lemmatized/POS-tagged texts are explicitly labeled as Akkadian, and of these all are not given lemmas due to the aforementioned reasons.

This is an unfortunate error that occurs in several word count statements about Korp-Oracc due to my mistake in a Google Docs sheet about the 2019 Korp-Oracc data.

See also ```./eval``` for revised results with explicitly labeled data without overlapping inputs.

# Acknowledgements

This piece of software would not have been possible without the hard work of dozens of Assyriologists lemmatizing the Akkadian texts in the [Oracc](http://oracc.org) corpus: Jamie Novotny, Laurie Pearce, John Carnahan, Philip Jones, Alexa Bartelmus, Cristopher Bravo, Frauke Weierhäuser, Giulia Lentini, Jay Cristostomo, Joshua Jeffers, Melanie Groß, Mikko Luukko, Nathan Morello, Poppy Tushingham, Talia Prussin (and many others whose names I do not know).

//testi
