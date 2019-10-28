
logFile = 'test_run_id.log'
newLogFile = 'test_run_id.log'

inFile = open(logFile,'r')
outFile = open(newLogFile,'a')

run_id = 0
for line in inFile:
    if line:
        if "Run_ID :" not in line:
            run_id = run_id + 1
            outFile.write(line.rstrip('\n') + " Run_ID : " + str(run_id) + '\n')
        
inFile.close()
outFile.close()