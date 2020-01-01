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
    loadFile.Save(outputFile)

if __name__=='__main__':
    txConvertIce()
