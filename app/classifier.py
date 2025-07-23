
class Classifier:

    def __init__(self, trained_data, query_dict):
        self.trained_data = trained_data     # the dict of the df values
        self.query_dict = query_dict
        self.dict_values = self.trained_data.dict_values()
        self.dict_class_values = self.trained_data.dict_class()

    # calculate the probability and return answer
    def probability(self):
        """ calculate the probability for dict of option """
        prob_dict = {}
        # mult probability for each option column
        for keys in self.dict_values:
            probability = 1
            for key, value in self.query_dict.items():
                if self.dict_values[keys][key][value] != 0 :
                    probability *= self.dict_values[keys][key][value]
                # add 1 if found 0
                else:
                    self.dict_values[keys][key][value] += 1
                    probability *= self.dict_values[keys][key][value]
                prob_dict[keys] = probability * self.dict_class_values[keys]
        return max( prob_dict,key=prob_dict.get)
