import logging


permanent_store = '/home/kenglish/downloads/uploads/'
import os, re, shutil 
import bio1.lib.helpers as h
from bio1.lib.base import *
import Bio.Fasta

log = logging.getLogger(__name__)

class BioController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        c.fasta_files = []
        for filename in os.listdir(permanent_store):
            if re.compile('.*fasta$').match(filename):
                c.fasta_files.append( filename ) 
        c.links = [ 'James', 'Ben', 'Philip' ]
        return render('/index.mako')

    def form(self):
        # hello
        return render('/form.mako')

    def email(self):
        return 'Your email is : %s ' % request.params['email']

    def upload(self):
        uploadfile = request.POST['uploadfile']
        fasta_file = open(os.path.join(permanent_store,
                                           uploadfile.filename.lstrip(os.sep)),
                                           'w')

        shutil.copyfileobj(uploadfile.file, fasta_file)
        uploadfile.file.close()
        fasta_file.close()
        handle = open( fasta_file.name )
#        if false:
        it = Bio.Fasta.Iterator(handle, Bio.Fasta.SequenceParser())
        seq = it.next()
        output_string = "" 
        while seq:
            output_string += seq.description 
            output_string += "<br /> " 
            log.debug("seq : %s" ,  seq.description) 
            seq = it.next()
        handle.close()
        self.testmethod()
        self.formatdb(fasta_file.name) 

        log.debug('Hello Kenglish' )
        print "Hello Kenglish" 

        return 'Successfully uploaded: %s, description: %s, <br /> results: <br /> %s ' % \
            (uploadfile.filename, request.POST['description'], output_string)

    def formatdb(self,fasta_file):
        db_name = fasta_file
        cmd = "formatdb -i %s -p F -o F" % fasta_file
        output = os.system(cmd)
        print "output: %s " % output
