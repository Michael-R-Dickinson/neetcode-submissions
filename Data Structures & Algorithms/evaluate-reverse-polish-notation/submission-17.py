class Solution:
    def isIntegerString(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    """
    returns
        A tuple where the first value represents the evaluation of the operator
        The second represents the length in the string of the operator and its arugments
    """
    def evalRPNOperator(self, tokens: List[str], operator_idx: int) -> Tuple[int, int]:
        operator = tokens[operator_idx]
        if self.isIntegerString(operator):
            return (int(operator), 1)
        
        # evaluate the right argument - use the length to determine the idx of the left operator
        # evaluate the left argument
        # apply the outer argument to combine them

        # print('right output', self.evalRPNOperator(tokens, operator_idx - 1))
        right_eval, right_arg_length = self.evalRPNOperator(tokens, operator_idx - 1)
        left_eval, left_arg_length = self.evalRPNOperator(tokens, operator_idx - 1 - right_arg_length)

        print(left_eval, operator, right_eval)

        operator_seq_length = right_arg_length + left_arg_length + 1
        if operator == "+":
            return right_eval + left_eval, operator_seq_length
        if operator == "-":
            return left_eval - right_eval, operator_seq_length
        if operator == "*":
            return right_eval * left_eval, operator_seq_length
        if operator == "/":
            return int(left_eval / right_eval), operator_seq_length
        print('OPERATOR UNKNOWN', operator)

    def evalRPN(self, tokens: List[str]) -> int:
        eval, _ = self.evalRPNOperator(tokens, len(tokens) - 1)
        return eval
    
        
        