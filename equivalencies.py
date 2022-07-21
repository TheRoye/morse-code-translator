import pandas

data = pandas.read_csv("traductor-morse\morse.csv")
elements = data.to_dict('split')['data']

equivalencies = { element[0] : element[1] for element in elements}
equivalencies['"'] = equivalencies.pop('comillas dobles')

