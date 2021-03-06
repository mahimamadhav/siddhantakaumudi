# This Python file uses the following encoding: utf-8
"""
Usage:
python step1.py sk0.txt step0_notes.txt
"""
import re,codecs,sys
import transcoder
def numberingerrors(filein,logfile):
	counter = 0
	fin = codecs.open(filein,'r','utf-8')
	fillog = codecs.open(logfile,'w','utf-8')
	for line in fin:
		if line.startswith('('):
			m = re.search('[(]([0-9]+)[)]',line)
			if m:
				rulenum = int(m.group(1))
				if not rulenum == counter + 1:
					fillog.write(str(counter)+','+str(rulenum)+'\n')
				counter = rulenum
	fin.close()
	fillog.close()
if __name__=="__main__":
	filein = sys.argv[1]
	logfile1 = sys.argv[2]
	numberingerrors(filein,logfile1)
