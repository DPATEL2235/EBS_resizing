Here I have attached the outputs of the project which I have implemented 

Before the output we need to feed the data into ec2 instance. As we know that its been difficult or longlasting thing to feed data manually or download it from the internet. So for that I have used below command to feed the data

command : dd if=/dev/urandom of=target-file bs=1M count=1000
        Here dd isa command for copying or converting the data
        if is input file, /dev/urandom which generates the random data, 
           it is unique file in Unix-like os which provides the stream of pseudo-random numbers
        of is output file, random data from inputfile is going to store in it
        bs is blocksize for coping data
        count = 1000 means numbers of copy

Output 1: email to the user (screenshot output_email)
Output 2: extension of the ebs (screenshot output_after)