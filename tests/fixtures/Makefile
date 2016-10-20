all: zen.txt.bz2 zen.txt.gz zen.txt.xz zen.txt.zip zen.txt.unk

clean:
	rm -rf zen.txt.bz2 zen.txt.gz zen.txt.xz zen.txt.zip zen.txt.unk

zen.txt.bz2: zen.txt
	bzip2 -k zen.txt

zen.txt.gz: zen.txt
	gzip -k zen.txt

zen.txt.xz: zen.txt
	lzma -c zen.txt > zen.txt.xz

zen.txt.zip: zen.txt
	zip zen.txt.zip zen.txt

zen.txt.unk: zen.txt
	cat zen.txt > zen.txt.unk
