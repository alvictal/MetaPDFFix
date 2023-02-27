# MetaPDFFix
Simple tool to correct wrong pdf metadata that make some pdfreaders not open the a file (Python 3.11 version) 

## How to install the dependencies
You can use the devcontainer app (vscode extension is recomended) to avoid any package installation on your machine.
If you prefer to install the dependencies direct into your machine, just insert the command below in the main folder
```
pip3 install --user -r requirements.txt
```

## Using the MetaPDFFix Scprit 
 You can download all pdf files with meta issues and add to your prefered folder. The script will gather any pdf inside the folder and try to fix
 the metadata without change the content of the file
 
 `Example of usage:`
 ```
 python MetaPDFFix.py --input-dir=test/
 ```
 
 You don't need to set the output directory, the script will create a new one in the same folder where the script is located. But if you prefer you can setting up using --output-dir= 

```
 python MetaPDFFix.py --input-dir=test/ --output-dir=my_new_files/
 ```
