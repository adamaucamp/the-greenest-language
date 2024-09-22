

import yaml
import os

pwd = os.getcwd()
file_path = os.path.realpath(__file__)
folder = os.path.dirname(__file__)

print("pwd \t\t",pwd)
print("folder \t\t",folder)
print("file_path \t",file_path)


langs = [
    f for f in os.listdir(folder + '/../languages') if os.path.isdir(folder + '/../languages')
]

print(langs)


lang_dict = {}
setup_times = []
key_words = []

for lang in langs:
  with open(folder + '/../languages/'+ lang +'/spec.yml', 'r') as f:
      data = yaml.load(f, Loader=yaml.SafeLoader)
      lang_dict[lang] = data
      setup_times.append(data['spec']['ux']['initial-setup-time'])
      key_words.append(data['spec']['keywords'])

# Print the values as a dictionary
# print(lang_dict)

# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = langs
# corresponding y axis values
y = key_words

# plotting the points
plt.bar(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

plt.savefig("graph.svg", format='svg', dpi=1200)
# function to show the plot
plt.show()
