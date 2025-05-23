# schedulers/simple_job_scheduler/tests/test_scheduler.py
import unittest
import datetime
from unittest.mock import patch
from schedulers.simple_job_scheduler.scheduler import Job, SimpleScheduler

class TestScheduler(unittest.TestCase):
    def test_job_execution(self):
        # Schedule a job for the past to ensure it's runnable immediately
        past_time = datetime.datetime.now() - datetime.timedelta(minutes=1)
        job = Job("test_job_1", past_time, "Perform test task")
        
        with patch('builtins.print') as mock_print:
            job.execute()
            self.assertTrue(job.executed)
            mock_print.assert_called_once() # Asserts print was called exactly once
            self.assertIn("Executing job test_job_1", mock_print.call_args[0][0]) # Use call_args for single call

    def test_add_job(self):
        scheduler = SimpleScheduler()
        current_time = datetime.datetime.now()
        job = Job("test_job_2", current_time, "Another task")
        
        with patch('builtins.print') as mock_print: # Patch print before add_job
            scheduler.add_job(job)
            self.assertIn(job, scheduler.jobs)
            self.assertEqual(len(scheduler.jobs), 1)
            mock_print.assert_called_once()
            self.assertIn(f"Job {job.job_id} added", mock_print.call_args[0][0])


    def test_run_pending_jobs(self):
        scheduler = SimpleScheduler()
        
        # Move the patch block to cover all print calls you want to assert on
        with patch('builtins.print') as mock_print: 
            # Job in the past
            past_time = datetime.datetime.now() - datetime.timedelta(seconds=5)
            job_past = Job("job_past", past_time, "Execute immediately")
            scheduler.add_job(job_past) # This print will now be captured by mock_print (call_args_list[0])

            # Job in the future
            future_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
            job_future = Job("job_future", future_time, "Execute later")
            scheduler.add_job(job_future) # This print will now be captured by mock_print (call_args_list[1])

            scheduler.run_pending_jobs() # This will trigger job_past.execute() (call_args_list[2])
            
            # Only job_past should have been executed
            self.assertTrue(job_past.executed)
            self.assertFalse(job_future.executed)
            
            # Check the total number of print calls
            # 2 calls from add_job, 1 call from job_past.execute()
            self.assertEqual(mock_print.call_count, 3) 

            # Check print calls for job_past execution (now at index 2)
            self.assertIn("Executing job job_past", mock_print.call_args_list[2][0][0])