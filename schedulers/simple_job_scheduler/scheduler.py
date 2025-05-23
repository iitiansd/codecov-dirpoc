# schedulers/simple_job_scheduler/scheduler.py
import datetime
import time

class Job:
    def __init__(self, job_id: str, scheduled_time: datetime.datetime, task: str):
        self.job_id = job_id
        self.scheduled_time = scheduled_time
        self.task = task
        self.executed = False

    def execute(self):
        """Simulates executing the job."""
        print(f"Executing job {self.job_id}: {self.task} at {datetime.datetime.now()}")
        self.executed = True

class SimpleScheduler:
    def __init__(self):
        self.jobs: list[Job] = []

    def add_job(self, job: Job):
        """Adds a job to the scheduler."""
        self.jobs.append(job)
        print(f"Job {job.job_id} added, scheduled for {job.scheduled_time}")

    def run_pending_jobs(self):
        """Runs jobs whose scheduled time has passed."""
        now = datetime.datetime.now()
        for job in self.jobs:
            if not job.executed and job.scheduled_time <= now:
                job.execute()

# Example usage
if __name__ == "__main__":
    scheduler = SimpleScheduler()

    # Schedule a job for 5 seconds from now
    job1_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
    job1 = Job("job_001", job1_time, "Send daily report")
    scheduler.add_job(job1)

    # Schedule a job for 2 seconds from now
    job2_time = datetime.datetime.now() + datetime.timedelta(seconds=2)
    job2 = Job("job_002", job2_time, "Clean up temporary files")
    scheduler.add_job(job2)

    print("Scheduler running...")
    # Simulate time passing to allow jobs to execute
    for _ in range(7):
        scheduler.run_pending_jobs()
        time.sleep(1) # Wait for 1 second
    
    print("Scheduler finished checking for jobs.")