#!/bin/sh
version=`which python`
if [ "$1" == "install-python" ]
then
	if [ $version = "/usr/local/bin/python" ]
	then
		wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh 2>/dev/null >/dev/null
		sh Miniconda3-latest-MacOSX-x86_64.sh -b -p ~/goinfre/bootcamp_python/miniconda 2>/dev/null >/dev/null
		export PATH=~/goinfre/bootcamp_python/miniconda/bin:$PATH
​
		rm Miniconda3-latest-MacOSX-x86_64.sh
		echo 'Python has been installed.'
	else
		echo 'Python is already installed, do you want to reinstall it ?'
		echo '[yes|no]> \c'
		read answer
		if [ $answer == "yes" ]
		then
			echo 'Python has been removed.'
			wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh 2>/dev/null >/dev/null
			sh Miniconda3-latest-MacOSX-x86_64.sh -b -p ~/goinfre/bootcamp_python/miniconda 2>/dev/null >/dev/null
			rm Miniconda3-latest-MacOSX-x86_64.sh
			echo 'Python has been installed.'
			presence_zshrc=`grep '^export PATH=' ~/.zshrc`
			presence_miniconda=`grep '^export PATH=~/goinfre/bootcamp_python/miniconda' ~/.zshrc`
			echo "valeur de presence_zshrc = $presence_zshrc"
			echo "valeur de presence_miniconda = $presence_miniconda"
			if [ -z "$presence_zshrc" ] 
			then
				echo  "export PATH=/export PATH=~/goinfre/bootcamp_python/miniconda/bin:$PATH" >> ~/.zshrc
			elif [ -n "$presence_zshrc" ] && [ -z "$presence_miniconda" ]
			then
				sed -i 's/export PATH=/export PATH=~\/goinfre\/bootcamp_python\/miniconda\/bin\:$PATH/g' ~/.zshrc
			fi
		elif [ $answer == 'no' ]
		then
			echo 'exit.'
		fi
	fi
	# if [ -n $presence_miniconda ] && [ $version == 'Python 2.7.4' ]
	# then
	# 	export PATH=~/goinfre/bootcamp_python/miniconda/bin:$PATH
	# fi
fi
