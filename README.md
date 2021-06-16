Bài trước chúng ta đã tìm hiểu sơ bộ về streamlit. Trong bài này mình muốn chia sẻ cách deploy model (thực ra cái gì cũng được) lên Heroku thông qua streamlit thông qua Github.

Để deploy lên Heroku ngoài các file của project chúng ta cần tạo thêm 3 file:
* `Procfile` (procurement file) chứa thông tin `web: sh setup.sh && streamlit run [name_app].py`. Ở đây `[name_app].py` là file chạy của bạn. Trong này chứa các câu lệnh để thực thi khi mở app.
* `requirements.txt` chứa các packages dùng cho project, có thể tạo file này qua lệnh sau
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