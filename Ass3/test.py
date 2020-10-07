from student_heart import calibrate
from assignment_3_heart import assignment_3_heart
import time


for a in range(5):
    print("-------------------------------------------------------------------------------------------------", a)
    for i in range(50, 155, 5):
        print(i)
        run = assignment_3_heart(str(1.9), str(66.6), str(i))
        run.run()
        time.sleep(1)