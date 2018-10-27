

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.courses = []
        self.students = []
        self.Teacher = []
        self.classroom = []

    def  create_course(self,course_type,price,time):#创建课程
        Course(course_type, price, time)
        self.courses.append(Course(course_type,price,time))
    def login_student(self,name,age,sex):#注册学生

        self.students.append(Studnet(name,age,sex))
    def login_Teacher(self,name,age,sex):#注册教师
        name = Teacher(name,age,sex)
        self.Teacher.append(name)
    def create_class(self,id):#创建班级
        self.classroom.append(Classroom(id))
class SchoolMember(object):  #学校人员类
    def __init__(self,name,age,sex):
        self.name = name
        self.age  = age
        self.sex  = sex
class Studnet(SchoolMember): #学生类
    def __init__(self,name,age,sex):
        super(Studnet,self).__init__(name,age,sex)
    def pay_tuition(self):
        pass
    def choose_class(self):
        pass
class Teacher(SchoolMember,School): #教师类
    def __init__(self,name,age,sex):
        self.tea_classroom =[]
        super(Teacher,self).__init__(name,age,sex)
    def pay_tuition(self):
        pass
    def choose_class(self):
        pass
class Classroom(object):   #班级类
    def __init__(self,id):
        self.id = id
        self.class_stu = []
        self.class_cour = []
    def plus_stu(self,stu_obj):
        self.class_stu.append(stu_obj)

    def plus_cour(self,course):
        self.class_cour.append(course)


class Course(object):     #课程类
    def __init__(self,name,price,time):
        self.name = name
        self.price = price
        self.time = time


s1 = School("希望小学","北京")
s2 = School("联合小学","上海")
s1.create_course("python",1000,"2018年5月2日")
print(s1.courses[0])
print(s1.courses[0].name)

i = 1
j = 1
while(i):

    a = input('''
                    1.学生入口
                    2.教师入口
                    3.管理员入口''')


    if a == "1":   #学生界面入口
        while(j):
            b = input('''
                        1.注册
                        2.交学费
                        3.选择班级''')

            if b == "1":    #注册
                stu_name = input("姓名:")
                stu_age = input("年龄:")
                stu_sex = input("性别:")
                school = input("选择学校:1.%s 2.%s" % (s1.name, s2.name))
                if school == "1":
                    s1.login_student(stu_name, stu_age, stu_sex)
                    for n in s1.students:
                        print(n.name)
                elif school == "2":
                    for n in s2.students:
                        print(n.name)




            elif b == "2":#学生交学费
                pass

            elif b == "q":
                break



            elif b == "3":  #学生选择班级

                for i ,val in enumerate(s1.classroom,1):
                    print(i,"班级%s:"%val.id)

                cho_classid = input("选择班级编号:")
                stu_name = input("输入学生姓名:")
                #print(s1.classroom)
                s1.classroom[int(cho_classid)-1].plus_stu(stu_name)
                # s1.classroom.index(int(cho_classid)-1).plus_stu(stu_name)
                # print(s1.classroom.index(int(cho_classid)+1))
                for i in s1.classroom[int(cho_classid)-1].class_stu:
                    print(i)


            else:
                print("请选择正确的输入")
                continue
                j= 1  #学生接口结束
    elif a == "2": #教师界面入口
        while (j):
            b = input('''
                                1.管理自己班级
                                2.上课时选择班级
                                3.查看班级学员列表
                                4.修改学员成绩''')

            if b == "1":  # 管理班级
                stu_name = input("姓名:")
                stu_age = input("年龄:")
                stu_sex = input("性别:")
                school = input("选择学校:1.%s 2.%s" % (s1.name, s2.name))
                if school == "1":
                    s1.login_student(stu_name, stu_age, stu_sex)
                    for n in s1.students:
                        print(n.name)
                elif school == "2":
                    for n in s2.students:
                        print(n.name)




            elif b == "2":  # 上课时选择班级
                pass

            elif b == "q":
                break



            elif b == "3":  # 查看班级学员列表

                for i, val in enumerate(s1.classroom, 1):
                    print(i, "班级%s:" % val.id)

                cho_classid = input("选择班级编号:")
                stu_name = input("输入学生姓名:")
                # print(s1.classroom)
                s1.classroom[int(cho_classid) - 1].plus_stu(stu_name)
                # s1.classroom.index(int(cho_classid)-1).plus_stu(stu_name)
                # print(s1.classroom.index(int(cho_classid)+1))
                for i in s1.classroom[int(cho_classid) - 1].class_stu:
                    print(i)
            elif b == "4":  # 修改学员成绩
                pass
            else:
                print("请选择正确的输入")
                continue
                j = 1  # 学生接口结束
    elif a == "3":  #管理员接口入口

            while (j):
                b = input('''
                            1.创建讲师
                            2.创建班级
                            3.创建课程''')
                if b == "1":     #创建讲师
                    tea_name = input("姓名:")
                    tea_age = input("年龄:")
                    tea_sex = input("性别:")
                    school = input("选择学校:1.%s 2.%s" % (s1.name, s2.name))
                    if school == "1":
                        s1.login_Teacher(tea_name,  tea_age, tea_sex)
                        for n in s1.Teacher:
                            print(n)


                    elif school == "2":
                        for n in s2.Teacher:
                            print(n.name)




                elif b == "2":#创建班级
                    school = input("选择学校:1.%s 2.%s" % (s1.name, s2.name))
                    classid = input("输入创建班级id:")
                    if school == "1":
                        s1.create_class(classid)
                        for n in s1.classroom:
                            print(n.id
                                  )
                    elif school == "2":
                        s2.create_class(classid)
                        for n in s2.classroom:
                            print(n.id)
                elif b == "3":
                    input("选择班级:")
                elif b == "q":
                    break
                else:
                    print("请选择正确的输入")
                    continue
                    j = 1
    else:
        print("请选择正确的输入")
        continue
        i = 1






