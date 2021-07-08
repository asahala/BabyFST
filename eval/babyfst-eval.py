#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from collections import Counter

""" This script evaluates transducer outputs. It requires 

   FILENAME.results          that contains analyses produced
                             by BabyFST
   oracc-lemmas.freqs        list of lemma frequencies
                             extracted from Oracc 

How to run:

   python babyfst-eval.py -f FILENAME

   Do not add extension to your FILENAME!

"""

def readfile(filename):
    with open(filename, 'r', encoding="utf-8") as data:
        return data.read().splitlines()

def writefile(filename, d):
    with open(filename, 'w', encoding='utf-8') as data:
        data.write('\n'.join(d))

def get_args():
    ap = argparse.ArgumentParser(description='Test')
    ap.add_argument('-f', '--files', nargs='*')
    return ap.parse_args()

""" Read lemma freqs """
lemmafreqs = {}
for line in readfile('../oracc/oracc-lemmas.freqs'):
    freq, lemma, pos = line.split('\t')
    lemmafreqs.setdefault(lemma+'+'+pos, int(freq))

""" Separate wf, analysis and pos from given foma output """
def _separate(string):
    wf, analysis = string.split('\t')
    lemma = analysis.split('+')[0]
    pos = analysis.split('+')[1]
    if '=' in pos:
        pos = pos.split('=')[0]
    return wf, lemma, pos

""" Get analyses with highest lemma freq """
def get_mostfreq(data, top=2, gold_standard=None, short=False, filename=''):
    OUT = []
    errors_pos = {}
    errors_pos_bool = {}
    output = []
    analyses = []
    unknowns = 0
    count = 0
    amb_dist = []
    total_bool_matches = 0 # true if any analyses were correct
    total_count_matches = 0 # count number of correct analyses
    total_analyses = 0 # total number of analyses
    for line in data:
        if not line:
            freqs = []
            
            for x in analyses:
                wf, lemma, pos = _separate(x)
                if '|' in lemma:
                    lemmata = lemma.split('|')
                else:
                    lemmata = [lemma]
                for l in lemmata:
                    freqs.append(lemmafreqs.get(l+'+'+pos, 0))
            amb_dist.append(len(analyses))
            #if len(analyses) > 190:
            #    print(analyses)
            # Build a dictionary of lemma frequencies
            freqdict = {}
            for k, v in zip(freqs, analyses):
                freqdict.setdefault(k, []).append(v)
            analyses = []
            
            top_analyses = []
            match_bool = 0  # yes - no level match
            match_count = 0 # number of matching lemma+pos combsinations

            for fkey in sorted(freqdict.keys(), reverse=True)[0:top]:
                for analysis in freqdict[fkey]:
                    wf, lemma, pos = _separate(analysis)
                    result = lemma + '+' + pos
                    gold = gold_standard[count].split('\t')[-1]
                    goldpos = gold.split('+')[-1]
                    ## add + for matches and - for mismatches
                    if '|' in lemma:
                        lemmata = lemma.split('|')
                        results = [x + '+' + pos for x in lemmata]
                    else:
                        results = [result]

                    if gold in results:
                        match = '+'
                        match_bool = 1
                        match_count += 1
                        errors_pos.setdefault(goldpos, {'match': 0, 'mismatch':0, 'unknown':0})['match'] += 1
                    else:
                        match = '-'
                        #print(gold, results)
                        errors_pos.setdefault(goldpos, {'match': 0, 'mismatch':0, 'unknown':0})['mismatch'] += 1
                    top_analyses.append((analysis, fkey, match))
        
            ## keep track of total matches
            if match_bool:
                total_bool_matches += 1
                errors_pos_bool.setdefault(goldpos, {'match': 0, 'mismatch':0,'unknown':0})['match'] += 1
            else:
                errors_pos_bool.setdefault(goldpos, {'match': 0, 'mismatch':0,'unknown':0})['mismatch'] += 1 

            total_count_matches += match_count
            total_analyses += len(top_analyses)

            ## append to final output list
            output.append('\n## word=%i match=%i gold=%s' % (count, match_bool, gold))
            for a, f, m in top_analyses:
                output.append('%s\t%i\t%s' % (a, f, m))

            count += 1
        else:
            if '+?' in line:
                unknowns += 1
            if line not in analyses:
                analyses.append(line)

    #for x, y in Counter(amb_dist).items():
    #    print(x, y)

    if count > 0:
        coverage = (count - unknowns) / count
        recall =  total_bool_matches / count
        precision = total_count_matches / total_analyses
        ambiguity = total_analyses / count
        
        OUT.append('|'.join([filename, str(coverage), str(recall), str(precision), str(ambiguity), str(count)]))

        POSS = [('V'), ('N'), ('AJ'), ('AV'), ('PRP', 'PP'),
                ('CNJ', 'SBJ'), ('J'), ('MOD'), ('NU'), 
                ('DP', 'IP', 'XP', 'QP', 'REL'),
                ('CN','DN','EN','GN','KN','LN','MN','NN','ON','PN','QN','RN','SN','TN','WN')]
        names = ['V', 'N', 'AJ', 'AV', 'PRP', 'CNJ', 'J', 'MOD', 'NU', 'PRON', 'NAME']


        POSS = [('V'), ('N'), ('AJ'), ('AV'), ('PRP', 'PP', 'CNJ', 'SBJ', 'J', 'MOD', 'NU'), 
                ('DP', 'IP', 'XP', 'QP', 'REL'), 
                ('CN','DN','EN','GN','KN','LN','MN','NN','ON','PN','QN','RN','SN','TN','WN')]
        names = ['V', 'N', 'AJ', 'AV', 'MISC', 'PRON', 'NAME']


        if not short:
            OUT.append('\nRECALL BY POS:')
            DICT = {}
            for k, v in errors_pos_bool.items():
                i = 0
                for pos in POSS:
                    name = names[i]
                    if k in pos:
                        DICT.setdefault(name, []).append(v['match'] / (v['mismatch'] + v['match']))
                        
                    i += 1
                #OUT.append(k + '\t%.3f' % (v['match'] / (v['mismatch'] + v['match'])))
            
            for k, v in sorted(DICT.items()):
                OUT.append(k + '\t%.4f' % (sum(v) / len(v))) 
            OUT.append('\n')
            OUT.append('\n'.join(output))

    writefile(filename+'.eval', OUT)
    print('    -->', filename + '.eval')

args = get_args()
for fi in args.files:
    f = fi.split('.')[0]
    print(f)
    get_mostfreq(readfile(f+'.results'),
             top=100,
             gold_standard=readfile(f+'.gold'),
             short=False,
             filename=f)
