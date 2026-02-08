class Department:
    """
    Simple class to represent a hospital department.
    
    :name: department name
    :type name: str
    :department_id: unique id for department
    :type department_id: str
    :patients: dict of patients
    :type patients: dict
    :staff: dict of staff
    :type staff: dict
    """

    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id
        self.patients = {}
        self.staff = {}

    def add_patient(self, patient)->str:
        """
        add patient to department

        :patient: patient object
        :type patient: Patient
        :return: patient_id
        :rtype: str
        """
        self.patients[patient.patient_id] = patient
        print(f"Patient '{patient.name}' added to {self.name} department.")
        return patient.patient_id

    def remove_patient(self, patient_id):
        """
        remove patient if not under treatment

        :patient_id: id of patient
        :type patient_id: str
        
        :return: None
        :rtype: None
        """
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            if not patient.current_treatments:
                del self.patients[patient_id]
                print(f"Patient '{patient.name}' removed successfully.")
            else:
                print("Patient is under treatment, cannot remove.")
        else:
            print("Invalid patient ID.")