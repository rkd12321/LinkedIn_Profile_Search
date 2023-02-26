# LinkedIn_Profile_Search
구글검색을 활용하여 링크드인 프로필 검색(링크드인으로 크롤링 시 차단되기 때문임)<br> 

## 1. 프로필 검색 환경 구성하기 (OS 환경 : Amazon linux2)
### 1) python & pip3 설치
---

```
sudo yum isntall python3 pip3 
```

### 2) 크롬 설치를 위한 yum 레파짓토리 추가
---
#### - yum 레파짓토리 파일 생성
```
sudo vi /etc/yum.repos.d/google-chrome.repo
```
#### - 생성한 yum 레파짓토리 파일에 아래의 내용 추가
---
```
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/<br>stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/<br>linux_signing_key.pub
```
### 3) 크롬 드라이버 설치
---
#### - 크롬 설치 및 버전 확인
```bash
sudo yum install google-chrome-stable # 크롬 설치
google-chrome --version # 설치한 크롬의 버전 확인
```
#### - 크롬 드라이버 다운로드 및 압축 풀기 [크롬 드라이버 다운 경로 직접 확인](https://chromedriver.storage.googleapis.com/index.html)
```bash
wget -N http://chromedriver.storage.googleapis.com/[크롬 버전 입력]/chromedriver_linux64.zip # 크롬 드라이버 다운로드
unzip chromedriver_linux64.zip # 압축 풀기 
```
### 4) 셀레니움(Selenium) 설치 
---
```bash
sudo pip3 install selenium
```

### 5) search_profile.py 수정 
---
#### - 예시 경로 /home/ec2-user/chromedriver
#### - 수정 전
```py
### load selenium driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('[크롬 드라이버 경로 입력]',options=options)
driver.set_window_size(1920, 1080)
```
#### - 수정 후
```py
### load selenium driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/home/ec2-user/chromedriver',options=options)
driver.set_window_size(1920, 1080)
```
