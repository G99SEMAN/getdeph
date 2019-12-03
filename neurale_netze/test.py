import tensorflow as tf #Hier importieren wir die Library Tensorflow, welche für neuronale Netze der perfekte Einstieg ist. Eine Library ist ein vorgeschriebenes Programm. Es macht uns die Arbeit deutlich leichter
from tensorflow import keras #hier importieren wir dann noch einen speziellen Teil aus Tensorflow. Keras. Hierzu später mehr.

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])]) #hier definieren wir unser neuroanles Netz, wobei wir mit Dense unser Neuron erstellen. In diesem Beispiel nur eins, wir werden aber später sehen, dass man in der Regel mit deutlich mehr Neuronen arbeitet. Unser Neuron befindet sich in einem Layer, davon hat man später auch mehrere. Man kann sich dies wie Ebenen in einem Sieb vorstellen.

model.compile(optimizer='sgd', loss='mean_squared_error') #hier kompilieren wir unser neuronales Netz, wobei der loss misst, wie groß der Fehler ist und dies dann mit optimizer optimiert wird


xs=[1, 2, 3] #Zahlenreihe 1
ys=[2, 4, 6] #Zahlenreihe 2

model.fit(xs, ys, epochs=1000) #unser kompiliertes Modell fitten wir hier mit unseren zwei Zahlenreihen. epochs=1000 heißt, dass das Programm 1000 Durchläufer macht, um zu trainieren. Probiert gerne mal mit der Anzahl rum. Je weniger Durchläufe, desto schlechter ist die Schätzung. Gleichzeitig seht ihr, dass die Änderung im Loss immer weniger wird, je mehr Durchläufe es sind (es ist also irgendwann kaum noch eine Verbesserung sichtbar)

print(model.predict([7])) #hier lassen wir unser neuronales Netz schätzen, was für die zweiten Zahl rauskommt, wenn die erste Zahl gleich 10 ist. Der Befehlt print sorgt hier einfach dafür, dass der Wert für uns ausgegeben wird.
