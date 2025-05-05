with open("file1.txt", "r") as fh1:
    with open("file2.txt", "r") as fh2:
        with open("mergefile.txt", "w") as fh3:
            # Read all lines from both files and combine them into a list 'q'
            q = fh1.readlines() + fh2.readlines()
            
            # Write the combined lines into the output file 'mergefile.txt'
            fh3.writelines(q)
