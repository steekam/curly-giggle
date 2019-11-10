import numpy as np
import pandas as pd
import math


class ANN:

    def __init__(self):
        self.learning_rate: float = 0.5
        # Initial weights based on postion 0 => outer[[1j,2j,3j],[1i,2i,3i]], 1 => hidden[jk,ik]
        self.weights = [
            np.array([[0.2, 0.3, 0.2], [0.1, 0.1, 0.1]]), np.array([[0.5, 0.1]])]

        self.dataset = []

    def bind_values(self):
        max_value = max(self.dataset)
        min_value = min(self.dataset)
        self.dataset = list(
            map(lambda value: (value-min_value)/(max_value-min_value), self.dataset))

    def generate_vectors(self):
        input_vectors = []
        target_outputs = []

        current_start = 0

        while(current_start < len(self.dataset) - 3):
            local_index = current_start
            input_vectors.append(np.array([[self.dataset[local_index]], [
                                 self.dataset[local_index+1]], [self.dataset[local_index+2]]]))
            target_outputs.append(self.dataset[local_index+3])
            current_start += 1

        return input_vectors, target_outputs

    def sigmoid(self, value):
        return 1/(1+np.exp(-value))

    def sigmoid_fderivative(self, value):
        return value*(1-value)

    def forward_feed(self, current_inputs):
        layer_outputs = []
        layer_inputs = current_inputs  # init layer inputs
        for layer_weights in self.weights:
            layer_output = self.sigmoid(layer_weights.dot(layer_inputs))
            layer_outputs.append(layer_output)
            layer_inputs = layer_output
        return layer_outputs

    def compute_error(self, layer_outputs, target_output: float):
        error_list = []
        final_output = layer_outputs[-1][0][0]
        output_error = (target_output - final_output) * \
            self.sigmoid_fderivative(final_output)
        # print("Output error: ",output_error)
        # Error in hidden layer
        for inner_output, inner_weights in zip(layer_outputs[:-1], self.weights[1:]):
            # print("Inner output: \n{}\n Inner weights: \n{}\n".format(inner_output, inner_weights))
            output_fderivative = np.vectorize(
                self.sigmoid_fderivative)(inner_output)
            node_error = output_error * \
                np.multiply(output_fderivative, inner_weights.reshape(2, 1))
            error_list.append(node_error)
        # Add output error
        error_list.append(np.array([[output_error]]))
        return error_list

    def update_weights(self, error_list, layer_outputs):
        new_weights = []
        for errors, outputs, weights in reversed(list(zip(error_list, layer_outputs, self.weights))):
            # print("Error: ",errors)
            # print("Output: ",outputs)
            # print("Weights: ",weights)
            deltas = self.learning_rate*errors*outputs
            # print("deltas:",deltas)
            # weights_index = self.weights.index(weights)
            # self.weights[weights_index] = np.transpose(np.transpose(weights) - np.transpose(deltas))
            new_weights.append(np.transpose(
                np.transpose(weights) - np.transpose(deltas)))
        self.weights = list(reversed(new_weights))

    def back_propagation(self, input_vectors, target_outputs):
        # forward feed
        for current_inputs, current_target_output in zip(input_vectors, target_outputs):
            layer_outputs = self.forward_feed(current_inputs)
            # Error calculation
            error_list = self.compute_error(layer_outputs, current_target_output)
            # Update weights
            self.update_weights(error_list, layer_outputs)

    def print_layer_weights(self):
        for count, layer_weights in enumerate(self.weights):
            print("Layer {} weights:\n {}".format(count+1, layer_weights))

    def run(self):
        # bind values btn 0 and 1
        self.bind_values()
        # Generate input vectors and output target scalar
        input_vectors, target_outputs = self.generate_vectors()
        # Run back propagation
        self.back_propagation(input_vectors, target_outputs)
        # Print updated weights
        self.print_layer_weights()


if __name__ == "__main__":
    ann = ANN()
    # Traffic waiting times in minutes
    ann.dataset = [30, 40, 50, 20, 15, 60, 70, 50, 40]
    ann.run()
