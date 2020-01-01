import argparse
import sys
sys.path.append("C:\Program Files\Pixar\RenderManProServer-22.5\lib\python2.7\Lib\site-packages")
import ice


def txConvertIce():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", help="input file to convert")
    parser.add_argument("outputFile", help="output file returned after conversion")

    args = parser.parse_args()
    inputFile = (args.inputFile)
    outputFile = (args.outputFile)
    loadFile = ice.Load(inputFile)
    bits = loadFile.GetMetaData()

    if bits['Original Bits Per Sample'] == 32:
        formatFile = ice.constants.FMT_EXRFLOAT
        loadFile.Save(outputFile, formatFile)
    if bits['Original Bits Per Sample'] in (16, 8):
        formatFile = ice.constants.FMT_EXRHALF
        loadFile.Save(outputFile, formatFile)

if __name__=='__main__':
    txConvertIce()

