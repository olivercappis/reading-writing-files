def main():
    infile = open('clients.txt', 'r')
    
    i = 0

    for line in infile:
       newline = line.rstrip('\n')
       i += 1 
       print(f'{i}. {newline}')
main()