from flask import Flask , request , render_template
import os

app=Flask(__name__,template_folder='templates')


@app.route('/file1')
def hello_world():

    return 'sample test'

@app.route('/')
def path():
    # f = open("guru99.txt", "w+")

    filename = request.args.get('filename')
    linenumber = request.args.get('linenumber')

    try :
        int(linenumber)
    except ValueError as verr:
        return render_template('/error.html', name=linenumber)

    if filename == None :
        print('No file Name Given : Reading Default file file1')
        filecontent = open('file1.txt', 'r').read()
        print(filecontent)
        return filecontent


    if filename == "file1" :
        print('Reading the file1')
        filecontent = open('file1.txt', 'r').readlines()

        a = []
        for line in filecontent:
                a.append("{}".format( line.strip()))
        print(linenumber)

        if linenumber == None or linenumber == '':
            return render_template('/projects.html', name=a[0:100])

        return render_template('/projects.html', name=a[0:int(linenumber)])

    if filename == "file2" :
        print('Reading the file2')

        a = []
        with open('file2.txt', 'rb') as f:
            contents = f.readlines()
            print(contents)

        for content in contents:
            content.decode('utf-8', 'ignore')
            a.append(content.decode('utf-8', 'ignore'))

        if linenumber == None or linenumber == '':
            return render_template('/projects.html', context=a[0:100])
        return render_template('/projects.html' ,context = a[0:int(linenumber)])

    if filename == "file3":
        print('Reading the file3')
        filecontent = open('file3.txt', 'r').readlines()

        a = []
        for line in filecontent:
            a.append("{}".format(line.strip()))

        if linenumber == None or linenumber == '':
            return render_template('/projects.html', name=a[0:100])

        return render_template('/projects.html', name=a[0:int(linenumber)])

    if filename == "file4":
        print('Reading the file4')
        a = []
        with open('file4.txt', 'rb') as f:
            contents = f.readlines()
            print(contents)

        for content in contents:
            content.decode('utf-16', 'ignore')
            a.append(content.decode('utf-16', 'ignore'))

        if linenumber == None or linenumber == '':
            return render_template('/projects.html', context=a[0:100])

        return render_template('/projects.html', context=a[0:int(linenumber)])


if __name__ == '__main__':
    app.run()
