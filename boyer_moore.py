class BoyerMoore:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

    def create_shift_table(self) -> dict[str, int]:
        # init dict for character and his number of shits
        skip_list = {}

        for i in range(0, len(self.pattern)):
            # use formula->value = max(1, length of pattern - index - 1)
            skip_list[self.pattern[i]] = max(1, len(self.pattern) - i - 1)

        return skip_list

    def search(self) -> list[int]:
        # create bad char shift table
        bad_char = self.create_shift_table()
        print("Shift table is ", bad_char)

        # the current right most char index from the text from where we start comparison
        i = len(self.pattern) - 1

        # init the list where we will write the resulting indices
        result_of_search = []

        while i <= len(self.text) - 1:
            # index for char from pattern
            j = 0

            # checking whether the given character from the pattern (first time - last char in pattern) is identical
            # to the character at the same position ( first time - equals i) from the text
            while j < len(self.pattern) and self.pattern[len(self.pattern) - j - 1] == self.text[i - j]:
                j += 1

            # when j equals length of pattern - write index from text to result list
            if j == len(self.pattern):
                result_of_search.append(i - len(self.pattern) + 1)
                i += 1
                continue

            else:
                # get shift for current char and default value - shift for length of pattern
                # shift = bad_char.get(self.text[i+j], len(self.pattern) - 1) ?
                shift = bad_char.get(self.text[i+j], len(self.pattern))

                # count char for skips
                skips = shift - j

                i += skips

        for res in result_of_search:
            print("Find pattern on index ", res)
        print('')

        return result_of_search







