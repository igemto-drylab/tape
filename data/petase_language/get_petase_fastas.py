import json
import glob
from pathlib import Path

for f in glob.glob("*.json"):
	fasta = ""
	fpath = Path(f)
	records = json.loads(fpath.read_text())
	for item in records:
		try:
			fasta += ">" + str(item['name']) + "\n"
		except TypeError:
			print(item['name'])
		fasta += item['sequence'] + "\n"
	with open(f[:-5] + ".fasta", 'w') as g:
		g.write(fasta)
