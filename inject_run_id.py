
logFile = '../telegraf-1.12.3_windows_amd64/telegraf/test.log'
newLogFile = '../telegraf-1.12.3_windows_amd64/telegraf/test_run_id.log'

def inject_run_id(existinglogFile, newLogFile,run_id):
    inFile = open(existinglogFile,'r')
    outFile = open(newLogFile,'a')
    # for line in inFile:
    #     if line:
    #         if "Run_ID :" not in line:
    #             # run_id = run_id + 1
    #             outFile.write(line.rstrip('\n') + " Run_ID : " + str(run_id) + '\n')
    lineList = inFile.readlines()
    # print(lineList)
    if len(lineList) > 0:
        line = lineList[len(lineList)-1]
    else:
        line = lineList[0]
    # line = lineList[len(lineList)]
    outFile.write(line.rstrip('\n') + " Run_ID : " + str(run_id) + '\n')
    inFile.close()
    outFile.close()
