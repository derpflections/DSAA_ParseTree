# Name: Teo Wei Qi & Lee Hong Yi
# Student ID: p2201902 & p2223010
# Class: DAAA/FT/2B/07


class AssignmentEvaluator():
    """
    A class for evaluating assignments within a hash table based on certain bounds.

    Attributes:
        __hashTable (HashTable): The hash table containing the assignments to evaluate.
        __bounds (list): A list of upper bounds for evaluation ranges.
    """

    def __init__(self, HashTable, bounds=[240,  135.5,  16,  15,  1, None]):
        """
        Initialize the AssignmentEvaluator with a hash table and optional bounds.
        
        Args:
            HashTable (HashTable): The hash table to evaluate.
            bounds (list, optional): A list of upper bounds for evaluation ranges. Defaults to [240,  135.5,  16,  15,  1, None].
        """
        self.__hashTable = HashTable
        self.__bounds = bounds

    def evaluation(self):
        """
        Evaluate the assignments in the hash table based on the defined bounds and return a formatted string.
        
        Returns:
            str: A formatted string containing evaluated assignments grouped by their value ranges.
        """
        eval_list = []
        exp_list = []
        output_str = ""
        last_bound = float("inf")
        for key in self.__hashTable.__getkeys__():
            item = self.__hashTable.__getitem__(key)
            exp = item.getExp()
            eval = item.getEval()
            exp_list.append(exp)
            eval_list.append(eval)
        
        for bound in (b for b in self.__bounds if b is not None):
            output_str += f"*** Statements with value => {bound}\n"
            for i in range(0, len(exp_list)):
                if isinstance(eval_list[i], (int, float)) and bound <= eval_list[i] < last_bound:
                    output_str += f"{exp_list[i]}\n"
            last_bound = bound
            output_str += "\n"
        
        output_str += "*** Statements with value => None\n"
        for i in range(0, len(exp_list)):
            if not isinstance(eval_list[i], (int, float)):
                output_str += f"{exp_list[i]}\n"
        
        return output_str


