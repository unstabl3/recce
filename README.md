# Recce
    v.3.0
Domain Availability Checker 

# !What is Recce?
It makes a request to domain/subdomain and checks whether they are alive or not!

# !Screenshot

![recce](https://user-images.githubusercontent.com/48474764/63941389-2749f780-ca89-11e9-87ec-7ba288119947.png)

# !Features
1) Multithreaded
2) scan 11k domains in just 3 minutes
3) Server detection
4) response length
5) slack notification
6) take standard input(like httprobe)

# !Prerequesites
1) recce only tested on linux/unix
2) curl (preinstalled in almost every linux)
3) python3..You can download and install from here [How to download python](https://www.python.org/downloads/)
4) pycurl,requests, concurrent.futures,ssl these python libraries must be installed in machine.


# !Installation
1) `git clone https://github.com/unstabl3/recce.git`
2) `cd recce`
3) `chmod +x recce.py`
4) `sudo bash install.sh`

# Note:If you are using two versions of python use pip3

# Configuration
You have to configure your slack to get updates!

To do so visit here
[How to create slack webhook](https://slack.com/intl/en-in/help/articles/115005265063)

Configure your slack_webhook in config.py file present in the recce.

`slack_webhook = "PUT YOUR WEBHOOK HERE"`

# Usage
`usage: recce_test.py [-h] [-v] [-o out-file | -c csv-file] [-t Threads]`

    [-f Input file | -d domain] [-s] [-u] [-l] [-r] [-F] [-S]

    optional arguments:

    -h, --help            show this help message and exit
  
    -v, --verbose         verbose

    -o out-file, --output out-file 
                        write active domains in new file
  
    -c csv-file, --csv csv-file
                        mention .csv file to write output
                        
    -t Threads, --threads Threads
                        number of concurrent threads
                        
    -f Input file, --file Input file
                        File which consist domains(sub.example.com)
                        
    -d domain, --domain domain
                        single domain check
                        
    -s, --server          print web server
  
    -u, --update          update recce
  
    -l, --live            only print live subdomains
  
    -r, --length          print response length
  
    -F, --follow          Follow redirect
  
    -S, --slack           send slack notification`


# !How to use?

[~] Fastest way!

`cat subdomains.txt | recce -l`

[~] sending data to slack!

`cat subdomains.txt | recce -l -S`

[~] writing data and sending to the slack

`cat subdomains.txt | recce -l -S -o result.txt`

[~] Follow redirect and save locally

`cat subdomains.txt | recce -l -F -o result.txt`

[~] Scan domains with input as file! 

`recce -f filename.txt`

[~] Check single domain!

`recce -u example.com`

[~] Writing output in file!

`recce -f filename.txt -o result.txt`

[~] Verbose mode(to check status of live domain) and number of threads!

`recce -f filename.txt -o result.txt -t 100 -v`

[~] only print live subdomains(does not write output in file)!

`recce -f filename.txt -l`

[~] Server detection(does not work with -l)

`recce -f filename.txt -t 300 -s -v`

[~] print response body length!(only works with -s)

`recce -f filename.txt -t 300 -s -r -v`

[~] write output in csv format!

`recce -f filename.txt -t 300 -s -r -v -c result.csv`

# v3.0
     # slack notification
     # follows redirect
     # can now take standard input
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
To the Whole infosec Community :3

@athif shaikh for suggesting this great name! :3

# !Want to contribute?
Do a pull request! 

# !License
Licensed under the MIT License!

# Disclaimer

This project is made for educational and ethical testing purposes only. Usage of this tool for attacking targets without prior mutual consent is illegal. Developer assume no liability and are not responsible for any misuse or damage caused by this tool.
