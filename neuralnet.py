from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

dataset = loadtxt('voice_dataset.csv', delimiter=',')
x = dataset[:, 0:20]
y = dataset[:, 20]

model = Sequential()
model.add(Dense(12, input_dim=20, activation='hard_sigmoid'))
model.add(Dense(9, activation='hard_sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=20, batch_size=10)

_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy * 100))

predictions = (model.predict(x) > 0.5).astype(int)

for i in range(5):
    print('%s => %d (expected %d)' % (x[i].tolist(), predictions[i], y[i]))
    print('%s => %d (expected %d)' % (x[2000 + i].tolist(), predictions[2000 + i], y[2000 + i]))
