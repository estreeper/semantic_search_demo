from InstructorEmbedding import INSTRUCTOR
import numpy

model = INSTRUCTOR('hkunlp/instructor-base')

def calculate_embedding(instruction, text):
    embeddings = model.encode([[instruction, text]])
    # convert from numpy ndarray type to regular list
    list_embeddings = numpy.ravel(embeddings).tolist()

    return list_embeddings
