#!/bin/python3

from typing import List


class Grid:
    grid: List[str]

    def __init__(self, grid: List[str]):
        self.grid = grid

    def grid_challenge(self) -> str:
        self.validate_non_empty_grid()
        word_length = len(self.grid[0])
        self.validate_every_word_same_length(word_length)

        self.rearrange_rows_alphabetical_order()

        for letter_index in range(word_length):
            column_word = ''.join([word[letter_index] for word in self.grid])
            if not self.is_word_ordered(column_word):
                return "NO"
        return "YES"

    def rearrange_rows_alphabetical_order(self) -> None:
        for index, word in enumerate(self.grid):
            self.grid[index] = self.alphabetical_rearrange(word)

    def validate_every_word_same_length(self, word_length: int) -> None:
        for i in range(1, len(self.grid)):
            if len(self.grid[i]) != word_length:
                raise Exception("Not every word has same length.")

    def validate_non_empty_grid(self) -> None:
        if len(self.grid) == 0:
            raise Exception("No grid passed.")

    @staticmethod
    def array_letters_to_string(sorted_letters: List[str]) -> str:
        sorted_word = ''
        for letter in sorted_letters:
            sorted_word += letter
        return sorted_word

    @staticmethod
    def alphabetical_rearrange(word: str) -> str:
        # return ''.join(sorted(word))
        sorted_letters = sorted(word)
        return Grid.array_letters_to_string(sorted_letters)

    @staticmethod
    def is_word_ordered(word: str) -> bool:
        sorted_word = ''.join(sorted(word))
        return word == sorted_word
