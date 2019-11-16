# Recce
    v.2.1
Domain Availability Checker 

# !What is this tool?
It was my personal script that i have been using during my recon in bug bounties that check status of domain whethter they are alive or not.
It uses curl to request domain and check the status of given domain.
Making it public so anyone in community can find it helpful! :)

# !Screenshot

![recce](https://user-images.githubusercontent.com/48474764/63941389-2749f780-ca89-11e9-87ec-7ba288119947.png)

# !Features
1) Multithreaded
2) scan 11k domains in just 3 minutes
3) Server detection
4) response length

# !Prerequesites
1) Tool only works on linux/unix
2) curl (preinstalled in almost every linux)
3) python3..You can download and install from here [https://www.python.org/downloads/](url)
4) pycurl,requests, concurrent.futures,ssl these python libraries must be installed in machine.

# !Installation
1) `git clone https://github.com/unstabl3/recce.git`
2) `cd recce`
3) `chmod +x recce.py`
4) `pip install -r requirements.txt`
# Note:If you are using two versions of python use pip3

# !How to use?
1) Scan domains with input as file! 

`python3 recce.py -f filename.txt`

2) Check single domain!

`python3 recce.py -u example.com`

3) Writing output in file!

`python3 -f filename.txt -o result.txt`

4) Verbose mode(to check status of live domain) and number of threads!

`python3 -f filename.txt -o result.txt -t 100 -v`

5) only print live subdomains(does not write output in file)!

`python3 -f filename.txt -l`

6) Server detection(does not work with -l)

`python3 -f filename.txt -t 300 -s -v`

7) print response body length!(only works with -s)

`python3 -f filename.txt -t 300 -s -r -v`

8) write output in csv format!

`python3 -f filename.txt -t 300 -s -r -v -c result.csv`

# v2.0
    `# using pycurl rather than calling system shell
     # server detection
     # can only print live subdomains without writing output into the file.
     # can now print response body length
     # can write output in csv format.
     # proper output screen`

# v1.0
    `# multithreaded
     # scan 11k domains in 3 min.`
     
# !Credits!
To the Whole infosec Community ;)

@athif shaikh for suggesting this great name! :3

# !Want to contribute?
1) Suggest a feature 

# !License
Licensed under the MIT License!
