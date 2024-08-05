import shutil
import time, os, glob
class FileOperation():

    def do_operation_on_all_files(self,target_dir,operation,operation_arguments):
        print("operation= %s"%operation)
        all_names=glob.glob(target_dir+'/*')
        for file_name in all_names:
            operation(file_name,target_dir,operation_arguments)
            pass
    def print_name(self,file_name,target_dir):
        print(file_name)

    def rename(self,file_name:str,target_dir):
        no_specific_char=file_name.replace("-","_")
        os.rename(file_name,no_specific_char)

    def print_change_time(self,file_name,target_dir):
        ti_m=os.path.getmtime(file_name)
        c_ti = time.ctime(ti_m)
        print(c_ti)

    def archive_file_by_mtime(self,file_name,target_dir,archive_dest_root_dir):
        ti_m=os.path.getmtime(file_name)
        #c_ti = time.ctime(ti_m)
        date_modified_obj  = time.localtime(ti_m)
        modified_month=date_modified_obj.tm_mon
        modified_year=date_modified_obj.tm_year
        archive_dest=archive_dest_root_dir+'/'+str(modified_year)+'_'+str(modified_month)
        if not os.path.isdir(archive_dest):
            os.mkdir(archive_dest)
        shutil.move(file_name,archive_dest)

    def ensure_archive_correctness(self,file_name:str,target_dir:str,archive_dest_root_dir):
        #
        target_dir_base_name=os.path.basename(target_dir).split('.')[0]
        target_dir_month=target_dir_base_name.split('_')[1]
        target_dir_year=target_dir_base_name.split('_')[0]

        #
        ti_m=os.path.getmtime(file_name)
        #c_ti = time.ctime(ti_m)
        date_modified_obj  = time.localtime(ti_m)
        modified_month=str(date_modified_obj.tm_mon)
        modified_year=str(date_modified_obj.tm_year)

        if target_dir_year!=modified_year or target_dir_month!=modified_month:
            print("file %s is in incorrect archive, moving it to the correc archive%s..."%(file_name,archive_dest_root_dir+'/'+str(modified_year)+'_'+str(modified_month)))
            archive_dest=archive_dest_root_dir+'/'+str(modified_year)+'_'+str(modified_month)
            if not os.path.isdir(archive_dest):
                os.mkdir(archive_dest)
            shutil.move(file_name,archive_dest)

f=FileOperation() 


dir='./sample'
all_names=glob.glob(dir)
for name in all_names:
    f.do_operation_on_all_files(target_dir=name,operation=f.archive_file_by_mtime,operation_arguments='.')