def sublistHelper(chosen,available):
    if len(available) == 0:
        print(chosen)

    else:
        element = available[0]
        available.pop(0)
        sublistHelper(chosen,available)  # Without
        chosen.append(element)
        sublistHelper(chosen, available) # With
        # Unchoose
        available.append(element)
        chosen.remove(element)


def sublist(available):
    chosen = []
    sublistHelper(chosen,available)

def main():
    items = ["Agnik","Troyee","Arthi","Ayan"]
    sublist(items)

main()


'''
Output:

[]
['Ayan']
['Arthi']
['Arthi', 'Ayan']
['Troyee']
['Troyee', 'Arthi']
['Troyee', 'Ayan']
['Troyee', 'Ayan', 'Arthi']
['Agnik']
['Agnik', 'Troyee']
['Agnik', 'Ayan']
['Agnik', 'Ayan', 'Troyee']
['Agnik', 'Arthi']
['Agnik', 'Arthi', 'Ayan']
['Agnik', 'Arthi', 'Troyee']
['Agnik', 'Arthi', 'Troyee', 'Ayan']

'''