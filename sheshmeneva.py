import pandas


accuracy_data = pandas.read_excel(r'/content/my_func_data.xlsx')
accuracy_data.drop('Unnamed: 2', axis=1, inplace=True) # из общей таблицы удаляются столбцы с данными по метрике Performance:
accuracy_data.drop('Unnamed: 4', axis=1, inplace=True)
accuracy_data.drop('Unnamed: 6', axis=1, inplace=True)
accuracy_data.drop(0, axis=0, inplace=True) # удаляется строка с заглавиями метрик Accuracy и Performance (т.к. остались только данные по метрике Accuracy)
accuracy_data.to_csv(r'accuracy.csv', encoding='utf-8', sep=';', index=False) # создается .csv-файл с оставшимися данными по метрике Accuracy для всех функций на всех процессорах

performance_data = pandas.read_excel(r'/content/my_func_data.xlsx')
performance_data.drop('Processor A', axis=1, inplace=True) # из общей таблицы удаляются столбцы с данными по метрике Performance:
performance_data.drop('Processor B', axis=1, inplace=True)
performance_data.drop('Processor C', axis=1, inplace=True)
performance_data.drop(0, axis=0, inplace=True) # удаляется строка с заглавиями метрик Accuracy и Performance, т.к. остались только данные по метрике Performance
performance_data.columns = ['Functions', 'Processor A', 'Processor B', 'Processor C'] # "пустые" названия столбцов (Unnamed: 2, Unnamed: 4, Unnamed: 6) меняются на соответствующие данным в них
performance_data.to_csv(r'performance.csv', encoding='utf-8', sep=';', index=False) # создается .csv-файл с данными по метрике Performance для всех функций на всех процессорах
