import database as db
import sms as Sms

# git name of the project would be same as project name
project_name=input("Enter Project name :: ")

# calling project create function from the database
db.make_folder(project_name)

# all data of students is needed
data=db.file_read()

# get all data from github
db.get_code(project_name,data)

# getting all desired outputs
outputs=db.read_outputs()

file_name=input("Name of file to run(without py) :: ")

# run all codes
data=db.run_code(data,project_name,file_name,outputs)

# sending sms
Sms.send_sms(data)