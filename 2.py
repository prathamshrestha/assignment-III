import json
import time


def ITAcademy():
    i = 1
    while (i != 0):
       
        print('1.Course Enquiry\n2.Student Payment related information\n3.Enrolled into course\n4.Update Student info\n5.Delete Student info\n6.Money Return on course completion\n0.Exit Application')
        num = int(input('enter a no. you want to approach a service     '))
        if (num == 1):
            print('Course Enquiry')
            fo = open(
                'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'r')
            info = json.load(fo).get('courses')
            print(info['Python'])
            print(info['PHP'])
            print(info['Backend Django'])
            print(info['Machine learning'])
            print(info['FrontEnd'])
            fo.close()
           

            continue
        if (num == 2):
            print(
                '    Student Payment information   ')

            fo = open(
                'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'r')
            id_std = input('please enter your student id: ')
            info = json.load(fo).get('student')
            if id_std in list(info.keys()):
                info_std = info.get(id_std)
                print(
                    f'Student Name:{info_std["name"]}\nCourse Enrolled: {info_std["course"]}\nPayment Made: Rs {info_std["payment"]}')
            else:
                print("you are not enrolled")
                fo.close()
            
            continue
        elif (num == 3):
          
            course = {"1": "Python", "2": "PHP", "3": "Backend django",
                      "4": "Machine Learning", "5": "FrontEnd"}
            for i, j in course.items():
                print(i, ".", j)
            choice = input('Enter above course you want to register: ')
            print(course.get(choice))
            if course.get(choice):
                fo = open(
                    'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'r')

                file = json.load(fo)
                # print(file)
                std_file = file['student']

                name = input('please enter your name')
                amount = int(input(
                    'Pay the amount 2500 in two installement\nyou can pay 1st installment 1500:'))
                if amount == 1500 or amount == 2500:
                    new_id = max([int(i) for i in std_file.keys()])
                    print(new_id)
                    new_id = new_id + 1
                    std_file[str(new_id)] = {"name": name,
                                             "payment": amount,
                                             "returned": 0,
                                             "course": course.get(choice),
                                             "course_status": [1 if amount == 1500 else 2][0]}
                    print(std_file)
                    file['student'] = std_file
                    fa = open(
                        'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'w')
                    json.dump(file, fa, indent=4)
                    fa.close()
                    fo.close()
                   
                    continue
                else:
                    print(
                        'please pay and move forward!!!\n Payment must not greater than 2500')
                    
                    continue
        elif (num == 4):
           

            fo = open(
                'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'r')
            file = json.load(fo)
            info = file.get('student')
            print('All student_id', list(info.keys()))
            id_std = input('please enter your student id: ')

            if id_std in list(info.keys()):
                info_std = info.get(id_std)
                print(
                    f'Student Name:{info_std["name"]}\nCourse Enrolled: {info_std["course"]}\nPayment Made: Rs {info_std["payment"]}')
                print('please enter change:')
                name = input('please enter name: ')
                payment = input('please enter payment: ')
                course = input('please enter course: ')
                returned = input('please enter returned: ')
                course_status = input('please enter course_status: ')


                info_std["name"] = [name if bool(
                    name) else info_std["name"]][0]
                info_std["payment"] = [int(payment) if bool(
                    payment) else info_std["payment"]][0]
                info_std["course"] = [course if bool(
                    course) else info_std["course"]][0]
                info_std["returned"] = [returned if bool(
                    returned) else info_std["returned"]][0]
                prev_status = info_std["course_status"]
                info_std["course_status"] = [int(course_status) if bool(course_status) else info_std["course_status"]][
                    0]
                info_std["course_status"] = [info_std["course_status"] if (
                    3 >= info_std["course_status"] >= 1) else prev_status][0]

                print(info_std)

                info[id_std] = info_std
                file['student'] = info
                print(file)
                fa = open(
                    'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'w')
                json.dump(file, fa, indent=4)
                fo.close()
                fa.close()
                
                continue
            else:
                print(' id incorrect Please enter correct student id!!!')
                
                continue
        elif (num == 5):
          

            fo = open(
                'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'r')
            file = json.load(fo)
            info = file.get('student')
            print('All student_id', list(info.keys()))
            id_std = input('please enter your student id: ')

            if id_std in list(info.keys()):
                if info[id_std]['payment'] == 2500:
                    info.pop(id_std)

                    print(info)

                    file['student'] = info
                    print(file)
                    fa = open(
                        'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'w')
                    json.dump(file, fa, indent=4)
                    fo.close()
                    fa.close()
                   
                    continue
                else:
                    print("this student haven't paid complete amount")
                  
                    continue
            else:
                print(
                    'Please enter correct student id!!!')
               
                continue
        elif (num == 6):
           

            fo = open(
                'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'r')
            file = json.load(fo)
            info = file.get('student')
            print('All student_id', list(info.keys()))
            id_std = input('please enter your student id: ')

            if id_std in list(info.keys()):
                if info[id_std]['course_status'] == 3:
                    info[id_std]['returned'] = '2500'
                    print( " you completed the course ")
                    print(" Your amount has been returned")
                    
                    print(info)

                    file['student'] = info
                    print(file)
                    fa = open(
                        'C:\\Users\\Pratham\\OneDrive\\Documents\\python assignment III\\data.json', 'w')
                    json.dump(file, fa, indent=4)
                    fo.close()
                    fa.close()
                    
                    continue
                else:
                    print("this student haven't paid complete amount")
                    
                    continue
            else:
               
                print('Please enter correct student id!!!')
               
                continue
        elif (num == 0):
            i = num
            print('Thank u for using our service')
           
            return


if __name__ == "__main__":
    ITAcademy()