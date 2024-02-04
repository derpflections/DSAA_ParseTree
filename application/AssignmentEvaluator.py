# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07


class AssignmentEvaluator():
    def __init__(self, HashTable, bounds = [240, 135.5, 16, 15, 1, None]):
        self.__hashTable = HashTable
        self.__bounds = bounds

    def evaluation(self):
        eval_list = []
        exp_list = []
        output_str = ""
        last_bound = float("inf")
        for key in (self.__hashTable.__getkeys__()):
            # print(key)
            item = self.__hashTable.__getitem__(key)
            exp = item.getExp()
            eval = item.getEval()
            exp_list.append(exp)
            eval_list.append(eval)
        for bound in (b for b in self.__bounds if b is not None):
            output_str += f"*** Statements with value => {bound}\n\n"
            for i in range(0, len(exp_list)):
                if isinstance(eval_list[i], (int, float)) and bound <= eval_list[i] < last_bound:
                    output_str += f"{exp_list[i]}\n\n"
            last_bound = bound
            output_str += "\n"
        output_str += "*** Statements with value => None\n\n"
        for i in range(0, len(exp_list)):
            if not isinstance(eval_list[i], (int, float)):
                output_str += f"{exp_list[i]}\n\n"
        return output_str

