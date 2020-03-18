class classroom:
    def __init__(self,name):
        self.name = name
        self.interest = []
        self.designation = ""
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.mentor = ""
    
    def addStack(self, _interest):
        self.interest.append(_interest)
        
    def setMentorOrLearner(self, _designation):
        if(_designation.lower()=='mentor' or _designation.lower()=='learner'):
            self.designation = _designation
            if(_designation.lower()=='mentor'):
                mentorsList.append(self)
        else:    
            print("Designation unacceptable. Please enter either learner or mentor , ", self.name, "!")
            return
        
        
    
    def setAvailableTime(self, _days, _hours, _minutes):
        if(self.designation.lower()!='mentor'):
            print("Sorry ,", self.name, "! Only mentors can set their time!")
            return
        
        self.days = _days
        self.hours = _hours
        self.minutes = _minutes
    
    def getMentor(self, _interest, _days, _hours, _minutes):
        if(self.designation.lower()=='mentor'):
            print(self.name, " is already a mentor!")
            return
        
        flag = 0
        
        for mentor in mentorsList:
            if(all(interest in mentor.interest for interest in self.interest) and _days<=mentor.days):
                if(_hours<=mentor.hours):
                    if(_minutes<=mentor.minutes):
                        self.mentor = mentor.name
                        print(self.name, ", you have found your mentor!", self.mentor, "is your mentor!")
                        flag = 1
                        return
                    
        if(flag==0):
            print("Sorry ,", self.name, "! We could not find a suitable mentor!")

mentorsList = []

l1 = classroom("Tom")
l2 = classroom("Susan")
l3 = classroom("Evolet")
m1 = classroom("Harry")
m2 = classroom("John")
m3 = classroom("Elizabeth")

l1.addStack('python')
l1.addStack('c')
l2.addStack('c')
l3.addStack('java')
l3.addStack('clojure')
m1.addStack('java')
m2.addStack('python')
m2.addStack('c')
m2.addStack('c++')
m3.addStack('java')
m3.addStack('clojure')

l1.setMentorOrLearner('learner')
l2.setMentorOrLearner('learner')
l3.setMentorOrLearner('learner')
m1.setMentorOrLearner('mentor')
m2.setMentorOrLearner('mentor')
m3.setMentorOrLearner('mentor')

l1.setAvailableTime(2,5,30)
m1.setAvailableTime(2,6,30)
m2.setAvailableTime(1,10,45)
m3.setAvailableTime(1,8,15)

l1.getMentor('python',1,10,15)
l3.getMentor('java',3,10,45)




  






















