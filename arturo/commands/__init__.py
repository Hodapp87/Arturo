#  _____     _               
# |  _  |___| |_ _ _ ___ ___ 
# |     |  _|  _| | |  _| . |
# |__|__|_| |_| |___|_| |___|
# http://32bits.io/Arturo/
#

import inspect
import string
import sys
import textwrap

from arturo import __app_name__
import arturo
from arturo.commands.base import Command, ProjectCommand, ConfiguredCommand
from arturo.commands.build import Cmd_preprocess, Cmd_source_headers, Cmd_source_files, Cmd_d_to_p, Cmd_mkdirs, Cmd_source_libs, Cmd_lib_source_files, Cmd_lib_source_headers
from arturo.commands.makegen import Cmd_makegen_noexpand, Cmd_makegen
from arturo.commands.prebuild import Cmd_init, Cmd_version
from arturo.commands.query import Cmd_commands, Cmd_list_boards, Cmd_list_tools, Cmd_list_platform_data, Cmd_list_libraries, Cmd_which_lib


def _is_concrete_command_subclass(commandClass):
    if inspect.isclass(commandClass) and issubclass(commandClass, Command) and commandClass != Command and not inspect.isabstract(commandClass):
        return True
    else:
        return False


def getAllCommands():
    '''
    Returns a dictionary of class names to class objects for all Command subclasses in the commands module.
    '''
    module = sys.modules[__name__]
    
    if not hasattr(module, "_commands"):
        # commands is a list of name, value pairs sorted by name
        commands = inspect.getmembers(module, _is_concrete_command_subclass)
        module._commands = {Command.command_class_to_commandname(commandClass): commandClass for name, commandClass in commands}  # @UnusedVariable
    return module._commands

def getDefaultCommand(environment, commandName, console=None):
    module = sys.modules[__name__]
    
    if not hasattr(module, "_commandObjects"):
        module._commandObjects = dict()
    
    try:
        return module._commandObjects[commandName]
    except KeyError:
        commandClass = getAllCommands()[commandName]
        if console is None:
            console = environment.getConsole()
        if issubclass(commandClass, ProjectCommand):
            #TODO: allow explicit project to be provided
            project = environment.getInferredProject()
    
            if issubclass(commandClass, ConfiguredCommand):
                #TODO: allow explicit configuration to be provided
                command = commandClass(environment, project, project.getLastConfiguration(), console)
            else:
                command = commandClass(environment, project, console)
        else:
            command = commandClass(environment, console)
        
        module._commandObjects[commandName] = command
        return command