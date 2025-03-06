import click
import os
import json

TODO_FILE = 'todo.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE,'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE,'w') as file:
        json.dump( tasks, file, indent=4 ) 


@click.group()
def cli():
    '''Simple Todo List Manager'''
    pass

@click.command()
@click.argument('task')
def add(task):
    '''Add a new task ro the list'''
    tasks = load_tasks()
    tasks.append({'task':task, 'done':False})
    save_tasks(tasks)
    click.echo(f'Task added successfully: {task}!')

cli.add_command(add)

if __name__ == '__main__':
    cli()
    