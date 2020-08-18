from . import ScribeModuleBaseClass

import sys

#from .lib.util import json

from . lib.util import validate_length

import json
import xmltodict
import re

class Nvidia_smi(ScribeModuleBaseClass):

    def __init__(self, input_dict=None, module_name=None, host_name=None,
                 input_type=None, scribe_uuid=None):
        ScribeModuleBaseClass.__init__(self, module_name=module_name,
                                       input_dict=input_dict,
                                       host_name=host_name,
                                       input_type=input_type,
                                       scribe_uuid=scribe_uuid)

    def parse(self):
        # Regex to find IP Address
        check_ip_address = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        
        #with open('/tmp/stockpile.json', 'r') as fp:
        #    docs = json.load(fp)
        #print(docs["localhost"].keys())i

        output_dict = {}
        for key,value in input_dict.items():

            if key == "localhost":
                output_dict[key] = xmltodict.parse(input_dict['localhost']['stockpile_nvidia_smi']['xml'])

            else:
                isIPaddress = check_ip_address.findall(key)
                if (len(isIPaddress) > 0):
                    # isIPaddress = [“name”, “name2”, . . .]
                    for ip in isIPaddress:
                        output_dict[ip] = xmltodict.parse(input_dict[ip]['stockpile_nvidia_smi']['xml'])
        
        validate_length(len(output_dict), self.module)

        yield output_dict
