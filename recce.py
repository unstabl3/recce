#!/usr/bin/env python3

import os
import sys
import platform
import time

ver = platform.python_version()

if (ver <= '3'):
        print("\033[91m Breakfold isn't compatible with python2 use python 3.x\033[00m")
        sys.exit(1)

import argparse
import concurrent.futures

parser = argparse.ArgumentParser(description="""\033[93m[~] Domain status checker by shubham chaskar
									https://twitter.com/chaskar_shubham\033[00m""")

group = parser.add_mutually_exclusive_group()
												#Taking arguments from CLI
parser.add_argument("-v","--verbose", help="verbose",action="store_true")

parser.add_argument("-o","--output", help="write active domains in new file" ,metavar='out-file')

parser.add_argument("-t","--threads", help="number of concurrent threads" ,type=int,metavar="Threads")

group.add_argument("-f","--file", help="File which consist domains(sub.example.com)",metavar="Input file")

group.add_argument("-u","--url", help="single domain check",metavar="URL")

args = parser.parse_args()

verbose = args.verbose
file = args.file
url = args.url
output = args.output
threads = args.threads

										#Just A fancy banner!
print("""\033[91m
.______       _______   ______   ______  _______
|   _  \     |   ____| /      | /      ||   ____|
|  |_)  |    |  |__   |  ,----'|  ,----'|  |__
|      /     |   __|  |  |     |  |     |   __|
|  |\  \----.|  |____ |  `----.|  `----.|  |____
| _| `._____||_______| \______| \______||_______|\033[00m

					\033[93m v1.0 By shubham_chaskar\033[00m
""")


if verbose:
	print("\033[93m[~] Verbosity is enabled..\033[00m")

if not threads:										#default number of threads
	threads = 20

t = time.time()

def recce(domain):
												#This function will make request to domain
	check = "curl -I " + domain + " -s -m 15 --write-out %{http_code} --output /dev/null"

	answer = os.popen(check)

	result = answer.read()

	return result


def check(data,domain):
												#This function will compare result
	if (data == "000"):

		print("\033[91m[!] Domain " , domain[:-1] ," is Down..\033[00m")
	else:
		if verbose:
			print("\033[92m[~] Domain " , domain[:-1] , " is live with status code: " , data, "\033[00m")
		else:
			print("\033[92m[~] Domain " , domain[:-1] , " is live \033[00m")
		if output:
			with open(output,"a") as output_file:						#Writing output to new file
				if verbose:
					print("\033[93m[~] Writing into file..\033[00m")

				output_file.write(domain)

if file:

	if os.path.isfile(file):
		num_domains = 0

		with open(file,"r") as f:
			for domain in f:
				num_domains += 1
		f.close()

		print("\033[92m[~] Total number of domains found in the file are: ", num_domains,"\033[00m")

		with open(file,"r") as f:

			pool = concurrent.futures.ThreadPoolExecutor(max_workers=threads)

		#Start the load operations and mark each future with its domain

			futures = {pool.submit(recce,domain[:-1]):domain for domain in f}

			for future in concurrent.futures.as_completed(futures):
				domain = futures[future]

				try:
					data = future.result()

					check(data,domain)

				except Exception as exc:

					print('%r generated an exception: %s' % (domain, exc))

	else:
		print("\033[91m[!] File not found..\033[00m")
		sys.exit(1)

if url:													#For single domain check
	check = "curl -I " + url + " -s -m 15 --write-out %{http_code} --output /dev/null/"

	answer = os.popen(check)

	if answer.read() == "000":
		print("\033[91m[!] Host ", url, " is down\033[00m")

	else:
		if verbose:
			print("\033[92m[~] Host ", url, "is live with status code: ",answer.read(),"\033[00m")
		else:
			print("\033[92m[~] Host ", url, "is live\033[00m")


print("\033[93m[~] Total time taken: " , time.time() -t , "\033[00m")
