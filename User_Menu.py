import projects_handler
import maain
def afterlog(u_id):
    while True:
        option=input("Project options enter :\n1-create\n2-view \n3-edit \n4-delete  \n5-search \n6-exit\n")
        if option=='1':
            projects_handler.createproject(u_id)
        elif option=='2':
            projects_handler.viewprojects(u_id)
        elif option=='3':
            projects_handler.editproject(u_id)
        elif option=='4':
            projects_handler.delproject(u_id)
        elif option=='5':
            projects_handler.searchproject(u_id)
        elif option == '6':
            exit()
        else:
            print("invalid option")
