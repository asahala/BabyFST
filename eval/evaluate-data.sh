file="$1"

cat $file.txt | ~asahala/foma/flookup ~asahala/work/BabyFST/compiled/poista.foma > $file.results &&
python3 babyfst-eval.py -f $file &&
echo DONE!
