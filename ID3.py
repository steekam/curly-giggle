import math
import pandas as pd
import networkx as nx

# ID3 Algorithm implementation


class ID3:

    def __init__(self, data, target):
        self.data = data
        self.target_attribute = target

    def entropy(self, probabilities):
        return sum(map(lambda prob: -1*(prob*math.log2(prob)), probabilities))

    def info_gain(self, target_entropy, attribute_entropy):
        return target_entropy - attribute_entropy

    def probabilities(self, attribute, chain = []):
        attribute_class_count = list(zip(self.data[attribute].unique(),self.data[attribute].value_counts()))
        attribute_count = sum([value[1] for value in attribute_class_count])
        return list(map(lambda value: value[1]/attribute_count, attribute_class_count))

    def run(self):
        # Find entropy of target
        target_prob_list = self.probabilities(self.target_attribute)
        target_entropy = self.entropy(target_prob_list)
        print("Entropy of target ({}): {} ".format(self.target_attribute,target_entropy))

        # Find root node


if __name__ == "__main__":
    data_headers = ['engine', 'turbo', 'weight', 'fueleco', 'fast']
    data = pd.read_csv("id3_data.csv", names=data_headers, header=None)
    id3 = ID3(data,"fast")
    id3.run()
