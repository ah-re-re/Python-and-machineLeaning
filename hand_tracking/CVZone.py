import cv2
from cvzone.HandTrackingModule import HandDetector  #thư viện https://github.com/cvzone/cvzone

cap = cv2.VideoCapture(0)  #tạo đối tượng cap
cap.set(1, 1280)    #đặt kích thước: chiều rộng, chiều cao
cap.set(2, 720)

detector = HandDetector(detectionCon= 0.8 ) #độ nhaỵ tìm kiếm hands
starDist = None
scale = 0
cx, cy = 500, 500
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread("cvarduino.jpg")  #đọc ảnh từ file

    if len(hands) == 2:
        # print("asdasd")
        #print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            # print("hasdjasd")
            #nếu toạ độ tay phải và trái là [1, 1, 0, 0, 0] thì ch/trình chấp nhận zoom
            lmList1 = hands[0]["lmList"] #tạo danh sách cho tay trái
            lmList2 = hands[1]["lmList"] #tạo danh sách cho tay phải

            if starDist is None:

                lenght, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                starDist = lenght #khoảng cách bắt đầu sẽ bằng độ dài

            lenght, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((lenght - starDist) // 2)
            cx, cy = info[4:]
            print(scale)
    else:
        starDist = None
    try:
        h1, w1, _ = img1.shape
        newH, newW = (((h1 + scale)-1/2) // 2) * 2, (((w1 + scale)-1/2) // 2) * 2
        #newH, newW = ((h1 + scale) *2) //2 , ((w1 + scale) * 2) //2

        img1 = cv2.resize(img1, (newW, newH))
        #để không bị lỗi định dạng ảnh:
        # VD: nếu ảnh ảnh = 90 (tổng cạnh+ chiều cao)
        #       nếu 90/2 = 49,5 + 50, nhưng 49,5 sẽ bị làm tròn xuống 49 ==> 49 + 50 != 99
        #     chia hết cho 2 rồi nhân thêm 2 lần nữa rồi chia hết cho 2, tuy chỉ là gần bằng nhưng có thể được


        #img[cy - newH -20 :cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1
        img[cy - newH - 20:cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1
    except:
        pass

    img[10:260, 10:260] = img1
    cv2.imshow("Image", img)
    cv2.waitKey(1)