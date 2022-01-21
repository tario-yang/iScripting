'''
    This script is to remove useless directories from Nexus repository.
'''
import os
import shutil

def returnFlagString(i):
    x = i.split('.')
    return '{0}.{1}.{2}'.format(x[0], x[1], x[2])

def formatString(i):
    x = i.split('.')
    x[-1] = x[-1].rjust(4, '0')
    return '.'.join(x)

def changeBackString(i):
    x = i.split('.')
    x[-1] = str(int(x[-1]))
    return '.'.join(x)

# for Maven VM
# '/home/ubuntu/nexus/nexus/sonatype-work/nexus/storage/servicemax-external/com/intalio/cloud/core'
# for backupVM
__PATH__ = '/media/Castor/nexus/nexus/sonatype-work/nexus/storage/servicemax-external/com/intalio/cloud/core'

if not os.path.exists(__PATH__):
    exit(1)

for (root, dirs, files) in os.walk(__PATH__):
    break

print "\nTotal directories which needs to be dealed with >>> {0}\n".format(len(dirs))

# each subDir is a module, there are different version directories in it.
for subDir in dirs:
    currentDir = '{0}/{1}'.format(root, subDir)
    print 'current working directory is {0}.'.format(currentDir)

    for (r, d, f) in os.walk(currentDir):
        break

    # ignore if directory number is less than 10
    if len(d) <= 10:
        print "(ignored since total number is NOT greater than 10.)\n"
        continue

    Result = []
    tmpLst = []
    flag = ''

    # generate working list for currentDir, it will be [[],[],...[]]
    d.sort()
    for i in d:
        i = formatString(i)
        if flag != returnFlagString(i):
            flag = returnFlagString(i)
            if len(tmpLst) != 0:
                tmpLst.sort()
                Result.append(tmpLst)
            tmpLst = []
        tmpLst.append(i)

    # this is for the last flag
    tmpLst.sort()
    Result.append(tmpLst)

    # generate deletion list
    for subResult in Result:
        print "Current list is,\n{0}.\nTotal number >>> {1}".format(subResult, len(subResult)),
        if len(subResult) <= 10:
            print " (ignored since number is NOT greater than 10.)\n"
            continue
        else:
            print
        for j in range(10):
            subResult.pop()

        for k in range(len(subResult)):
            subResult[k] = changeBackString(subResult[k])

        print "Deletion list is,\n{0}\nNumber >>> {1}\n".format(subResult, len(subResult))

        # execute `delete` according to deletion list
        print "Will delete the followings,"
        for l in subResult:
            delPath = "{0}/{1}".format(currentDir, l)
            print ">>>>>> {0}".format(delPath),
            if os.path.exists(delPath):
                print " - existed - ",
            try:
                shutil.rmtree(delPath)
            except OSError:
                print "[FAIL] (OS ERROR)"
            except IOError:
                print "[FAIL] (IO ERROR)"
            else:
                print "[PASS]"
        print
