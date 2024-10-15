from utime import sleep_ms
import uos

def TakePicture(imageName, resolution, cam):
    finalImageName = imageName
    if not '.jpg' in finalImageName:
        finalImageName = finalImageName + '.jpg'
    cam.resolution = resolution
    #Kept getting an error saying to add 500ms of delay
    sleep_ms(500)
    cam.capture_jpg()
    sleep_ms(500)
    cam.saveJPG(finalImageName)

def TakeMultiplePictures(imageName, resolution, interval, count, cam):
    cam.resolution = resolution
    for x in range(count):
        if x!=0:
            endImageName = imageName + str(x + 1) + '.jpg'
            try:
                uos.remove(endImageName)
            except:
                print("File does not exist")
    for x in range(count): 
        endImageName = imageName + str(x + 1) + '.jpg'
        TakePicture(endImageName, resolution, cam)
        sleep_ms(500)
        if x==0:
            uos.remove(endImageName)
        sleep_ms(interval)