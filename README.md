# Generate Passwords BruteForce - Python

A Python module to generate all the possible combination of passwords for performing brute force method.

## Installation: 
Using git
```shell
git clone https://github.com/MexsonFernandes/Generate_Passwords_Brute_Force-Python.git
```
Or download and extract the archive:
<img style="float: right;" src="assets/clone-repo-button.png" alt="Clone or download" />
Under the repository name, click Clone or download -> Download ZIP. 
Unpack the ZIP. 

## Usage:
main.py takes 4 arguments: 
  * number of password character
  * alphabets (y/n)
  * special characters (y/n)
  * numbers (y/n)

This generates a wordslist.txt and a logs.txt file. 

If we wanted to generate all possible combinations of passwords 4 characters long, containing lower- and uppercase letters, special characters and numbers we would run: 
```shell
python main.py 4 y y y
```
In this case the output is saved in wordslist4.txt and logs4.txt. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
