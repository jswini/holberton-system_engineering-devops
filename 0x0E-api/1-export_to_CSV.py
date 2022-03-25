#!/usr/bin/python3
'''
This script will gather and process data from a REST API
 and process it for display
'''
import requests
import sys
import csv

if __name__ == "__main__":
    '''
    finds data from api
    formats data
    outputs data
    '''
    task_completed = []
    # task_completed_count = 0
    employee_id = int(sys.argv[1])
    employees = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id))
    employees_info = employees.json()['username']
    # (alt way for above)employees_info = employees.get('name')
    all_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(employee_id))
    task_list = all_tasks.json()

    for task in task_list:
        task_detail = []
        task_detail.append(employee_id)
        task_detail.append(employees_info)
        task_detail.append(task.get('completed'))
        task_detail.append(task.get('title'))
        task_completed.append(task_detail)

    with open('2.csv', 'w')as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(task_completed)
