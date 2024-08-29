import cv2
import schedule,time


def job():
    try:
        timestr = time.strftime("%Y.%m.%d %H.%M")
        vc1 = cv2.VideoCapture("rtsp://admin:admin@10.10.103.60:554/stream2")
        ret1, frame1 = vc1.read()
        cv2.imwrite(f'./pole1/pole1({timestr}).jpeg', frame1)
        vc1.release()
    except cv2.error:
        print('Камера Поле1 недоступна')
        
    try:
        vc2 = cv2.VideoCapture("rtsp://admin:C0rsa!r9@10.10.103.61:554/main")
        ret2, frame2 = vc2.read()
        cv2.imwrite(f'./pole2/pole2({timestr}).jpeg', frame2)
        vc2.release()
    except cv2.error:
        print('Камера Поле2 недоступна')

    try:
        vc3 = cv2.VideoCapture("rtsp://admin:120579@10.10.103.66:554/h264")
        ret3, frame3 = vc3.read()
        cv2.imwrite(f'./pole3/pole3({timestr}).jpeg', frame3)
        vc3.release()
    except cv2.error:
        print ('Камера Поле3 недоступна')

    try:
        vc4 = cv2.VideoCapture("rtsp://admin:120579@10.10.103.67:554/h264")
        ret4, frame4 = vc4.read()
        cv2.imwrite(f'./pole4/pole4({timestr}).jpeg', frame4)
        vc4.release()
    except cv2.error:
        print ('Камера Поле4 недоступна')
        
    print(f'Отработано {timestr}')


print ('Запущено')
schedule.every(55).minutes.do(job)
while True:
   schedule.run_pending()
   time.sleep(1)

