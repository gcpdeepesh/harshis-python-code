import random
teachers = ["Neha ma'am","Preeti ma'am","Vatsala ma'am","Yogita ma'am","Sonal ma'am","Geetanjali ma'am","Harmeet ma'am","Priyanka ma'am","Karuna ma'am","Seema ma'am","Charu ma'am","Ranjna ma'am","Kalika ma'am","Sangeeta ma'am","Namrata ma'am","Preeti Raj ma'am"]
subjects = ["English","G.K","Maths","Hindi","E.V.S","Sanskrit","Social Studies","Social Science","Science","History","Psychology","Chemistry","Physics","Civics","Geography","Economy"]
for x in range(16):
    teacher = teachers[x]
    subjectrandom = random.choice(subjects)
    subjects.remove(subjectrandom)
    print(teacher, "is teaching" , subjectrandom)



