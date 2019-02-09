import re
files = ["Sports","Politics","Entertainment","Technology"]
#files = ["Sports"]


for i in files:
	output_file = i+"_no_hash_no_user.csv" 
	file = i+".csv"

	write_f = open(output_file, 'w')

	with open(file,"r") as f:
		for line in f:
			line = line.split("\n")[0]
			line = re.sub(r"#[\w]+","",line)
			line = re.sub(r"@[\w]+","",line)
			line = re.sub('\s+',' ', line)
			write_f.write(line+"\n")
			
	print i+" file done"
	write_f.close()