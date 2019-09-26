This is SENG2011!

Steps to get Dafny 1.9.7.XX.. working on your local machine (Linux).

	1)	mkdir se2011; git clone git@github.com:FaizAther/def-ny_se2011.git
	2)	cd dafny/
	3)	chmod +x dafny
	4)	chmod +x Dafny.exe
	
	[-- INSTALlING INSTRUCTIONS mono-project LINUX-DEBIAN-9
	    refer to
	    https://www.mono-project.com/download/stable/#download-lin-debian
	    for other Linux Distro --]
	
	5)	sudo apt install apt-transport-https dirmngr gnupg ca-certificates
	6)	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
	7)	echo "deb https://download.mono-project.com/repo/debian stable-stretch main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
	8)	sudo apt update; sudo apt install mono-devel

	[-- END OF mono-project INSTALL INSTRUCTIONS --]

	9)	cd ../; echo 'method Main() {print "hello, Dafny\n";assert 10 > 2;}' >>test.dfy
	
	[-- Add path to the dafny folder in my case this is the path. ~=$HOME #home folder. --]

	10)	PATH=$PATH:~/Documents/se2011/dafny

	[-- OPTIONAL STEP 11: Permanently add path to bash #your path may vary --]
	
	11)	echo "PATH=$PATH:~/Documents/se2011/dafny" >> ~/.bashrc

	12)	dafny test.dfy
	13)	./test.exe

	[-- It should print "hello, Dafny\n" --]

End-of-text.
