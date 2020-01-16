# import nuke
# import os

# n_read_list = [x for x in nuke.allNodes() if x.Class()=='Read']

# def writeFromRead(lst, outDir):
#     global nuke
#     for x in lst:
#         fileName = x.knob('file').getValue()
#         _filename, _ext = os.path.splitext(os.path.split(fileName)[1])
#         print(fileName)

#         #create write
#         n_write = nuke.createNode('Write')
#         n_write.knob('file').setValue(os.path.join(outDir, _filename+'.exr'))
#         n_write.knob('file_type').setValue('exr')
#         n_write.knob('raw').setValue(1)
#         n_write.knob('metadata').setValue(3)
#         n_write.knob('compression').setValue(2)
#         n_write.setInput(0, x)
#         #print('dir is {} and file is {} extension is {}'.format(dir,file,'.png'))

# writeFromRead(n_read_list, r'G:/Python/qt/tx_ice_test/')

import os
_filename = 'COL_1001'
_ext = '.exr'
ext = 'same'
pFix = ''
sFix = 'end'
if ext == 'same':
    ext = _ext
if pFix!='':
    _filename = pFix+_filename
if sFix!='':
    _filename = _filename+sFix

print(_filename+ext)
