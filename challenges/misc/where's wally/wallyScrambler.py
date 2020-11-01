from PIL import Image
import sys
from random import choice
import csv
import pprint

curColour = (20,20,20)


def main():
    global curColour
    dimensions = {}

    try:
        wallyImage = Image.open("wheres wally unscrambled.jpg")
        img = Image.new("RGB", (wallyImage.size[0],wallyImage.size[1]), "white")
    except IOError:
        print("Unable to load image")
        sys.exit(1)

    # NOTE: Size 1024 means indexes go from 0-1023
    pixels = img.load()

    rects = []

    # Start from 0,0 and iterate through every pixel to create a rectangle.
    # If the pixel is not white then that means it has been filled already and doen't need a rectangle
    # NOTE: These are indexes
    posX = 0
    posY = 0

    # posX bounds is implemented inside the loop
    while not (posY >= img.size[1]):
        # print(f"Current Position: {posX},{posY}")

        # Check if position already filled
        if pixels[posX,posY] == (255,255,255):
            # Bind rect size by the grid limit
            limitX = 60
            if posX + 100 > img.size[0] - 1:
                limitX = img.size[0] - posX

            limitY = 60
            if posY + 100 > img.size[1] - 1:
                limitY = img.size[1] - posY

            rectSizeX = choice([i for i in range(40,limitX,20)] + [-1])
            rectSizeY = choice([i for i in range(40,limitY,20)] + [-1])

            if rectSizeX != -1 and rectSizeY != -1:
                # Check if rectangle is valid
                if isValid(pixels,posX,posY,rectSizeX,rectSizeY):
                    curRect = createRect(pixels,posX,posY,rectSizeX,rectSizeY)
                    rects.append(curRect)
                    # Add rectangle to dimensions dictionary
                    dimension = f"{rectSizeX}x{rectSizeY}"
                    if dimension not in dimensions:
                        dimensions[dimension] = [curRect]
                    else:
                        dimensions[dimension].append(curRect)

                posX += rectSizeX + 1
            else:
                posX += 1
        else:
            posX += 1

        # posX bounds checking
        if posX >= img.size[0]:
            posX = 0
            posY += 1

    '''
    pp = pprint.PrettyPrinter(width=41,compact=True)
    pp.pprint(dimensions)
    print(f"Dimension Count: {len(dimensions)}")

    dimensionColours = {}
    # Dimension dependent colours
    for d in dimensions.keys():
        curColour = changeColour(curColour)
        dimensionColours[d] = curColour

    # Redraw rects with new colours
    for rect in rects:
        dimension = f"{rect[2]}x{rect[3]}"
        tempColour = dimensionColours[f"{rect[2]}x{rect[3]}"]
        # print(f"{dimension} {tempColour}")

        for i in range(rect[0],rect[0] + rect[2] + 1):
            for j in range(rect[1],rect[1] + rect[3] + 1):
                pixels[i,j] = tempColour
    '''

    wallyPixels = wallyImage.load()

    # Swap around same dimensions
    for d in dimensions.values():
        # Random choice of indexes
        indexOrder = []
        for i in range(0,len(d)):
            indexOrder.append(choice([index for index in range(0,len(d)) if index not in indexOrder]))

        # Index for the ordered indexes
        tempCount = 0
        for index in indexOrder:
            # Swap when index hasn't been swapped yet
            if index > tempCount:
                # Swap the pixels for each rectangle by drawing over each other
                swapPixels(wallyPixels,d[tempCount],d[index])

            tempCount += 1

    img.show()
    wallyImage.show()
    img = img.save("rectangles.jpg")
    wallyImage = wallyImage.save("wheres wally.jpg")

    # Not needed for easy
    # createCSV(rects)

'''
Figure this out
'''
def swapPixels(wallyPixels,firstRect,secondRect):
    # Save firstRect pixels
    '''
    oldPixels = []

    oldPixelRow = 0
    oldPixelCol = 0
    for row in firstRect:
        oldPixels.append([])
        for tempColour in row:
            oldPixels[oldPixelRow][oldPixelCol] = tempColour
            oldPixelCol += 1
        oldPixelRow += 1
    '''

    # Get a list of pixels for both rectangles
    firstRectPixels = []
    for row in range(firstRect[0],firstRect[0] + firstRect[2] + 1):
        for col in range(firstRect[1],firstRect[1] + firstRect[3] + 1):
            firstRectPixels.append(wallyPixels[row,col])

    secondRectPixels = []
    for row in range(secondRect[0],secondRect[0] + secondRect[2] + 1):
        for col in range(secondRect[1],secondRect[1] + secondRect[3] + 1):
            secondRectPixels.append(wallyPixels[row,col])


    # Overwrite firstRect pixels in wally pixels
    tempIndex = 0
    for row in range(firstRect[0],firstRect[0] + firstRect[2] + 1):
        for col in range(firstRect[1],firstRect[1] + firstRect[3] + 1):
            wallyPixels[row,col] = secondRectPixels[tempIndex]
            tempIndex += 1

    tempIndex = 0
     # Overwrite secondRect pixels in wally pixels
    for row in range(secondRect[0],secondRect[0] + secondRect[2] + 1):
        for col in range(secondRect[1],secondRect[1] + secondRect[3] + 1):
            wallyPixels[row,col] = firstRectPixels[tempIndex]
            tempIndex += 1





'''
Check if rectangle space is empty
'''
def isValid(pixels,posX,posY,sizeX,sizeY):
    for i in range(posX,posX+sizeX+1):
        for j in range(posY,posY+sizeY+1):
            try:
                if pixels[i,j] != (255,255,255):
                    return False
            except:
                print("Invalid pixel ",i,j)
                return False
    return True


'''
Arguments: (pixels,posX,posY,sizeX,sizeY)
'''
def createRect(pixels,posX,posY,sizeX,sizeY):
    global curColour
    # i and j are offsets to the current position
    for i in range(0,sizeX+1):
        for j in range(0,sizeY+1):
            if i == 0 or i == sizeX or j == 0 or j == sizeY:
                pixels[posX + i,posY + j] = (0,0,0)
            else:
                pixels[posX + i,posY + j] = curColour

    curColour = changeColour(curColour)
    return [posX,posY,sizeX,sizeY,curColour]

'''
Colour is specified
'''
def drawRect(pixels,posX,posY,sizeX,sizeY,colour):
    for i in range(0,sizeX+1):
        for j in range(0,sizeY+1):
            if i == 0 or i == sizeX or j == 0 or j == sizeY:
                pixels[posX + i,posY + j] = (0,0,0)
            else:
                pixels[posX + i,posY + j] = colour



def changeColour(colour):
    colourList = list(colour)

    if colourList[0] + 10 <= 220:
        colourList[0] += 20
    elif colourList[1] + 10 <= 220:
        colourList[1] += 20
    elif colourList[2] + 10 <= 220:
        colourList[2] += 20

    if colourList[0] >= 200 and colourList[1] >= 220 and colourList[2] >= 220:
        colourList = [20,20,20]

    return tuple(colourList)

'''
posX,posY,sizeX,sizeY
'''
def createCSV(rects):
    with open("pieces_easy.csv","w",newline="") as csvfile:
        piecesWriter = csv.writer(csvfile, delimiter=",",
                quotechar="|",quoting=csv.QUOTE_MINIMAL)
        for rect in rects:
            piecesWriter.writerow(rect)



if __name__=="__main__":
    main()
