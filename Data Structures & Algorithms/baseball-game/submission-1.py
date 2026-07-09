class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # iterate through operations
        # apply the operation at each step. Log it onto the record. Record is an array (stack)

        record = []
        for operation in operations:
            int_val = None
            try:
                int_val = int(operation)
            except:
                pass
            
            if isinstance(int_val, int):
                record.append(int_val)
            elif operation == "C":
                record.pop()
            elif operation == "D":
                record.append(record[-1] * 2)
            elif operation == "+":
                record.append(record[-1] + record[-2])

        return sum(record)
