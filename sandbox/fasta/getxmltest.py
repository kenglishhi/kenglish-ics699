
import sys
sys.path.append('/home/kenglish/workspace/kenglish-ics699/www/biotoolspylons')
#sys.path.append('/home/kenglish/workspace/kenglish-ics699/sandbox/blast_tests')

from biotoolspylons.lib.base import *
from biotoolspylons.model import fastafile
from biotoolspylons.model import miniblast
from biotoolspylons.model.pathinfo import *




def getXML(obj, objname=None):
    """getXML(obj, objname=None)
    returns an object as XML where Python object names are the tags.
    
    >>> u={'UserID':10,'Name':'Mark','Group':['Admin','Webmaster']}
    >>> getXML(u,'User')
    '<User><UserID>10</UserID><Name>Mark</Name><Group>Admin</Group><Group>Webmaster</Group></User>'
    """
    if obj == None:
        return ""
    if not objname:
        objname = "Deepdesk"
    adapt={
        dict: getXML_dict,
        list: getXML_list,
        tuple: getXML_list,
        }
    if adapt.has_key(obj.__class__):
        return adapt[obj.__class__](obj, objname)
    else:
        return "<%(n)s>%(o)s</%(n)s>"%{'n':objname,'o':str(obj)}

def getXML_dict(indict, objname=None):
    h = "<%s>"%objname
    for k, v in indict.items():
        h += getXML(v, k)
    h += "</%s>"%objname
    return h

def getXML_list(inlist, objname=None):
    h = ""
    for i in inlist:
        h += getXML(i, objname)
    return h


hash = {"GLY" : "G", "ALA" : "A", "LEU" : "L", "ILE" : "I"} 
 
print getXML(hash) 



#import Bio.Fasta
#from Bio.Blast import NCBIStandalone
#from Bio.Blast import NCBIXML
#
files = fastafile.get_fasta_files()
for file in files:
    print file.filename
    print getXML(file,'User') 
#    fileinfo = PathInfo(file)
#    print fileinfo

#p = PathInfo("/home/kenglish/downloads/uploads/EST_Clade_A_1.fasta")
#print p

