import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
np.set_printoptions(precision=6, suppress=True)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoidDerivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def relu(x):
    return x * (x > 0)


def reluDerivative(x):
    return 1. * (x > 0)


def neuralNetwork(trainInput, trainOutput, hidFunc, hidDerFunc, outFunc, outDerFunc, testInput):
    print(trainInput, trainOutput)
    predictedOutput = 0
    synapticWeightsHidden = 2 * np.random.rand(trainInput.shape[1], trainInput.shape[0]) - 1
    synapticWeightsOutput = 2 * np.random.rand(trainOutput.shape[0], trainOutput.shape[1]) - 1
    print("\n\nThe train input is\n", trainInput)
    print("Testing for attributes: [{}] used as hidden function, "
          "[{}] used as derivative for hidden function, [{}] used as out function, "
          "[{}] used as  derivative for out function\n".format(hidFunc, hidDerFunc, outFunc, outDerFunc))

    for i in range(2000):
        # Feedforward
        hiddenLayerWeights = np.dot(trainInput, synapticWeightsHidden)
        predictedHiddenOutput = hidFunc(hiddenLayerWeights)

        outputLayerWeights = np.dot(predictedHiddenOutput, synapticWeightsOutput)
        predictedOutput = outFunc(outputLayerWeights)

        # Back propagation of hidden-output layer
        errorOutput = predictedOutput - trainOutput
        derivativeHidden = hidDerFunc(outputLayerWeights)
        pho = predictedHiddenOutput
        adjustmentHidden = np.dot(pho.T, errorOutput * derivativeHidden)

        # Back propagation of input-hidden layer
        inputLayerOut = trainInput
        erdh = errorOutput * derivativeHidden
        swo = synapticWeightsOutput
        hiddenLayerError = np.dot(erdh, swo.T)
        derivativeOutput = outDerFunc(hiddenLayerWeights)
        adjustmentOutput = np.dot(inputLayerOut.T, derivativeOutput * hiddenLayerError)

        synapticWeightsOutput -= adjustmentHidden
        synapticWeightsHidden -= adjustmentOutput

    print("Hidden weights\n", synapticWeightsHidden)
    print("Output weights\n", synapticWeightsOutput)
    print("Predicted output\n", predictedOutput)

    # Test
    hidLayer = sigmoid(np.dot(testInput, synapticWeightsHidden))
    testOutput = sigmoid(np.dot(hidLayer, synapticWeightsOutput))
    print("New situation {}, with same weights: ".format(testInput), testOutput)
    return predictedOutput, testOutput


def parabola():
    x = np.linspace(-50, 50, 26)
    y = x ** 2
    trainInp = np.reshape(x, (len(x), 1))
    trainOut = np.reshape(y, (len(y), 1))
    testX = np.linspace(-50, 50, 101)
    testInp = np.reshape(testX, (len(testX), 1))
    fig, axs = plt.subplots(3)
    axs[0].set_title("Original")
    axs[0].scatter(x, y)
    axs[1].set_title("Aproximated for original input")
    predictedOut, testOut = neuralNetwork(trainInp, trainOut, sigmoid, sigmoidDerivative, relu, reluDerivative, testInp)
    axs[1].scatter(trainInp, predictedOut)
    axs[2].set_title("Aproximated for testing input")
    axs[2].scatter(testInp, testOut)
    plt.show()


def sin():
    x = np.linspace(0, 2, 21)
    y = np.sin(x * (3 * np.pi / 2))
    trainInp = np.reshape(x, (len(x), 1))
    trainOut = np.reshape(y, (len(y), 1))
    testX = np.linspace(0, 2, 161)
    testInp = np.reshape(testX, (len(testX), 1))
    fig, axs = plt.subplots(3)
    axs[0].set_title("Original")
    axs[0].scatter(x, y)
    axs[1].set_title("Aproximated for original input")
    predictedOut, testOut = neuralNetwork(trainInp, trainOut, sigmoid, sigmoidDerivative, relu, reluDerivative, testInp)
    axs[1].scatter(trainInp, predictedOut)
    axs[2].set_title("Aproximated for testing input")
    axs[2].scatter(testInp, testOut)
    plt.show()


parabola()
sin()
