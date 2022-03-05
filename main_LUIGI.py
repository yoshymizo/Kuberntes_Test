# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import luigi
from flask import Flask

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



app = Flask(__name__)


class HelloWorldTask(luigi.Task):
    task_namespace = 'examples'
    def run(self):
        print("{task} says: Hello world!".format(task=self.__class__.__name__))
class task_2(luigi.Task):
    def requires(self):
        HelloWorldTask(self.param)
    def run(self):
        x =  3*3
    def output(self):
        return x

@app.route("/")
def hello():
    print(x +1)
    return "Hello from Python - working"


if __name__ == "__main__":
    luigi.run(['examples.HelloWorldTask', '--workers', '1', '--local-scheduler'])
    #luigi.run(['examples.HelloWorldTask'])
    #luigi.run()
    app.run(host='0.0.0.0')


#https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
