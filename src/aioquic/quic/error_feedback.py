# trace dissector for error report

import json
import os
import sys
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ErrorReport:
    error_type:int
    frame_type: str
    feedback:str
    error:Dict


class QuicErrorReporter:
    def __init__(
        self
    ) -> None :
        print("New error reporter.", file=sys.stderr) #FLUSH
        self.errors_log = list()

    def add_error(self,er:ErrorReport):
        self.errors_log.append(er)

    def write_html(self,path):

        fs = "<!DOCTYPE html><html><body><h1>Error report</h1>\n"
        for err in self.errors_log:
            fs += "<ul><li>Error type : {}</li>".format(err.error_type)
            fs += "<li>Frame type : {}</li>".format(err.frame_type)
            if err.feedback is not None : fs += "<li>Feedback : {}</li>".format(err.feedback)
            fs += "</ul><p>Error report in logfile : {}</p>\n".format(err.error)
        fs += "</body></html>"

        print("Error report written here : {}".format(path), file=sys.stderr) #FLUSH
        with open(path, "w") as fp:
            print(fs,file=fp)
            fp.close()
