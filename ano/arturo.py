#!/usr/bin/env python2

import os

from ano.Arduino15.environment import Environment


#  _____     _               
# |  _  |___| |_ _ _ ___ ___ 
# |     |  _|  _| | |  _| . |
# |__|__|_| |_| |___|_| |___|
# http://32bits.io/Arturo/
#
def main():
    print "Start anew"
#     searchPath = SearchPath()
#     anoConsole = Console()
#     print "Search here: ", str(searchPath)
#     packages = Packages(searchPath, anoConsole)
#     print "packages: ", packages.getPackage("arduino")['name']
#     print "build.verbose = %s" % (Preferences(searchPath, anoConsole).get("build.verbose", "(not found)"))
#     arduinoPackage = packages.getPackage('arduino')
#     print "Found package ", arduinoPackage['name']
#     print "Found platforms", str(arduinoPackage.getPlatforms())
#     for platformName, platform in arduinoPackage.getPlatforms().iteritems():
#         print str(platform.getBoards())
#         print str(platform.getProgrammers())
#         print str(platform.getBoards()['yun'].getBuildInfo())
    env = Environment()
    env.getMakefileGenerator('arduino', 'Arduino AVR Boards', 'uno').writeMakefile()
        
    
if __name__ == "__main__" :
    main()