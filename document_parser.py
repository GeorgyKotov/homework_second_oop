import os
from operator import itemgetter


def get_dict_documents(name_directory: str):
    file_path = os.path.join(os.getcwd(), name_directory)
    documents_list = os.listdir(file_path)
    documents_dict = {}
    for document in documents_list:
        line_count = sum(1 for line in open(file_path + f'\\{document}', encoding='utf-8'))
        documents_dict[document] = line_count
    return dict(sorted(documents_dict.items(), key=itemgetter(1)))


def final_file_completion(name_directory_files: str, name_final_file: str):
    documents_list = get_dict_documents(name_directory_files)
    for document in documents_list:
        file_path = os.path.join(os.getcwd() + f'\\{name_directory_files}' + f'\\{document}')
        with open(file_path, encoding='utf-8') as file_initial:
            lines_list = file_initial.readlines()
            lines_count_in_document = len(lines_list)
        with open(name_final_file, 'a', encoding='utf-8') as file_final:
            file_final.write(document + '\n')
            file_final.write(f'{lines_count_in_document}' + '\n')
        for line in lines_list:
            with open(name_final_file, 'a', encoding='utf-8') as file_final:
                file_final.write(line)
        with open(name_final_file, 'a', encoding='utf-8') as file_final:
            file_final.write("\n")


final_file_completion('documents', 'final_text.txt')


