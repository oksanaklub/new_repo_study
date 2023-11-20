class Worker:

    def __init__(self, name, job_title, employee_id,):
        self.name = name
        self.job_title = job_title
        self.employee_id = employee_id

    def get_worker_info(self):
        info = f"Worker Name: {self.name}\n"
        info += f"Job Title: {self.job_title}\n"
        info += f"Employee ID: {self.employee_id}\n"
        return info
