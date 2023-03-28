import logging

logging.basicConfig(format="[%(levelname)s]:%(lineno)s - %(message)s", level=logging.DEBUG)
LOGGER = logging.getLogger()



## CREDIT TO: https://stackoverflow.com/a/65568586
def level_contents(str1):
    level_dict = {}
    level = 0
    level_char = ''
    for s in str1:
        if s == '(':
            if level not in level_dict:
                level_dict[level] = [level_char]
            elif level_char != '':
                level_dict[level].append(level_char)
            level_char = ''
            level += 1
        elif s == ')':
            if level not in level_dict:
                level_dict[level] = [level_char]
            elif level_char != '':
                level_dict[level].append(level_char)
            level_char = ''
            level -= 1
        else:
            level_char += s
    
    return level_dict