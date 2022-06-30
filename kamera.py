import cv2
#telefon icin telefonunuza ýpwebcami indiriniz ve oradaki ip adresinizi id istenilen yera yaziniz
url="http://ýd'ninizi yazýnýz/video"

cam=cv2.VideoCapture(url)

while cam.isOpened():
    ret,frame=cam.read()
    
    if not ret:
        print("kameradan goruntu okunamadi")
        
    cv2.imshow("goruntu",frame)
    
    if cv2.waitKey(1)==ord("q"):
        break
    
cv2.destroyAllWindows()    
    