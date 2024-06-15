import Backend.Constant as const
from selenium.webdriver.common.by import By
from selenium import webdriver

import threading


class Routine(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Ensure headless option is set correctly
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        super(Routine, self).__init__(options=options)
        self.implicitly_wait(300)  # Adjust implicit wait time as needed
        self.main_list = []
        self.store = []
        print("Initialized WebDriver with headless mode")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
    def thread(self,x):
        # print("Thread", x)
        temporary = []
        courseName = x
        course_list = self.find_elements(By.CSS_SELECTOR, 'td[style="text-align: center; width: 100px"]')
        course_sec = self.find_elements(By.CSS_SELECTOR, 'td[style="text-align: center; width: 69px;"]')
        course_time = self.find_elements(By.CSS_SELECTOR, 'td[style="text-align: center; width: 290px;"]')
        faculty_initials = self.find_elements(By.CSS_SELECTOR, 'td[style="text-align: center; width: 68px;"]')
        check = False

        for i in range(len(course_list)):
            courseName1 = course_list[i].get_attribute('innerHTML').strip()
            course_sec1 = course_sec[i].get_attribute('innerHTML').strip()
            course_time1 = course_time[i].get_attribute('innerHTML').strip()
            faculty_initials1 = faculty_initials[i].get_attribute('innerHTML').strip()

            if courseName1 == courseName:
                check = True
                temporary.append([courseName1, course_sec1, course_time1, faculty_initials1])

            if check == True and courseName1 != courseName:
                break
        self.main_list.append(temporary)

    def get_info(self,args):

        threads = []
        for x in args:
            t = threading.Thread(target=self.thread, args=(x,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()



        data = []
        for i in self.main_list:
            for j in i:
                data.append(j)

        while len(data)!=0:
            routine = {
                'Saturday':
                    {
                        '08:00 AM-09:20 AM': [],
                        '09:30 AM-10:50 AM': [],
                        '11:00 AM-12:20 PM': [],
                        '12:30 PM-01:50 PM': [],
                        '02:00 PM-03:20 PM': [],
                        '03:30 PM-04:50 PM': [],
                        '05:00 PM-06:20 PM': [],
                    },
                'Sunday':
                    {
                        '08:00 AM-09:20 AM': [],
                        '09:30 AM-10:50 AM': [],
                        '11:00 AM-12:20 PM': [],
                        '12:30 PM-01:50 PM': [],
                        '02:00 PM-03:20 PM': [],
                        '03:30 PM-04:50 PM': [],
                        '05:00 PM-06:20 PM': [],
                    },
                'Monday':
                    {
                        '08:00 AM-09:20 AM': [],
                        '09:30 AM-10:50 AM': [],
                        '11:00 AM-12:20 PM': [],
                        '12:30 PM-01:50 PM': [],
                        '02:00 PM-03:20 PM': [],
                        '03:30 PM-04:50 PM': [],
                        '05:00 PM-06:20 PM': [],
                    },
                'Tuesday':
                    {
                        '08:00 AM-09:20 AM': [],
                        '09:30 AM-10:50 AM': [],
                        '11:00 AM-12:20 PM': [],
                        '12:30 PM-01:50 PM': [],
                        '02:00 PM-03:20 PM': [],
                        '03:30 PM-04:50 PM': [],
                        '05:00 PM-06:20 PM': [],
                    },
                'Wednesday':
                    {
                        '08:00 AM-09:20 AM': [],
                        '09:30 AM-10:50 AM': [],
                        '11:00 AM-12:20 PM': [],
                        '12:30 PM-01:50 PM': [],
                        '02:00 PM-03:20 PM': [],
                        '03:30 PM-04:50 PM': [],
                        '05:00 PM-06:20 PM': [],
                    },
                'Thursday':
                    {
                        '08:00 AM-09:20 AM': [],
                        '09:30 AM-10:50 AM': [],
                        '11:00 AM-12:20 PM': [],
                        '12:30 PM-01:50 PM': [],
                        '02:00 PM-03:20 PM': [],
                        '03:30 PM-04:50 PM': [],
                        '05:00 PM-06:20 PM': [],
                    }
            }

            deleted = []
            visited = []
            n = len(data)

            for i in range(len(data)):
                # print(data[i])
                if data[i][0] not in visited:

                    x = data[i][2]
                    deleted.append(data[i])
                    for k in range(0, len(x), 30):
                        dum = x[k] + x[k + 1]
                        dum1 = x[k + 3:k + 20]

                        if dum == 'Sa':
                            if len(routine['Saturday'][dum1]) == 0:
                                routine['Saturday'][dum1] = [data[i][0], data[i][1], data[i][3]]
                                visited.append(data[i][0])
                        elif dum == 'Su':

                            if len(routine['Sunday'][dum1]) == 0:
                                routine['Sunday'][dum1] = [data[i][0], data[i][1], data[i][3]]
                                visited.append(data[i][0])
                        elif dum == 'Mo':
                            if len(routine['Monday'][dum1]) == 0:
                                routine['Monday'][dum1] = [data[i][0], data[i][1], data[i][3]]
                                visited.append(data[i][0])
                        elif dum == 'Tu':
                            if len(routine['Tuesday'][dum1]) == 0:
                                routine['Tuesday'][dum1] = [data[i][0], data[i][1], data[i][3]]
                                visited.append(data[i][0])
                        elif dum == 'We':
                            if len(routine['Wednesday'][dum1]) == 0:
                                routine['Wednesday'][dum1] = [data[i][0], data[i][1], data[i][3]]
                                visited.append(data[i][0])
                        elif dum == 'Th':
                            if len(routine['Thursday'][dum1]) == 0:
                                routine['Thursday'][dum1] = [data[i][0], data[i][1], data[i][3]]
                                visited.append(data[i][0])

            # for key, value in routine.items():
            #     print(key)
            #     print(value)

            # print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(len(deleted)):
                data.remove(deleted[i])
            self.store.append(routine)

        return self.store
        # print(self.store)




