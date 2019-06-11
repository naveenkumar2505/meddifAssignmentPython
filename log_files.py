def log_Extractor(file):
    file=open(file,'r')
    f1 = open('error.log', 'w+')
    f2 = open('warning.log', 'w+')
    f3=open('another.log','w+')
    read=file.readlines()
    for i in read:
        if 'ERROR' in i:
            f1.write(i)
        elif 'WARNINGS' in i:
            f2.write(i)
        else:
            f3.write(i)
log_Extractor('test.log')