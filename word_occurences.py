import pprint


input_str = "Hola que tal, bienvenidos un dia más a hola. En en ESté tExt0 de Prueba de hoy vamos a HOLA resolver cosa. hOlá"
# input_str = """Thank you for this wonderful job opportunity in research. I am a Mechatronics Engineer professionally since April 2019 in Colombia. During my studies at the university, I was a member of the student research group in robotics (SIR): A Research Group that conducts projects in Robotics focuses on Intelligent Systems. As a result of my work in the group, I found a particular interest in the field of Computer vision and Intelligent systems and because of that, I have tried to focus my skills and competence area in perception (my degree project consisted of a computer vision module to estimate geometry features of an individual tree such as a trunk diameter, tree height and crown volume using a point cloud representation built from a set of 2D digital images from a RGB monocular camera). Thanks to that project, I participated in the Colombian Conference on Robotics and Automation CCRA 2018 where I achieved my first article published on the IEEE . After my graduation (I got my degree on 4 April of 2019), I was admitted for a Research role in Embedded systems at the IMaR Technology Gateway: A research centre on Intelligent Mechatronics and RFID from the Institute of Technology Tralee in Ireland (1.6 years) where I worked on projects focused on IoT and Computer vision applications until December 2020.
# Now, I am back in Colombia where I have been taking online courses in Deep learning (DeepLearning.AI TensorFlow Developer Specialization) at coursera.org, computer science and software development. I consider AI as a fundamental technology that I will need to domain in my field if I want to work in Academia or in Industry as a research engineer and that’s why I think this job could give me a superb opportunity to learn from top experts in AI and computer vision, machine learning as well to connect with possible job references in my future."""

"""Normalize word formato to standard format
"""


def normalized_word(word):
    word = word.lower().replace('.', ' ').replace(',', ' ').replace(' ', '')
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b)
    return word


"""Count words from normalized format O(n) time complexity 
"""


def count_words(input):
    words = input.split(' ')
    print("words: ", words)
    result = dict()
    for word in words:
        word = normalized_word(word)
        if word in result:
            result[word] += 1
            pass
        else:
            result[word] = 1
            pass
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(result)


count_words(input_str)
