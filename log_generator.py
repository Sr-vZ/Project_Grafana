import datetime
import random
import time
import os
from inject_run_id import inject_run_id
# ts = datetime.datetime.now().timestamp().isoformat()
# 
# ts = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
logGenCount = 0
def logGen(logGenCount):
    ts =  datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    ts = str(ts)
    ts = ts.replace('T',' ').replace('.',',')
    # print(ts)

    
    logLine = ts

    tag =['  INFO Performance:270 -',' ERROR Performance:318 - Failed    :']
    errors = [
        ' [action:load-GCD on: Assembly-BASE-PAN_ASM]  GCD not found gcdKey: Assembly-BASE-PAN_ASM.Assembly.5186f6af-39fc-4fe9-9b94-955a5faf31cf.1571252726331',
        ' [action:load-GCD on: Assembly-00005-PS-CAGE-COVER_ASM]  with key: Assembly-00005-PS-CAGE-COVER_ASM.Assembly.528f2044-1eb6-4eb1-9569-0c178c68f6f2.1571252726329',
        ' [action:load-GCD on: Assembly-EG-31708-10H95A_ASM]  GCD not found gcdKey: Assembly-EG-31708-10H95A_ASM.Assembly.b56195dc-c969-437e-b42f-facc84314ee1.1571252726323'
    ]

    status = [' Starting  :',' Completed :']
    action =[
        ' [action:load-GCD on: Assembly-700-32149-01_A0]',
        ' [action:Spatial conversion of assembly and subcopmonents]',
        ' [action:Spatial conversion]',
        ' [action:Spatial part load ]',
        ' [action:load-image on: Assembly-00005-BASE-PAN_ASM]'
        ' [action:save on: Assembly-00005-BASE-PAN_ASM.Initial]'

    ]
    completion = [
        ' used memory:307mb (0) available:5836mb (0) safety margin:5761mb est JVM size:528mb (0) max JVM size:6144mb ',
        ' used memory:416mb (0) available:5727mb (0) safety margin:5652mb est JVM size:528mb (0) max JVM size:6144mb 9_STD-B-DIRVER-PASS_APO6500P',
        ' used memory:423mb (+1) available:5720mb (-1) safety margin:5645mb est JVM size:528mb (0) max JVM size:6144mb 9_SPOOL-BASEPAN-RAIL_S-EAGLE',
        ' used memory:293mb (0) available:5850mb (0) safety margin:5775mb est JVM size:528mb (0) max JVM size:6144mb SPOOL-3MM, area=164.89006955640397'
    ]
    start = [
        ' STEP ASSEMBLY&amp;PARTS k:\\scratch\\rhyde\\flex\\2019-09 escalation\\typical quote assembly\\00005-base-pan_asm.stp using Direct Reader in process',
        ' c:\\users\\kpatel\\appdata\\local\\apriori\\19.2\\tmp\\acis\\work\\1_sm_midplane_bar_btm_tatooine.sab',
        ' with key: Assembly-00005-BASE-PAN_ASM.Web3DImage.null.0',
        ' BASE-PAN',
        ' 9_STD-B-DIRVER-PASS_APO6500P'
    ]
    if logGenCount == 0:
        statusChoice = status[0]
        logLine = ts + tag[0] + statusChoice + random.choice(action) + random.choice(start)
    else:
        tagChoice =  random.choice(tag)
        if tagChoice == tag[1]:
            errorChoice = random.choice(errors)
            logLine = ts + tagChoice + errorChoice
        else:
            if logGenCount%2 == 1:
                statusChoice = status[1]
                duration = ' ('+str(round(random.uniform(0.01,60),2)) +' seconds)' 
                logLine = ts + tag[0] + statusChoice + random.choice(action) + duration +  random.choice(completion)
            else:
                statusChoice = status[0]
                logLine = ts + tag[0] + statusChoice + random.choice(action)
            
    
    logGenCount = logGenCount + 1
    return logLine, logGenCount


N = 1000

logFile = '../telegraf-1.12.3_windows_amd64/telegraf/test.log'
newLogFile = '../telegraf-1.12.3_windows_amd64/telegraf/test_run_id.log'

logFile = './test.log'
newLogFile = './test_run_id.log'
run_id = 1

# entries = os.listdir('./')
# print(entries)
mergedLogfile = './mergedTest.log'

path = './'


with os.scandir(path) as entries:
    for entry in entries:
        # if '.log' in entry.name and not entry.name == logFile.lstrip('./') and not entry.name == newLogFile.lstrip('./'):
        if '.log' in entry.name and 'aprioriPerformance' in entry.name:
            logFile = './' + entry.name
            res = ''.join(filter(str.isdigit, logFile))
            print('Processing.... ', entry.name)
            # print(res)
            if res:
                run_id = res
            else:
                run_id = 0
            inFile = open(logFile, "r")            
            for line in inFile:
                # print(line)
                outFile = open(mergedLogfile, "a")
                outFile.write(line)
                outFile.close()
                inject_run_id(mergedLogfile, newLogFile, run_id)
                
            
            






# for i in range(N):
#     log, logGenCount = logGen(logGenCount)
#     outFile = open(logFile, "a")
#     outFile.write(log+'\n')
#     outFile.close()
#     inject_run_id(logFile, newLogFile, run_id)
#     print(log)
#     time.sleep(random.randrange (100,500,10)/1000)
