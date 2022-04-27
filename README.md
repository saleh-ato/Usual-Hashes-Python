# Usual Hashes Using Python
This repository contains the usual hash algorithms. I hope it will be useful.
## Hashes
In this repository I have used the usual hash algorithms as follows:

* MD5
* Sha1
* Sha256
* Blake1 512
* Blake 2b
* Blake 2s
* Blake 3
* Grøstl (Groestl)
* Skein 256
* Skein 512
* Skein 1024
* Keccak 256
* GOST
* Whirlpool
* RIPEMD 160
* SM3
## SM3 Hash implemented in python
The sm3 hash that has been implemented in this repository has been used from the source code of the following site due to not finding a suitable Python package.
* [Python implementation of domestic sm3 encryption algorithm](https://www.codestudyblog.com/cnb2105a/0516231809.html "Python implementation of sm3 encryption algorithm")

## Installation
Navigate to one of the folders you want and run the following command in Git, Bash or CMD:

**Note: You must have Git installed on your operating system.**
```bash
git clone https://github.com/saleh-ato/Usual-Hashes-Python
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt:
### Installing packages
```bash
pip install -r requirements.txt
```
**If Any Of Packages Raised Error:**

* **install [Blake512 Hashing library](https://github.com/tweqx/python-blake512)**
## Run The Program
Then you can run the program with the help of the following command:
```python
python hash.py
say something:
> hello
---
which one?:
 1.  md5
 2.  sha1
 3.  sha256
 4.  Blake 1 512
 5.  Blake 2b
 6.  Blake 2s
 7.  Blake 3
 8.  Grøstl (Groestl)
 9.  Skein 256
 10. Skein 512
 11. Skein 1024
 12. Keccak 256
 13. GOST
 14. Whirlpool
 15. RIPEMD 160
 16. SM3
> 1
___________----____________
the  md5 hash of hello is:
5d41402abc4b2a76b9719d911017c592
-----------____------------
```
## Contributing
Pull request is welcome. For any changes, major or minor, please open a topic first to discuss what you want to change.
## License
[MIT](https://github.com/saleh-ato/Usual-Hashes-Python/blob/main/LICENSE)