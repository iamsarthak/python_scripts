import os
import sys

def move(extension,source,destination):
	source_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),source)
	destination_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),destination)
	list_files=os.listdir(source_path)
	print(source_path)
	print(destination_path)
	print(list_files)
	for i in list_files:
		source_path=os.path.join(source_path,i)
		print(source_path)
		print(destination_path)
		if os.path.isfile(source_path):
			file_ext=i.split('.')[-1]
			file_name=i.split('/')[-1]
			if file_ext==extension:
				os.rename(source_path+'',destination_path+'/' +file_name)
		else:
			move(extension,source_path,destination)
						
move(sys.argv[1],sys.argv[2],sys.argv[3])
