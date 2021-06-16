Bài trước chúng ta đã tìm hiểu sơ bộ về streamlit. Trong bài này mình muốn chia sẻ cách deploy model (thực ra cái gì cũng được) lên Heroku thông qua streamlit thông qua Github.

Để deploy lên Heroku ngoài các file của project chúng ta cần tạo thêm 3 file:
* `Procfile` (procurement file) chứa thông tin `web: sh setup.sh && streamlit run [name_app].py`. Ở đây `[name_app].py` là file chạy của bạn. Trong này chứa các câu lệnh để thực thi khi mở app.
* `requirements.txt` chứa các packages dùng cho project, có thể tạo file này qua lệnh sau hoặc bạn cài packages nào thì ghi vào.
```python
pip freeze > requirements.txt
```
* `setup.sh` - chứa shell script dùng để thiết lập shell environment. Nội dùng của file `setup.sh` như sau.
```python
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```
**Chú ý:** Nếu dùng OpenCV trên Heroku thì trong file `requirements.txt` nên để `opencv-python-headless` chứ không phải `opencv-contrib-python` để tránh một số lỗi `ImportError: libGL.so.1: cannot open shared object file: No such file or directory`

Các bạn có thể xem thêm demo của mình tại [github-huytranvan2010](https://github.com/huytranvan2010/Deploy-DLmodel-with-Streamlit) hoặc tự tạo cho mình một project để chạy thử.

## Bổ sung - Deploy qua Heroku CLI 
Để deploy được app qua Heroku CLI đầu tiên chúng ta cần cài [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), sau đó cài [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up). Khí có có thể chạy các câu lệnh `heroku` từ command shell. Sử dụng `heroku login` để đăng nhập vào Heroku CLI.
**1.** Chuẩn bị files
Cũng tương tự như deploy sử dụ Github chúng sẽ sẽ cần các files của project và 3 file `setup.sh, requirements.txt và Profile` như trên
**2.** Tạo Git repository (nếu chưa có)
```python
git init
```
**3.** Login vào Heroku
```python
heroku login
```
Lúc này nó sẽ đưa mình đến trang đăng nhập, chỉ cần đăng nhập vào đó là được.
**4.** Deploy app
```python
heroku create
```
Khi tạo app một git remote (gọi là heroku) sẽ được tạo và kết nối với local git repository. Heroku sẽ tự tạo tên ngẫu nhiên cho app hoặc chúng ta có thể đặt tên cho app như sau:
```python
heroku create name-of-your-app
```
Sau đó thực hiện bước cuối cùng
```python
git push heroku main
```
hoặc
```python
git push heroku master
```
Heroku sẽ tự động nhận diện file, cài các packages cần thiết mà chúng ta đã setup. Khi kết thúc sẽ hiện ra đường link cho chúng ta.
Có thể kiểm tra xem app đã được deploy thành công chưa thông qua câu lệnh:
```python
heroku ps:scale web=1
```
Mở đường link bên trên hoặc mở bằng câu lệnh `heroku open` để thưởng thức.

##### Tài liệu tham khảo
1. https://www.geeksforgeeks.org/deploy-your-machine-learning-web-app-streamlit-on-heroku/
2. https://github.com/huytranvan2010/Deploy-DLmodel-with-Streamlit
3. https://gilberttanner.com/blog/deploying-your-streamlit-dashboard-with-heroku
