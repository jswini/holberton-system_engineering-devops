#!/usr/bin/python3
'''
This script will gather and process data from a REST API
 and process it for display
'''
import requests
import sys

if __name__ == "__main__":
    '''
    finds data from api
    formats data
    outputs data
    '''
    task_completed = []
    task_completed_count = 0
    employee_id = int(sys.argv[1])
    employees = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id))
    employees_info = employees.json()['name']
    # (alt way for above)employees_info = employees.get('name')
    all_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(employee_id))
    task_list = all_tasks.json()

    task_count = len(task_list)
    for task in task_list:
        if task.get('completed') is True:
            task_completed.append(task.get('title'))
        task_completed_count = len(task_completed)
    print('Employee {} is done with tasks({}/{}):'
          .format(employees_info, task_completed_count, task_count))
    for item in task_completed:
        print('\t {}'.format(item))
