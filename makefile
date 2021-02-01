install:
	sudo echo "" > /usr/bin/ipf
	sudo echo "#!/bin/bash" >> /usr/bin/ipf
	sudo echo "python3 /usr/share/ipf/ipf.py \"\$$@\"" >> /usr/bin/ipf
	sudo mkdir /usr/share/ipf -p
	sudo cp ./ipf.py /usr/share/ipf/
	sudo chmod +x /usr/bin/ipf
depens:
	sudo pip3 install bs4
	sudo pip3 install lxml
