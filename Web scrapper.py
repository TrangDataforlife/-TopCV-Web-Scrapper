import random
import time
import json
import sys
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright

base_url = 'https://www.topcv.vn/tim-viec-lam-data-analyst-tai-ho-chi-minh-kl2?type_keyword=1&sba=1&locations=l2'

def main():
    data = []
    
    with sync_playwright() as p:
        # Khởi tạo trình duyệt Chromium giả lập máy thật
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            viewport={'width': 1280, 'height': 800},
            locale="vi-VN"
        )
        page = context.new_page()

        # 1. Lấy danh sách link job từ trang danh mục
        try:
            print("Đang mở trang danh mục TopCV...")
            page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(3000) # Đợi trang load render JS

            html_content = page.content()
            soup = BeautifulSoup(html_content, 'lxml')
            
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
        for idx, link in enumerate(link_list, 1):
            print(f"[{idx}/{len(link_list)}] Processing: {link}")
            try:
                page.goto(link, wait_until="domcontentloaded", timeout=20000)
                page.wait_for_timeout(random.randint(2000, 4000))
                
                new_soup = BeautifulSoup(page.content(), 'lxml')

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
            except Exception as err:
                print(f"  -> Lỗi khi truy cập link: {err}")
                
        browser.close()

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
