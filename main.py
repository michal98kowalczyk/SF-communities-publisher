import shlex
import sys
import publisher


ORG_NAME_PARAM = "org"

def getOrg(args):
    orgFound = False
    for arg in args:
        if ORG_NAME_PARAM in arg:
            orgFound = True
            return arg.split("=")[1]
    
    if not orgFound:
        raise Exception("ORG must be specified, please use following pattern org=yourOrgName") 


def readArguments():
    return getOrg(sys.argv)


def main() -> int:
    org = readArguments()
    print('\n###### We are running commands in context of {org} #######\n\n'.format(org=org))

    myPublisher = publisher.Publisher(org)
    myPublisher.publish()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())