Data structure: dict 
{student_name: [list of "P"/"A" for each class held]}. 
""" 
 
attendance = {} 
 
 
def add_student(name):     if name in attendance: 
        return "Student already 
exists."     attendance[name] = []     return "Student added." 
 
 
def mark(name, status): 
    """Add one day's attendance. 
status: P (present) or A (absent)."""     status = status.upper()     if name not in attendance:         return "Student not found."     if status not in ("P", "A"): 
        return "Status must be P or A." attendance[name].append(status)     return "Attendance recorded." 
 
 
def update(name, day, status): 
    """Correct an existing record. day is 1-based."""     status = status.upper()     if name not in attendance:         return "Student not found."     if status not in ("P", "A"):         return "Status must be P or A." 
    if not 1 <= day <= len(attendance[name]):         return "Invalid day number." 
    attendance[name][day - 1] = status     return "Attendance updated." 
 
 
def percentage(name):     records = attendance[name]     if not records:         return 0.0 
    return records.count("P") / len(records) * 100 
 
 
def below_threshold(threshold=75): 
    return [(n, percentage(n)) for n in attendance if percentage(n) < threshold] 
 
 
def display():     if not attendance:         print("No students.")         return 
    
print(f"{'Student':<12}{'Records':<2 5}{'Present':<9}{'Total':<7}{'%'}")     print("-" * 60)     for n, rec in attendance.items(): 
        print(f"{n:<12}{' 
'.join(rec):<25}{rec.count('P'):<9}{le n(rec):<7}{percentage(n):.1f}") 
 
 
def run_tests():     attendance.clear()     # Scenario 1: normal data 
    add_student("Asha"); add_student("Ravi"); add_student("Meena") 
    for s in "PPPP": mark("Asha", s)           
# 100% 
    for s in "PAPA": mark("Ravi", s)           
# 50% 
    for s in "PPPA": mark("Meena", s)          # 75% 
    assert percentage("Asha") == 100 and percentage("Ravi") == 50     assert percentage("Meena") == 75 
    # Scenario 2: threshold (75 is NOT below 75) 
    assert [n for n, _ in below_threshold(75)] == ["Ravi"] 
    assert sorted(n for n, _ in below_threshold(80)) == 
["Meena", "Ravi"] 
    # Scenario 3: update changes percentage 
    update("Ravi", 2, "P"); update("Ravi", 4, "P")     assert percentage("Ravi") == 100 
    # Scenario 4: invalid inputs and edge cases 
    assert add_student("Asha") == "Student already exists." 
    assert mark("Ghost", "P") == "Student not found." 
    assert mark("Asha", "X") == "Status must be P or A." 
    assert update("Asha", 9, "A") == "Invalid day number."     add_student("New") 
    assert percentage("New") == 0.0            # no classes held yet, no crash 
    print("All attendance tests passed.\n") 
 
 
def menu():     while True: 
        print("\n1.Add student 2.Mark attendance 3.Update record " 
              "4.Display 5.Below threshold 6.Exit")         ch = input("Choice: ").strip()         if ch == "1": 
            
print(add_student(input("Name: 
")))         elif ch == "2": 
            print(mark(input("Name: "), input("Status (P/A): ")))         elif ch == "3": 
            print(update(input("Name: "), int(input("Day no.: ")), input("New status (P/A): "))) 
        elif ch == "4":             display()         elif ch == "5": 
            t = float(input("Threshold %: 
"))             low = below_threshold(t)             for n, p in low: 
                print(f"{n}: {p:.1f}% 
(shortage)") 
            if not low: 
                print("Everyone meets the threshold.") 
        elif ch == "6": 
            break         else: 
            print("Invalid choice.") 
 
 
if __name__ == "__main__": 
    run_tests()     menu() 
