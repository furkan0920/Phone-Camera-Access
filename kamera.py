import cv2
#telefon icin telefonunuza �pwebcami indiriniz ve oradaki ip adresinizi id istenilen yera yaziniz
url="http://�d'ninizi yaz�n�z/video"

cam=cv2.VideoCapture(url)

while cam.isOpened():
    ret,frame=cam.read()
    
    if not ret:
        print("kameradan goruntu okunamadi")
        
    cv2.imshow("goruntu",frame)
    
    if cv2.waitKey(1)==ord("q"):
        break
    
cv2.destroyAllWindows()    
    