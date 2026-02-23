import random

def generate_sample_data():
    first_names = ["Jordan", "Taylor", "Casey", "Morgan", "Alex", "Jamie", "Riley"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
    majors = ["Computer Science", "Nursing", "Business Admin", "Criminal Justice", "Biology"]

    with open("sql_queries/seed_sample_data.sql", "w") as f:
        f.write("-- Generic Seed Data for Sample College ERP\n")
        f.write("INSERT INTO SC_ERP.STUDENTS (id, first_name, last_name, major, enroll_date) VALUES\n")
        
        for i in range(1001, 1050): # Generating 50 sample students
            fn = random.choice(first_names)
            ln = random.choice(last_names)
            mj = random.choice(majors)
            comma = "," if i < 1049 else ";"
            f.write(f"({i}, '{fn}', '{ln}', '{mj}', '2025-01-15'){comma}\n")
            
    print("Success: Generated 50 rows of generic student data in sql_queries/seed_sample_data.sql")

if __name__ == "__main__":
    generate_sample_data()