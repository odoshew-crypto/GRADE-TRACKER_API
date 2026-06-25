from sqlalchemy.orm import Session
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate): # defines a function called create_student that takes in a database session and a StudentCreate schema object as parameters. The function is used to create a new student in the database.
    db_student = models.Student(**student.model_dump()) # creates a new instance of the Student model using the data from the StudentCreate schema object. The data is passed as keyword arguments to the Student model's constructor.
    db.add(db_student) # adds the new student to the database session.
    db.commit() # commits the changes to the database, saving the new student.
    db.refresh(db_student) # refreshes the instance of the student in the database session, ensuring that it has the latest data from the database.
    return db_student # returns the newly created student object.

# Read operation
def get_student(db: Session, student_id: int): # defines a function called get_student that takes in a database session and a student ID as parameters. The function is used to retrieve a student from the database based on their ID.
    return db.query(models.Student).filter(models.Student.id == student_id).first() # queries the database for a student with the specified ID and returns the first result. If no student is found, it returns None.

# Read all operation
def get_students(db: Session): # defines a function called get_students that takes in a database session as a parameter. The function is used to retrieve all students from the database.
    return db.query(models.Student).all() # queries the database for all students and returns a list of student objects.

# Update operation
def update_student(db: Session, student_id: int, data: schemas.StudentUpdate): # defines a function called update_student that takes in a database session, a student ID, and a StudentUpdate schema object as parameters. The function is used to update an existing student in the database based on their ID.
    student = db.query(models.Student).filter(models.Student.id == student_id).first() # queries the database for a student with the specified ID and retrieves the first result. If no student is found, it returns None.
    if not student: # checks if a student was found in the database.
        return None # if no student was found, it returns None.
    update=data.model_dump(exclude_unset=True) # creates a dictionary of the data to be updated, excluding any fields that were not set in the StudentUpdate schema object.
    for field, value in update.items(): # iterates over the fields and values in the update dictionary.
        setattr(student, field, value) # sets the attribute of the student object to the new value for each field in the update dictionary.
    db.commit() # commits the changes to the database, saving the updated student.
    db.refresh(student) # refreshes the instance of the student in the database session, ensuring that it has the latest data from the database.
    return student # returns the updated student object.

# Delete operation
def delete_student(db: Session, student_id: int): # defines a function called delete_student that takes in a database session and a student ID as parameters. The function is used to delete an existing student from the database based on their ID.
    student = db.query(models.Student).filter(models.Student.id == student_id).first() # queries the database for a student with the specified ID and retrieves the first result. If no student is found, it returns None.
    if not student: # checks if a student was found in the database.
        return None # if no student was found, it returns None.
    db.delete(student) # deletes the student object from the database session.
    db.commit() # commits the changes to the database, saving the deletion of the student.
    return student # returns the deleted student object.