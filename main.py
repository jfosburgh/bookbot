LETTERS='qwertyuiopasdfghjklzxcvbnm'

def main(bookf):
    with open(bookf, 'r') as book:
        contents = book.read().lower()
        words = contents.split()
        letter_counts = {}
        for letter in contents:
            if letter in LETTERS:
                if letter in letter_counts.keys():
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1

        sorted_letter_counts = {letter:letter_counts[letter] for letter in sorted(letter_counts.keys())}

        print(f'--- Begin report of {bookf} ---')
        print(f'{len(words)} found in the document\n')

        for letter, count in sorted_letter_counts.items():
            print(f'The \'{letter}\' character was found {count} times')

        print('--- End report ---')
        

if __name__ == '__main__':
    main('./books/frankenstein.txt')