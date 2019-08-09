# recce
    v.1.0
domain availability checker 

# !What is this tool?
It was my personal script that i have been using during my recon in bug bounties that check status of domain whethter they are alive or not.
It uses curl to request domain and check the status of given domain.
Making it public so anyone in community can find it helpful! :)

# !Screenshot

![recce](https://user-images.githubusercontent.com/48474764/62758624-9771e880-ba9c-11e9-9497-93bdea350ef5.png)


# !Features
1) Multithreaded
2) scan 11k domains in just 3 minutes 

# !Prerequesites
1) Tool only works on linux/unix
2) curl (preinstalled in almost every linux)
3) python3..You can download and install from here [https://www.python.org/downloads/](url)

# !Installation
1) `git clone https://github.com/unstabl3/recce.git`
2) `cd recce`
3) `chmod +x recce.py`

# !How to use?
1) Scan domains with input as file! 

`python3 recce.py -f filename.txt`

2) Check single domain!

`python3 recce.py -u example.com`

3) Writing output in file!

`python3 -f filename.txt -o result.txt`

4) Verbose mode(to check status of live domain) and number of threads!

`python3 -f filename.txt -o result.txt -t 100 -v`

# !Credits!
To the Whole infosec Community ;)

# !Want to contribute?
1) Suggest a feature 

# !License
Licensed under the MIT License!
