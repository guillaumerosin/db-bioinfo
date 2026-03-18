D=$1
np=$(nproc)
/opt/pear-0.9.11-linux-x86_64/bin/pear \
	-f $D/*_R1_* \
	-r $D/*_R2_* \
	-v 23 \
	-j $np \
	-o bla
of=bla.assembled.fastq
awk 'NR%4==2' $of | sort |uniq -c|sort -nr >bla.uniq
head -2 bla.uniq
cat bla.uniq | python script_coo.py >bla.simplified
sed -i -e '1,6 d' bla.simplified
head -2 bla.simplified
head -200 bla.simplified >bla.top100.fa
/opt/bp/blastn \
	-task blastn \
	-query bla.top100.fa \
	-num_threads $np \
	-db 16S_ribosomal_RNA \
	-outfmt "7 qseqid length pident qstart qend ssciname" \
	-max_target_seqs 5 \
	-out bo
grep -v '^#' bo |awk '{print $6,$7}'| sort|uniq -c|sort -nr >$D/result
