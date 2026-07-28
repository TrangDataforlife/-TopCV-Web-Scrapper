import random
import time
import json
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://www.topcv.vn/tim-viec-lam-data-analyst-tai-ho-chi-minh-kl2?type_keyword=1&sba=1&locations=l2'

# Header mô phỏng chính xác hành vi trình duyệt
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.topcv.vn/',
    'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}

def main():
    session = requests.Session()
    session.headers.update(HEADERS)

    # 1. Lấy danh sách link job
    try:
        # Truy cập trang chủ trước để lấy Cookie hợp lệ
        session.get('https://www.topcv.vn/', timeout=15)
        time.sleep(2)

        page = session.get(base_url, timeout=15)
        soup = BeautifulSoup(page.content, 'lxml')
        
        # Thử lấy tất cả các thẻ a chứa link công việc (bao gồm cả class job-title)
        job_links_tags = soup.find_all('a', href=True)

        link_list = []
        for job in job_links_tags:
            href = job.get('href')
            if href and '/viec-lam/' in href and href.startswith('https://www.topcv.vn/'):
                link_list.append(href)
                
        link_list = list(set(link_list))
        print(f"Tìm thấy {len(link_list)} công việc hợp lệ.")

    except Exception as e:
        print(f"Lỗi khi lấy danh sách job: {e}")
        link_list = []

    # 2. Cào chi tiết từng job
    data = []
    for idx, link in enumerate(link_list, 1):
        print(f"[{idx}/{len(link_list)}] Processing: {link}")
        
        max_retries = 3
        new_webpage = None
        
        for attempt in range(max_retries):
            try:
                res = session.get(link, timeout=15)
                if res.status_code == 429:
                    print(f"  -> Dính Rate limit. Đợi 15s...")
                    time.sleep(15)
                elif res.status_code == 200:
                    new_webpage = res
                    break
                else:
                    print(f"  -> Mã lỗi HTTP {res.status_code}")
                    break
            except Exception as err:
                print(f"  -> Lỗi kết nối: {err}")
                time.sleep(5)
                
        if not new_webpage:
            print("  -> Bỏ qua link này.")
            continue

        new_soup = BeautifulSoup(new_webpage.content, 'lxml')

        job_title_element = new_soup.find('h1', class_='box-header-job__title')
        job_title = " ".join(job_title_element.text.split()) if job_title_element else ''

        company_name_el = new_soup.find('a', class_='name')
        company_name = company_name_el.text.strip() if company_name_el else ''

        job_info = {
            'job_title': job_title,
            'company_name': company_name,
            'link': link,
            'location': '',
            'experience': '',
            'deadline': ''
        }

        for item in new_soup.find_all('div', class_='list-info__content'):
            title_el = item.find('div', class_='list-info__content__title')
            desc_el = item.find('div', class_='list-info__content__desc')

            title = title_el.get_text(strip=True) if title_el else ''
            desc = desc_el.get_text(strip=True) if desc_el else ''

            if 'Địa điểm' in title:
                job_info['location'] = desc
            elif 'Kinh nghiệm' in title:
                job_info['experience'] = desc
            elif 'Hạn' in title:
                job_info['deadline'] = desc

        data.append(job_info)
        time.sleep(random.uniform(2, 4))

    # 3. Xuất file
    if data:
        with open("jobs.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        df = pd.DataFrame(data)
        df_renamed = df.rename(columns={
            'job_title': 'Tên công việc',
            'company_name': 'Tên công ty',
            'link': 'Đường link',
            'location': 'Địa điểm',
            'experience': 'Kinh nghiệm',
            'deadline': 'Hạn ứng tuyển'
        })
        df_renamed.to_csv('topcv_jobs_pandas.csv', index=False, encoding='utf-8-sig')
        print("\n✅ Đã hoàn thành cào dữ liệu và xuất file thành công!")
    else:
        print("\n⚠️ Không có dữ liệu nào được thu thập.")
        sys.exit(1)

if __name__ == '__main__':
    main()
