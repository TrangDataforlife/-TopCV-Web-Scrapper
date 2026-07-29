import random
import subprocess
import sys
import time

# --- 1. CÀI ĐẶT CÁC THƯ VIỆN CẦN THIẾT ---
subprocess.run([sys.executable, "-m", "pip", "install", "bs4"])
subprocess.run([sys.executable, "-m", "pip", "install", "lxml"])
subprocess.run([sys.executable, "-m", "pip", "install", "html5lib"])

# --- 2. IMPORT CÁC THƯ VIỆN ---
import pandas as pd
import requests
from bs4 import BeautifulSoup

# --- 3. CẤU HÌNH BAN ĐẦU ---
base_url = "https://www.topcv.vn/tim-viec-lam-data-analyst-tai-ho-chi-minh-kl2?type_keyword=1&sba=1&locations=l2"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        " (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
    ),
    "Accepted-Language": "vi-VN,vi;q=0.9,en-US;q=0.8",
}

# --- 4. THU THẬP DANH SÁCH LINK TỪ TRANG CHÍNH ---
page = requests.get(base_url, headers=HEADERS)
soup = BeautifulSoup(page.content, "lxml")

job_links = soup.find_all("a", attrs={"aria-label": True})

link_list = []
for job in job_links:
    href = job.get("href")
    # Chỉ lấy link thật, bỏ qua javascript popup và None
    if href and href.startswith("https://www.topcv.vn/"):
        link_list.append(href)

# --- 5. CÀO THÔNG TIN CHI TIẾT TỪNG VIỆC LÀM ---
data = []
for link in link_list:
    # Retry khi gặp lỗi 429 (Rate Limit)
    while True:
        new_webpage = requests.get(link, headers=HEADERS)
        if new_webpage.status_code == 429:
            print("Bị chặn 429, đợi lâu hơn rồi thử lại...")
            time.sleep(random.uniform(15, 30))
            continue
        break

    new_soup = BeautifulSoup(new_webpage.content, "lxml")

    # Trích xuất Tên công việc
    job_title_element = new_soup.find("h1", class_="box-header-job__title")
    job_title = (
        " ".join(job_title_element.text.split()) if job_title_element else ""
    )

    # Trích xuất Tên công ty
    company_name_el = new_soup.find("a", class_="name")
    company_name = company_name_el.text.strip() if company_name_el else ""

    # Khởi tạo Dictionary theo đúng thứ tự bạn yêu cầu
    job_info = {
        "job_title": job_title,  # 1. Tên công việc
        "company_name": company_name,  # 2. Tên công ty
        "link": link,  # 3. Đường link
        "location": "",  # 4. Địa điểm
        "experience": "",  # 5. Kinh nghiệm
        "deadline": "",  # 6. Hạn ứng tuyển
    }

    # Bổ sung các thông tin chi tiết
    for item in new_soup.find_all("div", class_="list-info__content"):
        title_el = item.find("div", class_="list-info__content__title")
        desc_el = item.find("div", class_="list-info__content__desc")

        title = title_el.get_text(strip=True) if title_el else ""
        desc = desc_el.get_text(strip=True) if desc_el else ""

        if "Địa điểm" in title:
            job_info["location"] = desc
        elif "Kinh nghiệm" in title:
            job_info["experience"] = desc
        elif "Hạn" in title:
            job_info["deadline"] = desc

    data.append(job_info)

    # Nghỉ 1 lần ngắn sau mỗi link thay vì nghỉ nhiều lần rải rác
    time.sleep(random.uniform(3, 7))

# In dữ liệu dạng dễ nhìn (Pretty Print)
print(json.dumps(data, ensure_ascii=False, indent=4))

with open("topcv.md", "w", encoding="utf-8") as job_file:
    job_file.write(pd.DataFrame(data).to_markdown(index=False))