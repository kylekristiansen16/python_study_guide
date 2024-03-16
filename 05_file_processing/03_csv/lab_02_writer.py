
""" 
improving the student's skills in reading and writing CSV files;
using the writer function or the DictWriter class.

Have you ever prepared a report? Your task will be to prepare a report summarizing the results 
of exams in maths, physics and biology. The report should include the name of the exam, the number 
of candidates, the number of passed exams, the number of failed exams, and the best and the worst scores.
All the data necessary to create the report is in the exam_results.csv file.

Note that one candidate may have several results for the same exam. The number of candidates should express 
the number of unique people in each exam identified by Candidate ID. The final report should look like this:

Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score
Maths,8,4,6,90,33
Physics,3,0,3,66,50
Biology,5,2,3,88,23
"""

import csv

class ExamResult():
    def __init__(self, exam_name, candidate_id, score, grade):
        self.exam_name = exam_name
        self.candidate_id = candidate_id
        self.score = int(score)
        self.grade = grade
        
class Exam():
    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.candidates = []
        self.num_passed = 0
        self.num_failed = 0
        self.best_score = 0
        self.worst_score = 100
    
    def add_exam_result(self, exam_result):
        self.candidates.append(exam_result.candidate_id)
        if exam_result.grade == 'Pass':
            self.num_passed += 1
        else:
            self.num_failed += 1
        
        if exam_result.score > self.best_score:
            self.best_score = exam_result.score
        
        if exam_result.score < self.worst_score:
            self.worst_score = exam_result.score
            
    def get_number_of_candidates(self):
        return len(set(self.candidates))
    
class Report():
    def __init__(self):
        self.exams = {}
    
    def parse_exam_results_csv(self, file_name):
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Exam Name'] not in self.exams:
                    self.add_exam(ExamResult(row['Exam Name'], row['Candidate ID'], row['Score'], row['Grade']))
                else:
                    self.exams[row['Exam Name']].add_exam_result(ExamResult(row['Exam Name'], row['Candidate ID'], row['Score'], row['Grade']))
    
    def add_exam(self, exam_result):
        self.exams[exam_result.exam_name] = Exam(exam_result.exam_name)
        self.exams[exam_result.exam_name].add_exam_result(exam_result)
    
    def print_report(self):
        print('Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score')
        for exam in self.exams.values():
            print(f'{exam.exam_name},{exam.get_number_of_candidates()},{exam.num_passed},{exam.num_failed},{exam.best_score},{exam.worst_score}')
    
    def write_report_csv(self, file_name=None):
        if file_name is None:
            file_name = 'exam_report.csv'
            
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 'Number of Failed Exams', 'Best Score', 'Worst Score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for exam in self.exams.values():
                writer.writerow({
                    'Exam Name': exam.exam_name, 
                    'Number of Candidates': exam.get_number_of_candidates(), 
                    'Number of Passed Exams': exam.num_passed, 
                    'Number of Failed Exams': exam.num_failed, 
                    'Best Score': exam.best_score, 
                    'Worst Score': exam.worst_score
                    })
                
report = Report()
report.parse_exam_results_csv('/Users/kylekristiansen/cherreco/python/05_file_processing/03_csv/exam_results.csv')
report.print_report()
report.write_report_csv('/Users/kylekristiansen/cherreco/python/05_file_processing/03_csv/exam_report.csv')