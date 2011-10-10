import ConfigParser
import sys
from UserDict import IterableUserDict

def report_errors(res):
    if 'error' in res:
        for e in res['error']:
            print >> sys.stderr, 'ERROR: ' + e
        return True
    return False

def report_warnings(res):
    if 'warning' in res:
        for e in res['warning']:
            print >> sys.stderr, 'WARNING: ' + e
        return True
    return False

class CommandLineClient(object):
    pass

class DogshellConfig(IterableUserDict):

    def load(self, config_file):
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        self['apikey'] = config.get('Connection', 'apikey')
        self['appkey'] = config.get('Connection', 'appkey')
