## ChatBotRasa

## Mục lục

* [Giới thiệu về RASA](#giới-thiệu-về-RASA)
* [Cài đặt thư viện](#Cài-đặt-thư-viện)
* [Nhập dữ liệu cho module NLU](#Nhập-dữ-liệu-cho-module-NLU)
* [Train và kiểm tra module NLU](#Train-và-kiểm-tra-module-NLU)
* [Train modul RASA Chatbot Core](#Train-modul-RASA-Chatbot-Core)
* [Train và test Chatbot](#Train-và-test-Chatbot])


# Giới thiệu về RASA

  Dự án nghiên cứu tìm hiểu chatbot trong tư vấn bán hàng, được xây dựng trên thư viện mã nguồn mở RASA để làm chatbot, RASA có hai modul chính là RASA NLU - Nature Language Uderstanding dùng để hiểu và xử lý ngôn ngữ tự nhiên (tóm lại để hiểu xem người dùng muốn gì) và RASA Core để xử lý trả lời khách hàng 

## Yêu cầu hệ thống

 * 'Operating Systems: Linux (Ubuntu, CentOS), Mac'
    
 * 'Python 3.6+

# Cài đặt thư viện

  Bây giờ muốn chạy được cần cài thêm thư viện asa_core, sklearn_crfsuite và spacy bằng lệnh:

    pip install rasa_core sklearn_crfsuite spacy rasa_nlu

  Sau đó gõ thêm lệnh sau để tải ngôn ngữ cho spacy:

    python -m spacy download en

# Nhập dữ liệu cho module NLU

  Trong modul NLU có khái niệm intent - ý đồ của khách hàng. Ví dụ nếu KH Chat "Cần mua điện thoại iphone" hay "mua điện thoại" thì tuy 2 câu khác nhau nhưng cùng một ý đồ - intent là "mua_điên_thoại"
Ở đây mình đã nhập dữ liệu trong file nlu.md và sẽ có cấu trúc như sau

![](img/intent.jpg)

  Trong đó :
  
   * intent: greet là ý đồ của khách hàng là greet(chào hỏi)
   * Các câu còn bên dưới là các mẫu câu chat chúng ta quy ước vào intent/ý đồ chào hỏi. Mình cũng có thể thêm nhiêu câu               như:"Chào","Alo",...

  Mỗi intent có tầm từ 10 câu trở lên để đạt được kết quả cao nhất
hình 1
# Train và kiểm tra module NLU
  Module NLU cần phải được kiểm tra kỹ trước khi làm các bước tiếp theo bởi vì nếu ta hiểu sai ý đồ/intent của khách hàng thì các bước sau đều sai cả

  Mở file nlu_model.py,  nhìn ở dòng cuối có các lệnh gọi hàm ask_question, mục đích là để chúng ta truyền thử các câu hỏi của khách hàng vào xem modul NLU có đoán đúng ý đồ không:

![](img/ask.jpg)

  Với những câu như trên là đang thử "Chào bạn", "Anh là Lâm", "bye" và "điện thoại 2gb ram" xem modul NLU nhận dạng như nào. Có thể chạy file nlu_model.py bằng IDE lập trình (Pycharm, VS…) hoặc gõ lệnh python nlu_model.py và nhìn trên màn hình kết quả có dạng như sau:

![](img/train.jpg)

  Chúng ta để ý những con số trên, với những con số ứng với mỗi intent
   * Với câu "Chào bạn", máy đã nhận đúng là intent greet vơi độ tin tưởng là 0.789
   * Với câu "bye", máy đã nhận đúng là intent bye vơi độ tin tưởng là 0.567

  Vậy nên, với độ tin tưởng càng lớn mà nghĩa của câu gần đúng với intent đã đặt thì modul NLU đã đoán đúng ý đồ

# Train modul RASA Chatbot Core
 
  Như vậy, modul NLU đã xong, máy đã có thể hiểu được chúng ta nói gì, bây giờ đên phần thứ 2, train cho RASA Chatbot phản ứng lại những gì khách hàng nói

  Ở phần này có 2 file cần hiểu đó là domain.yml và stories.md của RASA Chatbot

## File domain.yml

  Nếu như file nlu.md là để lưu các câu nói của khách hàng ứng với ý đồ nào thì file domain.yml là định nghĩa các câu phản hồi của bot với các ý đồ của khách hàng (gọi là các utter, ứng với intent ở trên)

  File domain.yml sẽ có 3 phần chính
   * Phần 1: Liệt kê lại các intent của khách hàng
   * Phần 2: Phần templates, cũng là phần quang trọng. Phần này liệt kê các utter phản hồi lại các intent của khách hàng. Mỗi utter có thể định nghĩa nhiều câu text và bot sẽ chọn random các câu text này để phản hồi. Như bên dưới là utter_greet (để chào lại khách hàng khi khách chào mình) chỉ có 1 text nhưng utter_bye (để chào tạm biệt khách khi khách tạm biệt mình) thì có 2 câu text. Trong phần này cần chú ý có một utter đặc biệt là utter_unclear, utter này sẽ được gọi khi máy không hiểu được ý của người dùng, khi đó máy sẽ nói các câu dạng như “Thưa quý khách, hiện tại tôi chưa hiểu được yêu cầu của Quý khách” thay vì im tịt.
 
 ![](img/templates.jpg)
 
   * Phần 3: Liệt kê lại các utter có trong phần 2
 
 ![](img/domain.jpg)
 
 ## File stories.md
 
  File này như một file kể chuyện, để kết nối giữa intent và utter. Nếu như nlu.md định nghĩa intent, domain.yml định nghĩa utter. Nhưng máy đâu có hiểu là intent nào thì dùng utter nào đâu. Và đó là lý do phải có thêm file stories.md để ghép nối.
 
  File này có dạng như sau
  
  ![](img/stories.jpg)
  
  Như đoạn trên là định nghĩa 1 đoạn chat giữa người và máy. Người vào chào hỏi, máy chào lại, rồi người hỏi tên, máy trả lời, rồi hỏi tiếp các món máy có thể làm, rồi tạm biệt…

  Chúng ta cố gắng nghĩ ra càng nhiều đoạn hội thoại càng tốt, thì máy sẽ càng thông minh khi chat và nội dung chat mềm dẻo hơn. Có thể xem thêm nội dung trong file stories.md trong thư mục dự án

# Train và test Chatbot

  Với những file đã chuẩn bị đây đủ, chúng ta có thể bắt đầu train cho Bot

  Ta mở file train_dialog.py và chạy file bằng IDE lập trình (Pycharm, VS…) hoặc gõ lệnh python train_dialog.py, sau khi máy chạy hết 200 Epoch và nhìn trên màn hình kết quả có dạng như sau:

 ![](img/train_dialog.jpg)

  Sau khi train xong thì chúng ta chạy tiếp file test_dialog.py, nó sẽ hiện ra một cửa sổ chat và chúng ta có thể chat với bot để test.

 Và đây là kết quả

 ![](img/test_bot.jpg)

































