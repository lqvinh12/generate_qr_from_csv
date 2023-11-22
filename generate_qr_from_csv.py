import qrcode
import qrcode.image.svg
from datetime import datetime
import os

# SVG config
factory = qrcode.image.svg.SvgImage
timestamp = str(int(datetime.now().timestamp()))
os.mkdir(f'output2/{timestamp}/')
# Generate
codeList = open('codeList.txt').readlines()
counter = 1
partname = "PCB ASSY (MAIN)"
transaction = ""
for singleSKU in codeList:
    SKUArray = singleSKU.replace("\n", "").split(",")
    partNumber = SKUArray[0]
    partSKU = SKUArray[1]
    partCondition = SKUArray[2]
    try:
        transaction = SKUArray[3]
    except:
        transaction = ""

    qrString = f"{partNumber}|{partname}|0|0|0|Được thể hiện trên bao bì|_|_|_|{partCondition}|_|{partSKU}|sYu1bh6ReR9ycil7bmCFhi38ghezNPgpEvRHCh9ls6AWQe"
    counterString = str(counter)
    if len(counterString) == 1:
        counterString = "000" + counterString
    elif len(counterString) == 2:
        counterString = "00" + counterString
    elif len(counterString) == 3:
        counterString = "0" + counterString

    # myImg = qrcode.make(qrString, image_factory = factory) For Svg
    myImg = qrcode.make(qrString)
    imgName = "output2/" + timestamp + "/"+transaction + \
        "_" + partNumber + "_" + partSKU + ".png"
    myImg.save(imgName)
    counter += 1
print(f'>>> Export done! Pls check the output/{timestamp}/')
