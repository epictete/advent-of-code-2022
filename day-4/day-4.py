class Cleanup:

    def __init__(self, demo=False):
        self.input = self.open_file(demo)

    @staticmethod
    def open_file(demo):
        input_data = []
        with open(f'day-4{demo and "-demo" or ""}.txt', 'r') as file:
            for line in file:
                a, b = line.strip().split(',')
                input_data.append([
                    list(map(int, a.split('-'))),
                    list(map(int, b.split('-'))),
                ])
        return input_data

    @staticmethod
    def check_condition(part, section):
        a, b = section
        a_low, a_high = a
        b_low, b_high = b
        if part == 1:
            # Check if 'a' contains 'b' or 'b' contains 'a'.
            return (a_low <= b_low and a_high >= b_high) or (b_low <= a_low and b_high >= a_high)
        elif part == 2:
            # Check if 'a' and 'b' have an intersection.
            return not (a_high < b_low or b_high < a_low)
        else:
            return False

    def solve(self, part):
        print(sum(1 for section in self.input if self.check_condition(part, section)))


cleanup_demo = Cleanup(demo=True)
cleanup_demo.solve(1)  # 2
cleanup_demo.solve(2)  # 4

cleanup = Cleanup(demo=False)
cleanup.solve(1)  # 560
cleanup.solve(2)  # 839
