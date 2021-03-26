import numpy as np
import json

# spilt = ['train', 'test', 'dev']
# doc = ['caps.json', 'ims.npy', 'ims_bbx.npy', 'ims_size.npy']
# loc = 'C:\\Users\\18834\\PycharmProjects\\GSMN-master\\f30k_precomp\\'
# print('size of different files of dataset:')
# for s in spilt:
#     print('size of %s' % s)
#     for d in doc:
#         path = loc + s + '_' + d
#         print(path)
#         if d.find('json') > -1:
#             with open(path) as f:
#                 caps = json.load(f)
#                 print(len(caps))
#         else:
#             numpy_file = np.load(path, allow_pickle = True)
#             print(numpy_file.shape)

path = r"vocab/coco_precomp_vocab.json"
with open(path) as f:
    d = json.load(f)
print(type(d))
print(d['word2idx'])
print(d['idx'])
