import pandas


def task_1_1(data, out):
    m_count = data.Sex[data.Sex == 'male'].count()
    f_count = data.Sex[data.Sex == 'female'].count()
    out.write(str(m_count) + ' ' + str(f_count))

def task_1_2(data, out):
    survived = data.Survived[data.Survived].count() / float(data.Survived.count()) * 100
    out.write('%.2f' % survived)


def task_1_3(data, out):
    class_a = data.Cabin.dropna().count() / float(data.Survived.count())
    out.write('%.2f' % class_a)

def task_1_4(data, out):
    out.write('%.2f' % data.Age.mean())
    out.write(' ')
    out.write('%.2f' % data.Age.median())

def task_1_5(data, out):
    corr = data.corr()['SibSp']['Parch']
    out.write('%.2f' % corr)

def main():
    data = pandas.read_csv('titanic.csv', index_col = 'PassengerId')
    for i in range(1, 6):
        name = 'task_1_' + str(i)
        out = open(name + '.out', 'w')
        method = globals().get(name)
        method(data, out)
        out.close()

if __name__ == '__main__':
    main()
