from operator import itemgetter


line_count_first = sum(1 for line in open('1.txt', encoding='utf-8'))
line_count_second = sum(1 for line in open('2.txt', encoding='utf-8'))
line_count_third = sum(1 for line in open('3.txt', encoding='utf-8'))
documents = {'1.txt': line_count_first, '2.txt': line_count_second, '3.txt': line_count_third}
sorted_documents = dict(sorted(documents.items(), key=itemgetter(1)))

for document in sorted_documents:
    with open(document, encoding='utf-8') as file_initial:
        lines_list = file_initial.readlines()
        lines_count_in_document = len(lines_list)
    with open('final_text.txt', 'a', encoding='utf-8') as file_final:
        file_final.write(document + '\n')
        file_final.write(f'{lines_count_in_document}' + '\n')
    for line in lines_list:
        with open('final_text.txt', 'a', encoding='utf-8') as file_final:
            file_final.write(line)
    with open('final_text.txt', 'a', encoding='utf-8') as file_final:
        file_final.write("\n")



