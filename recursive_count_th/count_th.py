'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, current_count = 0):
    th_count = current_count

    if 'th' in word:
        th_count += 1
        index = word.index('th')
        return count_th(word[index+2:], th_count)
    else:
        return th_count

print(count_th('othullythththTHjsjshsjthjsjsksjTH'))
