'''
helper script to group files into folders based on their last modified date.
'''
import shutil
import sys
import time
import os
import glob
import getopt
INPUT_DIR = './input'
class FileOperation():
    '''
    class holding several function
    '''
    def __init__(self) -> None:
        self.input_dir=INPUT_DIR
    def do_operation_on_all_files(self, target_dir, operation, operation_arguments):
        '''
        runner with callback
        '''
        #print("operation= %s" % operation)
        all_names = glob.glob(target_dir+'/*')
        for file_name in all_names:
            operation(file_name, target_dir, operation_arguments)
            pass

    def archive_file_by_mtime(self, file_name, target_dir, archive_dest_root_dir):
        ti_m = os.path.getmtime(file_name)
        # c_ti = time.ctime(ti_m)
        date_modified_obj = time.localtime(ti_m)
        modified_month = date_modified_obj.tm_mon
        modified_year = date_modified_obj.tm_year
        archive_dest = archive_dest_root_dir+'/' + \
            str(modified_year)+'_'+str(modified_month)
        if not os.path.isdir(archive_dest):
            os.mkdir(archive_dest)
        try:
            shutil.move(file_name, archive_dest)
            print(f"moved {file_name} to {archive_dest}")
        except shutil.Error as e: 
            print(e)

    def ensure_archive_correctness(self, file_name: str, target_dir: str, archive_dest_root_dir):
        target_dir_base_name = os.path.basename(target_dir).split('.')[0]
        target_dir_month = target_dir_base_name.split('_')[1]
        target_dir_year = target_dir_base_name.split('_')[0]

        #
        ti_m = os.path.getmtime(file_name)
        # c_ti = time.ctime(ti_m)
        date_modified_obj = time.localtime(ti_m)
        modified_month = str(date_modified_obj.tm_mon)
        modified_year = str(date_modified_obj.tm_year)

        if target_dir_year != modified_year or target_dir_month != modified_month:
            print("file %s is in incorrect archive, moving it to the correc archive%s..." % (
                file_name, archive_dest_root_dir+'/'+str(modified_year)+'_'+str(modified_month)))
            archive_dest = archive_dest_root_dir+'/' + \
                str(modified_year)+'_'+str(modified_month)
            if not os.path.isdir(archive_dest):
                os.mkdir(archive_dest)
            shutil.move(file_name, archive_dest)

if __name__=='__main__':

    f = FileOperation()

    opts, args = getopt.getopt(sys.argv[1:], "o", [
                           "--organize"])
    
    call_back=f.archive_file_by_mtime
    all_names = glob.glob(INPUT_DIR)
    for opt, arg in opts:
        if opt in ("-o", "--organize"):
    
        
            all_names = glob.glob('20*')
            call_back=f.ensure_archive_correctness
     
            
    
    for name in all_names:
        f.do_operation_on_all_files(
                    target_dir=name, operation=call_back, operation_arguments='.')