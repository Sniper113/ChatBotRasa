## ChatBotRasa

## Mục lục

* [Giới thiệu về RASA](#giới-thiệu-về-RASA)
* [Hướng dẫn Buid và sử dụng](#Hướng-dẫn-Buid-và-sử-dụng)
* []()
* []()
* []()
* []()


# Giới thiệu về RASA

Dự án nghiên cứu tìm hiểu chatbot trong tư vấn bán hàng, được xây dựng trên thư viện mã nguồn mở RASA để làm chatbot, RASA có hai modul chính là RASA NLU - Nature Language Uderstanding dùng để hiểu và xử lý ngôn ngữ tự nhiên (tóm lại để hiểu xem người dùng muốn gì) và RASA Core để xử lý trả lời khách hàng 

## Yêu cầu hệ thống

 * 'Operating Systems: Linux (Ubuntu, CentOS), Mac'
    
 * 'Python 3.6+

# Hướng dẫn Buid và sử dụng

Bây giờ muốn chạy được cần cài thêm thư viện asa_core, sklearn_crfsuite và spacy bằng lệnh:

pip install rasa_core sklearn_crfsuite spacy rasa_nlu

Sau đó gõ thêm lệnh sau để tải ngôn ngữ cho spacy:

python -m spacy download en

## Nhập dữ liệu cho module NLU

Trong modul NLU có khái niệm intent - ý đồ của khách hàng. Ví dụ nếu KH Chat "Cần mua điện thoại iphone" hay "mua điện thoại" thì tuy 2 câu khác nhau nhưng cùng một ý đồ - intent là "mua_điên_thoại"
Ở đây mình đã nhập dữ liệu trong file nlu.md và sẽ có cấu trúc như sau

Trong đó :
* ## intent: greet là ý đồ của khách hàng là greet(chào hỏi)
* Các câu còn bên dưới là các mẫu câu chat chúng ta quy ước vào intent/ý đồ chào hỏi. Mình cũng có thể thêm nhiêu câu như:"Chào","Alo",...

Mỗi intent có tầm từ 10 câu trở lên để đạt được kết quả cao nhất
hình 1
## Train và kiểm tra module NLU
Module NLU cần phải được kiểm tra kỹ trước khi làm các bước tiếp theo bởi vì nếu ta hiểu sai ý đồ/intent của khách hàng thì các bước sau đều sai cả

Mở file train_nlu.py,  nhìn ở dòng cuối có các lệnh gọi hàm ask_question, mục đích là để chúng ta truyền thử các câu hỏi của khách hàng vào xem modul NLU có đoán đúng ý đồ không:
hinh ask_qs

Với những câu như trên là đang thử "Chào bạn", "Anh là Lâm", "bye" và "điện thoại 2gb ram" xem modul NLU nhận dạng như nào. Có thể chạy file train_nlu.py bằng IDE lập trình (Pycharm, VS…) hoặc gõ lệnh python train_nlu.py và nhìn trên màn hình kết quả có dạng như sau:

hình train

Chúng ta để ý những con số trên, với những con số ứng với mỗi intent
 * Với câu "Chào bạn", máy đã nhận đúng là intent greet vơi độ tin tưởng là 0.789
 * Với câu "bye", máy đã nhận đúng là intent bye vơi độ tin tưởng là 0.567

Vậy nên, với độ tin tưởng càng lớn mà nghĩa của câu gần đúng với intent đã đặt thì modul NLU đã đoán đúng ý đồ

## Train modul RASA Chatbot Core

Như vậy, modul NLU đã xong, máy đã có thể hiểu được chúng ta nói gì, bây giờ đên phần thứ 2, train cho RASA Chatbot 
