import numpy
from sklearn.decomposition import PCA
from sklearn.svm import SVC

print('Read training data...')
with open('train.csv', 'r') as reader:
    reader.readline()
    train_label = []
    train_data = []
    for line in reader.readlines():
        data = list(map(int, line.rstrip().split(',')))
        train_label.append(data[0])
        train_data.append(data[1:])
print('Loaded ' + str(len(train_label)))

print('Reduction...')
train_label = numpy.array(train_label)
train_data = numpy.array(train_data)
pca = PCA(n_components=64, whiten=True)
pca.fit(train_data)
train_data = pca.transform(train_data)

print('Train SVM...')
svc = SVC()
svc.fit(train_data, train_label)

print('Read testing data...')
with open('test.csv', 'r') as reader:
    reader.readline()
    test_data = []
    for line in reader.readlines():
        pixels = list(map(int, line.rstrip().split(',')))
        test_data.append(pixels)
print('Loaded ' + str(len(test_data)))

print('Predicting...')
test_data = numpy.array(test_data)
test_data = pca.transform(test_data)
predict = svc.predict(test_data)

print('Saving...')
with open('pca_svm.csv','w') as writer:
    writer.write('"ImageId","Label"\n')
    count = 0
    for p in predict:
        count += 1
        writer.write(str(count) + ',"' + str(p) + '"\n')
