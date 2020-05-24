import numpy as np

np.random.seed(1)
np.set_printoptions(precision=6, suppress=True)

trainInput = np.array([[0, 0, 1],
                       [1, 1, 1],
                       [1, 0, 1],
                       [0, 1, 1]])

trainOutput = np.array([[0, 1, 1, 0]]).T


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoidDerivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def relu(x):
    return x * (x > 0)


def reluDerivative(x):
    return 1. * (x > 0)


def neuralNetwork(hidFunc, hidDerFunc, outFunc, outDerFunc):
    predictedOutput = 0
    synapticWeightsHidden = 2 * np.random.rand(len(trainInput[0]), 4) - 1
    synapticWeightsOutput = 2 * np.random.rand(4, 1) - 1
    print("\n\nTesting for attributes: [{}] used as hidden function, "
          "[{}] used as derivative for hidden function, [{}] used as out function, "
          "[{}] used as  derivative for out function\n".format(hidFunc, hidDerFunc, outFunc, outDerFunc))
    for i in range(2000):
        # Feedforward
        hiddenLayerWeights = np.dot(trainInput, synapticWeightsHidden)
        predictedHiddenOutput = sigmoid(hiddenLayerWeights) if hidFunc is "sigmoid" else relu(hiddenLayerWeights)

        outputLayerWeights = np.dot(predictedHiddenOutput, synapticWeightsOutput)
        predictedOutput = sigmoid(outputLayerWeights) if outFunc is "sigmoid" else relu(outputLayerWeights)

        # Back propagation of hidden-output layer
        errorOutput = predictedOutput - trainOutput
        derivativeHidden = reluDerivative(outputLayerWeights) if hidDerFunc is "derivative Relu" else sigmoidDerivative(outputLayerWeights)
        pho = predictedHiddenOutput
        adjustmentHidden = np.dot(pho.T, errorOutput * derivativeHidden)
        # Back propagation of input-hidden layer
        inputLayerOut = trainInput
        erdh = errorOutput * derivativeHidden
        swo = synapticWeightsOutput
        hiddenLayerError = np.dot(erdh, swo.T)
        derivativeOutput = reluDerivative(hiddenLayerWeights) if outDerFunc is "derivative Relu" else sigmoidDerivative(hiddenLayerWeights)
        adjustmentOutput = np.dot(inputLayerOut.T, derivativeOutput * hiddenLayerError)

        synapticWeightsOutput -= adjustmentHidden
        synapticWeightsHidden -= adjustmentOutput

    print("Hidden weights\n", synapticWeightsHidden)
    print("Output weights\n", synapticWeightsOutput)
    print("Predicted output\n", predictedOutput)

    newInput = np.array([1, 1, 0]), np.array([0, 1, 1])
    for newInput in newInput:
        hidLayer = sigmoid(np.dot(newInput, synapticWeightsHidden))
        output = sigmoid(np.dot(hidLayer, synapticWeightsOutput))
        print("New situation {}, with same weights: ".format(newInput), output)


neuralNetwork("relu", "derivative Relu", "relu", "derivative Relu")
neuralNetwork("relu", "derivative Relu", "sigmoid", "derivative Sigmoid")
neuralNetwork("sigmoid", "derivative Sigmoid", "relu", "derivative Relu")
neuralNetwork("sigmoid", "derivative Relu", "sigmoid", "derivative Relu")
neuralNetwork("relu", "derivative Sigmoid", "relu", "derivative Sigmoid")
neuralNetwork("sigmoid", "derivative Sigmoid", "sigmoid", "derivative Sigmoid")

